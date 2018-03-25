"""
Collect distributions for demo of central limit theorem.

Add a new file that will return N samples from your distribution similar to example_dist.py.
Then add the name to the list below.


grep class Dist*py | sed 's/(BaseDistribution)://' | sed 's/class //' | sed 's/^Dist/from .Dist/' | sed 's/.py:/ import /'

grep -h class Dist*py | sed 's/(BaseDistribution):/\",/' | sed 's/class /\"/'

"""

from __future__ import absolute_import

from .Dist_test1 import Dist_test1

__all__ = (
	"Dist_test1",
	)


