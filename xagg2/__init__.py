# Eventually restrict to just pixel_overlaps and aggregate; with
# everything else happening behind the scenes (and the exporting
# happening as methods to the classes that are exported from those
# two functions)


__author__ = """advancehs"""
__email__ = "1019753743@qq.com"
__version__ = "0.0.7"



__all__ = [
    'xagg2',
]




from .wrappers import pixel_overlaps
from .auxfuncs import (normalize,fix_ds,get_bnds,subset_find)
from .core import (aggregate,read_wm)
from .options import get_options, set_options
