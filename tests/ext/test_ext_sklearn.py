from spiral import TestApp


class SklearnApp(TestApp):
    class Meta:
        extensions = ["sklearn"]


def test_dummy():
    with SklearnApp() as app:
        app.sklearn.random_forest()
