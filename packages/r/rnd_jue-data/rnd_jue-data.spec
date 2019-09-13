#
# spec file for package rnd_jue-data
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define oname   rnd_jue

Name:           %{oname}-data
Version:        20141004
Release:        0
Summary:        Data files for R'n'D jue
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
Url:            http://www.jb-line.de/rnd/rnd_start_e.html
Source0:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/ZeldaII-1.0.0.zip
Source1:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Zelda-1.0.0.zip
Source2:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Emerald_Mine_Club-2.1.1.7z
Source3:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Snake_Bite-1.0.0.zip
Source4:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/BD2K3-1.0.0.zip
Source5:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Boulder_Dash_Dream-1.0.0.zip
Source6:        http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
Source7:        http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
# Downloaded from http://www.artsoft.org/RELEASES/unix/rocksndiamonds/rocksndiamonds-3.3.1.2.tar.gz
# Deleted all directories which are not level and packed than rockslevels
# Repacked as tar.gz
Source8:        rocksndiamonds.tar.gz
# These levels are once downloaded from disappeared site
# https://web.archive.org/web/20140110211740/http://www.bd-fans.com/RnD.html
# not all levels works which are on this site
Source9:        42_Steps.zip
Source10:       Alans_Random_Levels.zip
Source11:       Alexanders_Levels.zip
Source12:       Arcade_Levels.zip
Source13:       Be_a_bug.zip
Source14:       Contest_Levels.zip
Source15:       Danilo_Parantar_Serrano.zip
Source16:       Danilo_Parantar_Serrano_2.zip
Source17:       Gavin_Davidson_2006.zip
Source18:       Glasses.zip
Source19:       Hard_Skills.zip
Source20:       Haspeton.zip
# Designed only for R'n'D jue
Source21:       JuergenBonhagen.zip
Source22:       Learning_Maths.zip
Source23:       Little_Games.zip
Source24:       Magic_CEs.zip
Source25:       Manuel.zip
Source26:       Manuels_Sokoban_Levels.zip
Source27:       Master-Rocks.zip
Source28:       Memory.zip
Source29:       Mini_Levels_Ryan.zip
Source30:       Missions.zip
Source31:       Mixed_Levels.zip
Source32:       Mixed_Levels_2.zip
Source33:       MultiRandomLevel.zip
Source34:       My_Levels_of_Fun.zip
Source35:       Negundo_World_2.zip
Source36:       Negundo_World_3.zip
Source37:       P98_Level_Pack_1.zip
Source38:       Pacman.zip
Source39:       Puzzles_v1.8.zip
Source40:       Random_Games.zip
Source41:       Rocks_n_Diamonds_Fun.zip
Source42:       Ryans_Random_Levels.zip
Source43:       Slippery_Ground.zip
Source44:       Space_Invaders.zip
Source45:       Space_Invaders_2.zip
Source46:       Springlis_Levels.zip
Source47:       Stinky.zip
Source48:       Super_BD-Rock.zip
Source49:       rnd_the_h_world.zip
Source50:       Time_Gate_Rush.zip
Source51:       Venatir.zip
Source52:       Veysi_Orak_2006.zip
Source53:       Walpurgis_Collection.zip
Source54:       Warparound_Murphy.zip
# Repacked that is same than other rnd_tutorial_*
Source55:       Tutorial_Alpha.zip

%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif
BuildRequires:  unzip
Requires:       %{oname}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
"R'n'D jue" is an alternative version of Rocks'n'Diamonds, developed in
cooperation with R&D author Holger Schemel.

In contrast to the "rnd_jue -contribution package"
(still available on Download page) it is a separate and independent program
with the same source code as the original R'n'D but with a
completely different appearance.

This is based on the wide customizing features which have been developed
recently while all the integrated games have been produced with the R'n'D
Level Editor, which is actually a great "game creation tool" for
non-programmers. So far "R'n'D jue" is also an example for what is possible
with the old Rocks'n'Diamonds and should be an inspiration for potential
level designers and game developers.

Regarding the games and levels "R'n'D jue" is intended for players who have both
an eye for an attractive design and a bent especially for "puzzle games".
The user will also find "action" and many opportunities to test his
manual-skill - nevertheless, the main feature of "R'n'D jue" is primarily
to offer some (moderate) challenges for the brain.

Data files (levels, tapes, graphics, music, sound) for R'n'D jue.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}/levels

for l in %{S:6} %{S:7} %{S:8} ; do
    tar xfvz $l -C %{buildroot}%{_datadir}/%{oname}
done

for l in %{S:0} %{S:1} %{S:3} %{S:4} %{S:5} %{S:9} \
         %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} \
         %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28} %{S:29} \
         %{S:30} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36} %{S:37} %{S:38} %{S:39} \
         %{S:40} %{S:41} %{S:42} %{S:43} %{S:44} %{S:45} %{S:46} %{S:47} %{S:48} %{S:49} \
         %{S:50} %{S:51} %{S:52} %{S:53} %{S:54} ; do
     unzip $l -d %{buildroot}%{_datadir}/%{oname}/levels -x Readme.txt
done
unzip %{S:55} -d %{buildroot}%{_datadir}/%{oname}/levels/Tutorials

7z x %{S:2} -o%{buildroot}%{_datadir}/%{oname}/levels

# Remove not needed files
find %{buildroot}%{_datadir}/%{oname}/levels -name '*.broken' -delete \
            -or -name '*.orig' -delete -or -name '*.old' -delete \
            -or -name '*.Thumbs.db' -delete -or -name '*.conf~' -delete

# Remove conflict with R'n'D jue
rm -f  %{buildroot}%{_datadir}/%{oname}/levels/rnd_jue/levelinfo.conf

# Remove not working levels for R'n'D jue
rm -fr %{buildroot}%{_datadir}/%{oname}/levels/"Walpurgis Collection"/{"Walpurgis Gardens","Walpurgis World"}
rm -fr %{buildroot}%{_datadir}/%{oname}/levels/rnd_the_h_world/hwld_dceos

%if 0%{?suse_version}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%{_datadir}/%{oname}

%changelog
