# ensure we don't break imports from spiral namespace


def test_import():
    from spiral import App, Controller, ex, init_defaults  # noqa: F401
