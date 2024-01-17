#
# spec file for package rocksndiamonds-data
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define oname   rocksndiamonds
Name:           %{oname}-data
Version:        20220526
Release:        0
Summary:        Data files for Rocks'n'Diamonds
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.artsoft.org/rocksndiamonds/
Source0:        https://www.artsoft.org/RELEASES/%{oname}/levels/ZeldaII-1.0.0.zip
Source1:        https://www.artsoft.org/RELEASES/%{oname}/levels/Zelda-1.0.0.zip
Source2:        https://www.artsoft.org/RELEASES/%{oname}/levels/Emerald_Mine_Club-3.1.3.7z
Source3:        https://www.artsoft.org/RELEASES/%{oname}/levels/Sokoban-1.0.0.zip
# Use supplied tarbal, fixed with fdupes -l sym -r -m .
# and packed than rockslevels, repacked as tar.bz2
Source4:        Contributions-1.2.0.tar.bz2
Source5:        https://www.artsoft.org/RELEASES/%{oname}/levels/Snake_Bite-1.0.0.zip
Source6:        https://www.artsoft.org/RELEASES/%{oname}/levels/BD2K3-1.0.0.zip
Source7:        https://www.artsoft.org/RELEASES/%{oname}/levels/Boulder_Dash_Dream-1.0.0.zip
Source8:        https://www.artsoft.org/RELEASES/%{oname}/levels/Supaplex-2.0.0.7z
Source9:        https://www.artsoft.org/RELEASES/unix/%{oname}/levels/rockslevels-dx-1.0.tar.gz
Source68:       https://www.artsoft.org/RELEASES/%{oname}/levels/Better_Together-1.0.0.7z
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
BuildRequires:  unzip
Requires:       %{oname}
BuildArch:      noarch
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150100
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif

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

tar -xjf %{SOURCE4} -C %{buildroot}%{_datadir}/%{oname}

for l in %{SOURCE9} %{SOURCE10} ; do
    tar xfvz $l -C %{buildroot}%{_datadir}/%{oname}
done

for l in %{SOURCE0} %{SOURCE1} %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
         %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} \
         %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
         %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE39} \
         %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} %{SOURCE45} %{SOURCE46} %{SOURCE47} %{SOURCE48} %{SOURCE49} \
         %{SOURCE50} %{SOURCE51} %{SOURCE52} %{SOURCE53} %{SOURCE54} %{SOURCE55} %{SOURCE56} %{SOURCE57} %{SOURCE58} %{SOURCE59} \
         %{SOURCE60} %{SOURCE61} %{SOURCE62} %{SOURCE63} %{SOURCE64} %{SOURCE65} %{SOURCE66} ; do
     unzip $l -d %{buildroot}%{_datadir}/%{oname}/levels -x Readme.txt
done
unzip %{SOURCE67} -d %{buildroot}%{_datadir}/%{oname}/levels/Tutorials

for l in %{SOURCE2} %{SOURCE8} %{SOURCE68} ; do
    7z x $l -o%{buildroot}%{_datadir}/%{oname}/levels
done

# Remove not needed files
find %{buildroot}%{_datadir}/%{oname}/levels -name '*.broken' -delete \
            -or -name '*.orig' -delete -or -name '*.old' -delete \
            -or -name '*.Thumbs.db' -delete -or -name '*.*~' -delete \
            -or -name '*.bak' -delete -or -name '*.swp' -delete

# Remove duplicate level, same than BD2K3, but not complete
rm -fr %{buildroot}%{_datadir}/%{oname}/levels/Contributions/Contributions_2004/rnd_rado_negundo_iii

%fdupes -s %{buildroot}%{_datadir}

%post
# Correct Permissions
chmod 0664 -R %{_datadir}/%{oname}/levels/Contributions
chmod 0664 -R %{_datadir}/%{oname}/levels/Supaplex

%files
%{_datadir}/%{oname}

%changelog
