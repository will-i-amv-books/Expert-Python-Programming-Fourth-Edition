from functools import partial
from http import HTTPStatus

from flask import Flask, request, Response
from redis import Redis

from backends import RedisBackend
from interfaces import ViewsStorageBackend


app = Flask(__name__)
PIXEL = (
    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00"
    b"\x00\x00\xff\xff\xff!\xf9\x04\x01\x00"
    b"\x00\x00\x00,\x00\x00\x00\x00\x01\x00"
    b"\x01\x00\x00\x02\x01D\x00;"
)


def track(storage: ViewsStorageBackend):
    try:
        referer = request.headers["Referer"]
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)

    storage.increment(referer)

    return Response(
        PIXEL,
        headers={
            "Content-Type": "image/gif",
            "Expires": "Mon, 01 Jan 1990 00:00:00 GMT",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
        },
    )


def stats(storage: ViewsStorageBackend):
    return storage.most_common(10)


@app.route("/")
def index():
    return """
    <html>
    <head></head>
    <body>
    <a href="/test">/test</a></br>
    <a href="/stats">/stats</a>
    </body>
    </html>
    """


@app.route("/test")
def test():
    return """
    <html>
    <head></head>
    <body><img src="/track"></body>
    </html>
    """


if __name__ == "__main__":
    views_storage = RedisBackend(
        redis_client=Redis(host="redis"),
        set_name="my-stats"
    )
    app.route("/track", endpoint="track")(partial(track, storage=views_storage))
    app.route("/stats", endpoint="stats")(partial(stats, storage=views_storage))
    app.run(host="0.0.0.0", port=8000)
