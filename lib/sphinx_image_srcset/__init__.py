from pathlib import Path
try:
    import importlib.metadata
    __version__ = importlib.metadata.version("sphinx-redirectfrom")
except ImportError:
    __version__ = "0+unknown"

from docutils.parsers.rst import Directive


def setup(app):
    RedirectFrom.app = app
    app.add_directive("redirect-from", RedirectFrom)
    app.connect("build-finished", _generate_redirects)


class RedirectFrom(Directive):
    required_arguments = 1
    redirects = {}

    def run(self):
        redirected_doc, = self.arguments
        env = self.app.env
        builder = self.app.builder
        current_doc = env.path2doc(self.state.document.current_source)
        current_reldoc, _ = env.relfn2path(current_doc)
        redirected_reldoc, _ = env.relfn2path(redirected_doc, current_doc)
        if redirected_reldoc in self.redirects:
            raise ValueError(
                f"{redirected_reldoc} is already noted as redirecting to "
                f"{self.redirects[redirected_reldoc]}")
        self.redirects[redirected_reldoc] = builder.get_relative_uri(
            redirected_reldoc, current_reldoc)
        return []


def _generate_redirects(app, exception):
    builder = app.builder
    if builder.name != "html" or exception:
        return
    for k, v in RedirectFrom.redirects.items():
        with Path(app.outdir, k + builder.out_suffix).open("x") as file:
            file.write(
                f'<html><head><meta http-equiv="refresh" content="0; url={v}">'
                f'</head></html>')
