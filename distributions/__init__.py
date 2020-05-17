
"""
Collect distributions for demo of central limit theorem.

Add a new file that will return N samples from your distribution similar to example_dist.py.
Then add the name to the list below.


grep class Dist*py | sed 's/(BaseDistribution)://' | sed 's/class //' | sed 's/^Dist/from .Dist/' | sed 's/.py:/ import /'

grep -h class Dist*py | sed 's/(BaseDistribution):/",/' | sed 's/class /"/'

"""

from __future__ import absolute_import
from .Dist_cmr653 import Dist_cmr653
from .Dist_rdm445 import Dist_rdm445
from .Dist_speedreed import Dist_speedreed
from .Dist_ltw244 import Dist_ltw244
from .Dist_bt1369 import Dist_bt1369
from .Dist_kc90 import Dist_kc90
from .Dist_rmr557 import Dist_rmr557
from .Dist_jam1535 import Dist_jam1535
from .Dist_at4227 import Dist_at4227
from .Dist_os852 import Dist_os852
from .Dist_ia1113 import Dist_ia1113
from .Dist_knd286 import Dist_knd286
from .Dist_aew492 import Dist_aew492
from .Dist_cah736 import Dist_cah736
from .Dist_phh250 import Dist_phh250
from .Dist_ks938 import Dist_ks938
from .Dist_sk7372 import Dist_sk7372
from .Dist_kc90_4 import Dist_kc90_4
from .Dist_sj2879 import Dist_sj2879
from .Dist_dmc731 import Dist_dmc731
from .Dist_sdl433 import Dist_sdl433
from .Dist_pbg240 import Dist_pbg240
from .Dist_pw1091 import Dist_pw1091
from .Dist_lac683 import Dist_lac683
from .Dist_ajt540 import Dist_ajt540
from .Dist_sm6779 import Dist_sm6779
from .Dist_mkb452 import Dist_mkb452
from .Dist_npl248 import Dist_npl248
from .Dist_speedreed2 import Dist_speedreed2
from .Dist_emm815 import Dist_emm815
from .Dist_yx1796 import Dist_yx1796
from .Dist_abw400 import Dist_abw400
from .Dist_sea438 import Dist_sea438
from .Dist_sb6187 import Dist_sb6187
from .Dist_ejt352 import Dist_ejt352
from .Dist_tt1392 import Dist_tt1392
from .Dist_jdg577 import Dist_jdg577


__all__ = (
"Dist_cmr653",
"Dist_rdm445",
"Dist_speedreed",
"Dist_ltw244",
"Dist_bt1369",
"Dist_kc90",
"Dist_rmr557",
"Dist_jam1535",
"Dist_at4227",
"Dist_os852",
"Dist_ia1113",
"Dist_knd286",
"Dist_aew492",
"Dist_cah736",
"Dist_phh250",
"Dist_ks938",
"Dist_sk7372",
"Dist_kc90_4",
"Dist_sj2879",
"Dist_dmc731",
"Dist_sdl433",
"Dist_pbg240",
"Dist_pw1091",
"Dist_lac683",
"Dist_ajt540",
"Dist_sm6779",
"Dist_mkb452",
"Dist_npl248",
"Dist_speedreed2",
"Dist_emm815",
"Dist_yx1796",
"Dist_abw400",
"Dist_sea438",
"Dist_sb6187",
"Dist_ejt352",
"Dist_tt1392",
"Dist_jdg577",
	)