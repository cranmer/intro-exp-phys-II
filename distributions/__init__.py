"""
Collect distributions for demo of central limit theorem.

Add a new file that will return N samples from your distribution similar to example_dist.py.
Then add the name to the list below.


grep class Dist*py | sed 's/(BaseDistribution)://' | sed 's/class //' | sed 's/^Dist/from .Dist/' | sed 's/.py:/ import /'

grep -h class Dist*py | sed 's/(BaseDistribution):/\",/' | sed 's/class /\"/'

"""

from __future__ import absolute_import

from .Dist_kc90 import Dist_kc90
from .Dist_rmr557 import Dist_rmr557
from .Dist_ap5312 import Dist_ap5312
from .Dist_cas955 import Dist_cas955
from .Dist_fay221 import Dist_fay221
from .Dist_fh828 import Dist_fh828
from .Dist_jam1535 import Dist_jam1535
from .Dist_jnt299 import Dist_jnt299
from .Dist_kc90 import Dist_kc90
from .Dist_knd286 import Dist_knd286
from .Dist_lac683 import Dist_lac683
from .Dist_lwp226 import Dist_lwp226
from .Dist_mm7253 import Dist_mm7253
from .Dist_omr234 import Dist_omr234
#from .Dist_os852 import Dist_os852
from .Dist_phh250 import Dist_phh250
from .Dist_pme240 import Dist_pme240
from .Dist_pr1392 import Dist_pr1392
from .Dist_pw1091 import Dist_pw1091
from .Dist_sm6779 import Dist_sm6779
from .Dist_rdm445 import Dist_rdm445
from .Dist_yz4244 import Dist_yz4244
from .Dist_speedreed import Dist_speedreed
from .Dist_speedreed2 import Dist_speedreed2

__all__ = (
"Dist_ap5312",
"Dist_cas955",
"Dist_rmr557",
"Dist_fay221",
"Dist_fh828",
"Dist_jam1535",
"Dist_jnt299",
"Dist_kc90",
"Dist_knd286",
"Dist_lac683",
"Dist_lwp226",
"Dist_speedreed",
"Dist_mm7253",
"Dist_omr234",
"Dist_phh250",
"Dist_pme240",
"Dist_pr1392",
"Dist_pw1091",
"Dist_rdm445",
"Dist_sm6779",
"Dist_yz4244",
"Dist_speedreed2",
	)


