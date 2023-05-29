<div align="center">

# wpm-reader

A file reader that show text word per word and you can controll the number of words per minute

[Contributing Guidelines](./CONTRIBUTING.md) · [Request a Feature](/-/issues/new?issuable_template=Feature) · [Report a Bug](/-/issues/new?issuable_template=Bug)

</div>

## Usage

You can install this package using [pip](https://pip.pypa.io/en/stable/):

```
$ pip install wpm_reader
```

You can now import this module on your Python project:

```python
import wpm_reader
```

## Development

To start developing this project, clone this repo and do:

```
$ make env-create
```

This will create a virtual environment with all the needed dependencies (using [tox](https://tox.readthedocs.io/en/latest/)). You can activate this environment with:

```
$ source ./.tox/wpm_reader/bin/activate
```

Then, you can run `make help` to learn more about the different tasks you can perform on this project using [make](https://www.gnu.org/software/make/).

## License

[Copyright](./LICENSE)