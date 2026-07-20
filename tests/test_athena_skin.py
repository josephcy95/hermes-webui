"""Athena skin registration and parchment/olive reading-palette affordances."""

from pathlib import Path

REPO = Path(__file__).parent.parent
CSS = (REPO / "static" / "style.css").read_text(encoding="utf-8")
BOOT_JS = (REPO / "static" / "boot.js").read_text(encoding="utf-8")
CONFIG_PY = (REPO / "api" / "config.py").read_text(encoding="utf-8")
INDEX_HTML = (REPO / "static" / "index.html").read_text(encoding="utf-8")
SHARE_HTML = (REPO / "static" / "share.html").read_text(encoding="utf-8")
I18N_JS = (REPO / "static" / "i18n.js").read_text(encoding="utf-8")


def test_athena_skin_is_registered_in_all_files():
    assert "{name:'Athena'" in BOOT_JS
    assert "athena:1" in INDEX_HTML
    assert "athena:1" in SHARE_HTML
    assert '"athena"' in CONFIG_PY


def test_athena_defines_both_light_and_dark_palettes():
    # Full light + dark palette skin (Sienna/Catppuccin pattern), not dark-only.
    assert ':root[data-skin="athena"]{' in CSS
    assert ':root.dark[data-skin="athena"]{' in CSS


def test_athena_light_palette_is_parchment():
    assert "--bg:#F6F3EB" in CSS
    assert "--sidebar:#EFEBE1" in CSS
    assert "--text:#33302A" in CSS


def test_athena_dark_palette_is_umber():
    assert "--bg:#1B1915" in CSS
    assert "--sidebar:#211E19" in CSS
    assert "--text:#D9D3C7" in CSS


def test_athena_accent_is_olive():
    # Light accent must stay dark enough for 4.5:1 link text on parchment;
    # dark accent is a lighter sage for the same reason on umber.
    assert "--accent:#55693E" in CSS
    assert "--accent:#A3B784" in CSS
    assert "--focus-ring:rgba(85,105,62,0.30)" in CSS


def test_athena_assistant_prose_uses_scoped_serif():
    # Serif is skin-scoped per docs/UIUX-GUIDE.md — it must never leak into
    # the global assistant prose stack.
    assert "--font-serif:" in CSS
    assert (
        ':root[data-skin="athena"] .msg-row[data-role="assistant"] '
        ".msg-body{font-family:var(--font-serif);}" in CSS
    )


def test_athena_i18n_lists_skin_in_all_locales():
    # 15 cmd_theme strings across locales (13 ASCII + 2 full-width parens);
    # athena sits between zeus and verdigris in each so the existing
    # trailing-skin assertions for verdigris keep passing.
    assert I18N_JS.count("/athena/") == 15
