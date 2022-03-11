VirusInfo Docs
==============

Getting started
---------------

.. _prerequisite:

Prerequisite.
~~~~~~~~~~~~~
| VirusInfo supports Python 3.8 or later.
| Therefore, it can also be used on Windows 7.

Installing
~~~~~~~~~~
This library is available from pypi. ::

    python3 -m pip install -U VirusInfo
    
Installation on Windows is as follows ::

    py -3 -m pip install -U VirusInfo

Congratulations. You have now completed the installation.    

Manuals
------------
`API Reference`_

.. _API Reference: api.html
`Changelog`_

.. _Changelog: changelog.html

Quickstart
------------
| Obtain the latest, nationwide confirmation of the cumulative number of infected patients.
| (v0.4.0)
.. code:: py

   import VirusInfo
   print(VirusInfo.Covid_19.japan_all())
   # 2022-03-09
   # 北海道188241
   # 青森県25182
   # 岩手県13149
   # 宮城県46200
   # 秋田県11519
   # 山形県13487
   # 福島県27461
   # 茨城県85211
   # 栃木県50739
   # 群馬県57235
   # 埼玉県350096
   # 千葉県298996
   # 東京都1086519
   # 神奈川県505130
   # 新潟県32572
   # 富山県21767
   # 石川県28240
   # 福井県15981
   # 山梨県18563
   # 長野県34172
   # 岐阜県58469
   # 静岡県99743
   # 愛知県351897
   # 三重県45896
   # 滋賀県56108
   # 京都府135668
   # 大阪府707967
   # 兵庫県286080
   # 奈良県63720
   # 和歌山県24637
   # 鳥取県7502
   # 島根県7290
   # 岡山県53641
   # 広島県79421
   # 山口県23702
   # 徳島県13030
   # 香川県22057
   # 愛媛県19383
   # 高知県13709
   # 福岡県256765
   # 佐賀県26238
   # 長崎県27922
   # 熊本県54361
   # 大分県26563
   # 宮崎県20511
   # 鹿児島県34689
   # 沖縄県106661
