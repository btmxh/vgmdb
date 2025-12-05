VGMdb
=========

[![Docker Pulls](https://img.shields.io/docker/pulls/hufman/vgmdb)](https://hub.docker.com/repository/docker/hufman/vgmdb)

# Fork description

Currently, all tests passed, but there is no guarantee that everything works as
expected. The old Docker code is basically completely rewritten from scratch,
and everything is now being bundled in a single Docker image.

Some fixes to the scraper logic is also included to keep up with vgmdb.net's
HTML changes. However, don't expect this fork to be actively maintained,
especially for miscellaneous endpoints that are not `album/*` and `artist/*`.
Nevertheless, feel free to open issues or pull requests if you find any problems
or want to contribute improvements, I will try to address them as I can.

Currently, this fork only exports one single Docker image `btmxh/vgmdb`, on
GitHub container registry (ghcr.io). This image, by default, run the web server
on port 80. It can also be run as celery workers by overriding the entrypoint.
See the `docker-compose.yml` for example usage.

# Original README from here

VGMdb.net is an excellent resource, containing gigabytes of information about video game music. It documents the relationships between games, albums that represent games, and all the people that contributed to an album.

However, VGMdb does not provide an API to access its information, which provides an obstacle to programs that want to use its information. This site is a way to programmatically access the information on VGMdb.net.

VGMdb.net stores the information of each item at a friendly URL, such as <a href="http://vgmdb.net/album/79">album/79</a> or <a href="http://vgmdb.net/artist/137">artist/137</a>. This friendly url will work on this site. Once there, an overview of the item's information can be found, along with a few extra features.

## Usage
In the right sidebar, there are links to view the page's information in different formats. The raw information that has been parsed out of the original VGMdb.net item is available in JSON format by adding ?format=json to any URL. The YAML format is also available for this information, available by adding ?format=yaml.

Additionally, an effort has been made to produce RDF tuples representing some of the information in VGMdb. The default HTML view of the data has RDFa encoded into it, allowing any RDFa library to parse the page. Additionally, RDF/XML and Turtle serialization formats are available.

The page will produce the output format that most-closely matches the request's HTTP Accept header. A particular format can be forced by adding ?format=html, ?format=xml, or ?format=turtle arguments to the URL

There are also links to validation services, to verify that the page's data is in fact valid and parseable in the respective formats. The main page doesn't produce any other formats, but every other page does.

## Development and Installation
Unit tests are employed, both in the parsing and in the output stages, to validate that the information is being correctly parsed and encoded. Run the tests.sh script to run the tests.

Most of any runtime requirements should be documented in requirements.txt. Use pip install -r requirements.txt to install them. **NOTE: for this fork, dependencies are declared in `pyproject.toml` instead.**

The run.py example script will start up an HTTP server process for the site. An example Apache2 configuration, using mod\_wsgi, is also provided. It should work just as well under any other WSGI server.

The `docker/docker-build.sh` script should produce a `vgmdb_reqs` base image with the dependencies and a `vgmdb` image with the current version of the code installed. This image exposes port 80, and `vgmdb/autoload_settings.py` implements loading optional dependencies and settings based on environment variables.
