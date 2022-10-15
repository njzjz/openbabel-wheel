import os
import sys
from pathlib import Path
from distutils import sysconfig

this_directory = Path(__file__).parent.absolute()
sp_dir = sysconfig.get_python_lib(1, 0, prefix=str(this_directory))
sys.path.insert(1, sp_dir)

from openbabel import __version__, openbabel

os.environ["BABEL_LIBDIR"] = str(this_directory / "lib" / "openbabel" / __version__)
os.environ["BABEL_DATADIR"] = str(this_directory / "share" / "openbabel" / __version__)
os.environ["LD_LIBRARY_PATH"] = str(this_directory / "lib") + ":" + os.environ.get("LD_LIBRARY_PATH", "")

__all__ = ["__version__", "openbabel"]
