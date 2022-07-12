from quart import Quart, render_template, request, session, url_for

app = Quart(__name__)


@app.route("/", methods=["GET"])
async def root():
    return await render_template("root.html")
    
