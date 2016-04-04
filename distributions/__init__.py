"""
Collect distributions for demo of central limit theorem.

Add a new file that will return N samples from your distribution similar to example_dist.py.
Then add the name to the list below.


grep class Dist*py | sed 's/(BaseDistribution)://' | sed 's/class //' | sed 's/^Dist/from Dist/' | sed 's/.py:/ import /'

grep -h class Dist*py | sed 's/(BaseDistribution):/\",/' | sed 's/class /\"/'

"""

from Dist_ac5790 import Dist_ac5790
from Dist_jeg535 import Dist_jeg535
from Dist_kc90 import Dist_kc90
from Dist_kc90_2 import Dist_kc90_2
from Dist_kc90_3 import Dist_kc90_3
from Dist_mh3908 import Dist_mh3908
from Dist_my1462 import Dist_my1462
from Dist_ptf223 import Dist_ptf223
from Dist_rdr335 import Dist_rdr335
from Dist_recast import Dist_recast
from Dist_vag273 import Dist_vag273
from Dist_vag273_1 import Dist_vag273_1
from Dist_vag273_2 import Dist_vag273_2

__all__ = ("Dist_ac5790",
	"Dist_jeg535",
	"Dist_kc90",
	"Dist_kc90_2",
	"Dist_kc90_3",
	"Dist_mh3908",
	"Dist_my1462",
	"Dist_ptf223",
	"Dist_rdr335",
	"Dist_recast",
	"Dist_vag273",
	"Dist_vag273",
	"Dist_vag273_2",)


