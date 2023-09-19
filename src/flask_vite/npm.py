import subprocess
from dataclasses import dataclass
from textwrap import dedent

from flask import current_app
from devtools import debug

# Assume npm is in the path for now.
NPM_BIN_PATH = "npm"


class NPMError(Exception):
    pass


@dataclass
class NPM:
    cwd: str = ""
    npm_bin_path: str = NPM_BIN_PATH

    def run(self, *args):
        try:
            _args = [self.npm_bin_path] + list(args)
            debug(_args)
            subprocess.run(_args, cwd=self.cwd)
        except OSError as e:
            if e.filename == self.npm_bin_path:
                msg = """
                It looks like node.js and/or npm is not installed or cannot be found.
                Visit https://nodejs.org to download and install node.js for your system.
                """
            elif e.filename == self.cwd:
                msg = f"""
                It looks like the current working directory for vite is not correct.
                cwd: {self.cwd}
                """
            else:
                msg = f"""
                An error occurred while running npm.
                cwd: {self.cwd}
                npm_bin_path: {self.npm_bin_path}
                """

            raise NPMError(dedent(msg))
