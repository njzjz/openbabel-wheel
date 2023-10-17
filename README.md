# openbabel-wheel

[![Pypi version](https://img.shields.io/pypi/v/openbabel-wheel)](https://pypi.org/project/openbabel-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dm/openbabel-wheel)](https://pypi.org/project/openbabel-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dw/openbabel-wheel)](https://pypi.org/project/openbabel-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dd/openbabel-wheel)](https://pypi.org/project/openbabel-wheel/)

`openbabel-wheel` is an unofficial repository to distribute OpenBabel prebuilt wheels through Pypi using

```sh
pip install openbabel-wheel
```

The package requires Python 3.7 and above.

The project is inspired by [rdkit-pypi](https://github.com/kuelumbus/rdkit-pypi) and powered by [scikit-build-core](https://github.com/scikit-build/scikit-build-core) and [cibuildwheel](https://github.com/pypa/cibuildwheel). 

## Available Builds

| OS      | Arch    | Bit | Conditions     | Python        | 
| ------- | ------- | --- | -------------- | ------------- |
| Linux   | x86_64  | 64  | glibc >= 2.17  | 3.7-3.12      | 
| macOS   | x86_64  | 64  | >= macOS-10.9  | 3.7-3.12      | 
| macOS   | arm64   | 64  | >= macOS-11    | 3.8-3.12      |  
| Windows | amd64   | 64  |                | 3.8-3.11      |

## Usage

### Python

```py
from openbabel import openbabel
```

### Command line

```sh
obabel -h
```

## License

`openbabel-wheel` distributed under the same [license](LICENSE) as OpenBabel.
For original OpenBabel repository, refer [openbabel/openbabel](https://github.com/openbabel/openbabel).
