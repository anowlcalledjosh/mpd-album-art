from setuptools import setup
setup(
    name="MPD-Album-Art",
    version="0.1",
    author="Jamie Macdonald",
    author_email="jamie.alban@gmail.com",
    description="Module to fetch Album Art for currently playing song on Music PLayer Daemon",
    license="GPL 3.0",

    url="http://jameh.github.io/mpd-album-art",

    packages=['mpd_album_art'],
    entry_points={
        'console_scripts': ["mpd-album-art=mpd_album_art.__main__:main"],
    },
    install_requires=['python-mpd2', 'pylast'],

    keywords="MPD, Album Art, LastFM",

    # could also include long_description, download_url, classifiers, etc.
)
