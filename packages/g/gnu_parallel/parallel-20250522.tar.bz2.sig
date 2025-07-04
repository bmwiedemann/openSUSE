#!/bin/bash

# To check the signature run:
#   echo | gpg
#   gpg --auto-key-locate keyserver --keyserver-options auto-key-retrieve parallel-20250522.tar.bz2.sig

echo | gpg 2>/dev/null
gpg --auto-key-locate keyserver --keyserver-options auto-key-retrieve $0
exit $?

-----BEGIN PGP SIGNATURE-----

iQUHBAABCgAdFiEEzaAaQgjE90UGEH570atFFoiIiIgFAmgvZWQACgkQ0atFFoiI
iIi6LiaeJx/Np5YNH/BHJdrdNlZomLQtRST5ZPcdGKr6viZJA7Fhyu2MVa2QzzTQ
7YC9Lo+1LwW2oSprfAcw1qlvQPWxskKJ+9ne8LRJIUASG9TMojDyBBA1el6RKGBS
NdMenmd2DLuI8ScHcwqXlkhreqKaDlWWb0NtLj7faFodfqEuAkm135DCgTMI3arA
doL3WnumvodlhTSMJLC9WeBd1RMGbFQNsjLVXBGY7GJ7l/cGG3OJFT0glb6TKevs
CDlTYBidvIUpHFV6CgRiMZNa/MCJfpdcqq/8Z+aOjQjvT8T92YgF5RR2m2bZP6eB
KAFse4wkrkvpauIw2i7pUmfwX+vDs4SbRhgaGqJKRFaKLkkgkF2oeXP8r7dQTODh
emxiOfur36VOqOySLcfCipAbqTLbyx4w+pnD989gJkU3JVhjJYUO1ZRzjXTrVb9d
12rxQ/1FRnAs7pJ8AIJzZYD3DsidtWH13s+aaA0EMWlrQBNmrAbC2OlGrHovSk/7
QKcCo/+z4wNJ9ImJkRYMAPl5fLvjI3RCA5ZGoBvMQfbpUmsYVCC0ZSemyb46KeFF
BMcjhrBuzMa6tlY++SjcAvyATdN6SC8XQ9HSKdvZ3LGsXdXT/HApi2cYumK9DX8h
vn0boFDr5f+Om2aJyE06kwKxeuSv73fXG8sSbCOB8kJ2/KzqLNiNnb6UKFWyXc1m
0AQ/ZoHxmEO2ov/OxyZRv/Ts68bxjr4V9mB6xFKWqoI/tEMcgtkKqLI7SDoKIvMs
BTlRYOKSBJorofq34gqzf3HY50D4Lj9YMDdxJHNV46SzOBzMVOAV6ZswmVwTpw/T
+wfyxzz/GVUFmXCdgqshTiC3ku6W0ouAADU9CodsIOPYp2GPgH1WH8brgKx3/vzj
wYZATpLtf3ruM8dxflSXv8xWn7T1Kq7QKlk49/cgpegoRoHzIQvlf0ia7Qi0hwP0
PQizzpcb54zwje1zqfEMx0OoiqJJDd0s8YYokRPEggVKezv5vNAeYq1yQkxq6ID7
LI84XBSeUd8CQiaGEHw1pkoiszrpJk35nv/2KpW6WbbxUD7UCfbYchp/Ltu8Bo7E
PJeEq1FDqRazmIvAu0EYsYJ6zetxYDja4RFTvxvhWkVxdlOJh3F9E9XwFZeBVXX2
5xXXiSF6PlL92ir+GEwNrIv29d3ktS9Esvqo/73OASBCZIVJ8UaFaYhCeCbjIhTe
RvpSHly6YaXtQySXA2x4oFKkdJpLN+W7xZiKJ43de4iOHXP5s9KLMyDHMgbf8sEw
BgN2S5iN1KRZjZxmc+11SSGDyOlnEBXJHfSbIjGmP/XJHGS3HJemyUiok6prAQFF
DhJ69AysLc+9HF+bIbd3KlCNOe17RfHZbTyao9yONRuc8vUknijOKKBkX4JvN7Xi
lxnQoGBiwRvltqwjEKXHyO22QrUkX92bSj5M1LqF8nN70CfOWutZO5gk19ut2M7H
i95OQFLxuFNchrG35j0fFoP1bW4Tzt3lYxCchmxP+pOBuHsZmWU5UD82L+ZCLbD2
OAbPkEHXFBEiKRpNDF+4X1hABumJPKAG+YoYV7ypVetpABGrZM8jF773VcTbjsRU
mdk5hdBUVyaJ29SY5HMV3pERGv/+5oqapP2bn0p96ResfhelnjTkjIX1
=e+yk
-----END PGP SIGNATURE-----
