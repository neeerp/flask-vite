import glob
from textwrap import dedent

from flask import current_app


def make_vite_header_tag():
    js_file = glob.glob("vite/dist/assets/*.js")[0].split("/")[-1]
    css_file = glob.glob("vite/dist/assets/*.css")[0].split("/")[-1]
    tags = dedent(f"""
        <script type="module" crossorigin src="/assets/{js_file}"></script>
        <link rel="stylesheet" href="/assets/{css_file}">
    """)

    if current_app.debug:
        tags = dedent(f"""
            <!-- FLASK_VITE_HEADER -->
            <script type="module" src="http://localhost:3000/@vite/client"></script>
            <script type="module" src="http://localhost:3000/main.js"></script>
        """)
    else:
        tags = dedent(f"""
            <!-- FLASK_VITE_HEADER -->
            <script type="module" crossorigin src="/assets/{js_file}"></script>
            <link rel="stylesheet" href="/assets/{css_file}">
        """)

    return tags
