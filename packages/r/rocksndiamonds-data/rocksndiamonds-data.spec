#
# spec file for package rocksndiamonds-data
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


%define oname   rocksndiamonds

Name:           %{oname}-data
Version:        20141005
Release:        0
Summary:        Data files for Rocks'n'Diamonds
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
Url:            http://www.artsoft.org/rocksndiamonds/
Source0:        http://www.artsoft.org/RELEASES/%{oname}/levels/ZeldaII-1.0.0.zip
Source1:        http://www.artsoft.org/RELEASES/%{oname}/levels/Zelda-1.0.0.zip
Source2:        http://www.artsoft.org/RELEASES/%{oname}/levels/Emerald_Mine_Club-2.1.1.7z
Source3:        http://www.artsoft.org/RELEASES/%{oname}/levels/Sokoban-1.0.0.zip
# Use supplied tarbal, fixed with fdupes -l sym -r -m .
# and packed than rockslevels, repacked as tar.bz2
Source4:        Contributions-1.2.0.tar.bz2
Source5:        http://www.artsoft.org/RELEASES/%{oname}/levels/Snake_Bite-1.0.0.zip
Source6:        http://www.artsoft.org/RELEASES/%{oname}/levels/BD2K3-1.0.0.zip
Source7:        http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Boulder_Dash_Dream-1.0.0.zip
Source8:        http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
Source9:        http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
# Downloaded from http://www.jb-line.de/rnd/rnd_jue-3.3.0.0.tar.gz
# Deleted directory rnd_jue/jue_sobigo and other which are not level
# and packed than rockslevels, repacked as tar.gz
Source10:       rnd_jue.tar.gz
# These levels are once downloaded from disappeared site
# https://web.archive.org/web/20140110211740/http://www.bd-fans.com/RnD.html
# not all levels works which are on this site
Source11:       42_Steps.zip
Source12:       Alans_Random_Levels.zip
Source13:       Alexanders_Levels.zip
Source14:       Arcade_Levels.zip
Source15:       Be_a_bug.zip
Source16:       Bug_Hunter.zip
Source17:       Colourful_World.zip
Source18:       Contest_Levels.zip
Source19:       Danilo_Parantar_Serrano.zip
Source20:       Danilo_Parantar_Serrano_2.zip
Source21:       Gavin_Davidson_2006.zip
Source22:       Glasses.zip
Source23:       Hard_Skills.zip
Source24:       Haspeton.zip
Source25:       Learning_Maths.zip
Source26:       Little_Games.zip
Source27:       Love_Pac.zip
Source28:       Magic_CEs.zip
Source29:       Maniac_Mines.zip
Source30:       Manuel.zip
Source31:       Manuels_Sokoban_Levels.zip
Source32:       Master-Rocks.zip
Source33:       Memory.zip
Source34:       Mini_Levels_Ryan.zip
Source35:       Missions.zip
Source36:       Mixed_Levels.zip
Source37:       Mixed_Levels_2.zip
Source38:       MultiRandomLevel.zip
Source39:       My_Levels_of_Fun.zip
Source40:       Negundo_Dash.zip
Source41:       Negundo_World_2.zip
Source42:       Negundo_World_3.zip
Source43:       P98_Level_Pack_1.zip
Source44:       Pacman.zip
Source45:       Pipemania.zip
Source46:       Puzzles_v1.8.zip
Source47:       Random_Games.zip
Source48:       Rockfighter.zip
Source49:       Rocks_n_Diamonds_Fun.zip
Source50:       Ryans_Random_Levels.zip
Source51:       Slippery_Ground.zip
Source52:       Space_Invaders.zip
Source53:       Space_Invaders_2.zip
Source54:       Springlis_Levels.zip
Source55:       Stinky.zip
Source56:       Super_BD-Rock.zip
Source57:       Super_Comic_Levels.zip
Source58:       Super_Jetset_Willy_Bros_3.zip
Source59:       rnd_the_h_world.zip
Source60:       Through_the_Ages.zip
Source61:       Time_Gate_Rush.zip
Source62:       Trucky_Cargos_v0.1.zip
Source63:       Venatir.zip
Source64:       Veysi_Orak_2006.zip
Source65:       Walpurgis_Collection.zip
Source66:       Warparound_Murphy.zip
# Repacked that is same than other rnd_tutorial_*
Source67:       Tutorial_Alpha.zip
BuildRequires:  fdupes
%if 0%{?suse_version} > 1500
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif
BuildRequires:  unzip
Requires:       %{oname}
BuildArch:      noarch

%description
This is a nice little game with color graphics and sound for your Unix system
with color X11.  You need an 8-Bit color display or better.  It will not work
on black&white systems, and maybe not on gray scale systems.

If you know the game Boulder Dash (Commodore C64) or Emerald Mine (Amiga),
you know what Rocks'n'Diamonds is about.

Data files (levels, tapes, graphics, music, sound) for Rocks'n'Diamonds.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}/levels

tar -xjf %{S:4} -C %{buildroot}%{_datadir}/%{oname}

for l in %{S:8} %{S:9} %{S:10} ; do
    tar xfvz $l -C %{buildroot}%{_datadir}/%{oname}
done

for l in %{S:0} %{S:1} %{S:3}  %{S:5} %{S:6} %{S:7} \
         %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} \
         %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28} %{S:29} \
         %{S:30} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36} %{S:37} %{S:38} %{S:39} \
         %{S:40} %{S:41} %{S:42} %{S:43} %{S:44} %{S:45} %{S:46} %{S:47} %{S:48} %{S:49} \
         %{S:50} %{S:51} %{S:52} %{S:53} %{S:54} %{S:55} %{S:56} %{S:57} %{S:58} %{S:59} \
         %{S:60} %{S:61} %{S:62} %{S:63} %{S:64} %{S:65} %{S:66} ; do
     unzip $l -d %{buildroot}%{_datadir}/%{oname}/levels -x Readme.txt
done
unzip %{S:67} -d %{buildroot}%{_datadir}/%{oname}/levels/Tutorials

7z x %{S:2} -o%{buildroot}%{_datadir}/%{oname}/levels

# Remove not needed files
find %{buildroot}%{_datadir}/%{oname}/levels -name '*.broken' -delete \
            -or -name '*.orig' -delete -or -name '*.old' -delete \
            -or -name '*.Thumbs.db' -delete -or -name '*.*~' -delete \
            -or -name '*.bak' -delete -or -name '*.swp' -delete

# Remove duplicate level, same than BD2K3, but not complete
rm -fr %{buildroot}%{_datadir}/%{oname}/levels/Contributions/Contributions_2004/rnd_rado_negundo_iii

%fdupes -s %{buildroot}%{_prefix}

%post
# Correct Permissions
chmod 0664 -R %{_datadir}/%{oname}/levels/Contributions

%files
%defattr(-,root,root,-)
%{_datadir}/%{oname}

%changelog
