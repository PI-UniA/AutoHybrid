# AutoHybrid

    Project Repository of the publicly funded research project "AutoHybrid"



# ⚠️ Note: This package is still WIP ⚠️

# Installation

## Requirements

The package deps are all listed in a `.yml` File in the `docker-env/` directory.
To install them using conda:

```bash
conda create --name prosi3d --file docker-env/environment.yml
```

## Using `tox`

For now, you can use the package by invoking the `tox` build system:

```bash
tox -e build
```

## Using `setuptools`

Alternatively, you can use the Python package `setuptools` to build the local package:

```bash
python setup.py develop
```

## Using Docker

Lastly, you can build and run the Docker container that comes along with the package:

```bash
docker build . -t prosi3d:latest
```

Run the container in a terminal:

```bash
docker run --rm -ti prosi3d:latest
```