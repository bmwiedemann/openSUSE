#
# spec file for package kye-data
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oname   kye

Name:           %{oname}-data
Version:        2015_07_08
Release:        0
Summary:        Data files for Kye
License:        ISC
Group:          Amusements/Games/Strategy/Turn Based
Url:            http://www.nuke.demon.co.uk/kye/
# These levels are from http://www.nuke.demon.co.uk/kye/levels/
Source0:        http://www.nuke.demon.co.uk/kye/levels/xmas.zip
Source1:        http://www.nuke.demon.co.uk/kye/levels/vvv1.zip
Source2:        http://www.nuke.demon.co.uk/kye/levels/vexkyelevels.zip
Source3:        http://www.nuke.demon.co.uk/kye/levels/Training.zip
Source4:        http://www.nuke.demon.co.uk/kye/levels/Beginner.zip
Source5:        http://www.nuke.demon.co.uk/kye/levels/RComb.zip
Source6:        http://www.nuke.demon.co.uk/kye/levels/2Fun4Me.zip
Source7:        http://www.nuke.demon.co.uk/kye/levels/hordes.zip
Source8:        http://www.nuke.demon.co.uk/kye/levels/crowds.zip
Source9:        http://www.nuke.demon.co.uk/kye/levels/Action2.zip
Source10:       http://www.nuke.demon.co.uk/kye/levels/jg.zip
Source11:       http://www.nuke.demon.co.uk/kye/levels/afebrile.zip
Source12:       http://www.nuke.demon.co.uk/kye/levels/alanskye.zip
Source13:       http://www.nuke.demon.co.uk/kye/levels/AntKye2.zip
Source14:       http://www.nuke.demon.co.uk/kye/levels/Danish.zip
Source15:       http://www.nuke.demon.co.uk/kye/levels/Garyskye.zip
Source16:       http://www.nuke.demon.co.uk/kye/levels/gsmick.zip
Source17:       http://www.nuke.demon.co.uk/kye/levels/InARush.zip
Source18:       http://www.nuke.demon.co.uk/kye/levels/nelsons.zip
Source19:       http://www.nuke.demon.co.uk/kye/levels/Newkye.zip
Source20:       http://www.nuke.demon.co.uk/kye/levels/philsel1.zip
Source21:       http://www.nuke.demon.co.uk/kye/levels/Ricardo.zip
Source22:       http://www.nuke.demon.co.uk/kye/levels/TPsKye.zip
Source23:       http://www.nuke.demon.co.uk/kye/levels/sampler.zip
# These levels are once downloaded from http://www.nuke.demon.co.uk/kye/levels
Source24:       vvv2.kye
Source25:       vvv3.kye
# These levels are from http://games.moria.org.uk/kye/
Source26:       http://games.moria.org.uk/kye/jungle.kye
Source27:       http://games.moria.org.uk/kye/maze.kye
Source28:       http://games.moria.org.uk/kye/problem.kye
Source29:       http://games.moria.org.uk/kye/system.kye
Source30:       http://games.moria.org.uk/kye/mystical.kye
# These levels are from http://www.oocities.org/timessquare/stadium/4790/kye.html
Source31:       http://www.oocities.org/timessquare/stadium/4790/kye1.zip
Source32:       http://www.oocities.org/timessquare/stadium/4790/kye2.zip
Source33:       http://www.oocities.org/timessquare/stadium/4790/kye3.zip
Source34:       http://www.oocities.org/timessquare/stadium/4790/kye4.zip
Source35:       http://www.oocities.org/timessquare/stadium/4790/kye5.zip
# Only what isn't in main levels, Fan Levels
Source36:       http://www.oocities.org/timessquare/stadium/4790/thomast.zip
Source37:       http://www.oocities.org/timessquare/stadium/4790/archie.zip
Source38:       http://www.oocities.org/timessquare/stadium/4790/orpheus.zip
Source39:       http://www.oocities.org/timessquare/stadium/4790/mohammed.zip
# Same Content than DAVIDH.KYE from RGB Classic Games
#               http://www.oocities.org/timessquare/stadium/4790/DLH.zip
Source40:       http://www.oocities.org/timessquare/stadium/4790/www.zip
Source41:       http://www.oocities.org/timessquare/stadium/4790/juicy.zip
Source42:       http://www.oocities.org/timessquare/stadium/4790/qed.zip
# Have same name than from RGB Classic Games
Source43:       Chris-levels.zip
Source44:       http://www.oocities.org/timessquare/stadium/4790/gilc1.zip
Source45:       http://www.oocities.org/timessquare/stadium/4790/moni.zip
Source46:       http://www.oocities.org/timessquare/stadium/4790/production.zip
Source47:       http://www.oocities.org/timessquare/stadium/4790/Hesperus.zip
Source48:       http://www.oocities.org/timessquare/stadium/4790/Crow.zip
Source49:       http://www.oocities.org/timessquare/stadium/4790/Crow2.zip
Source50:       http://www.oocities.org/timessquare/stadium/4790/crow3.zip
Source51:       http://www.oocities.org/timessquare/stadium/4790/bastard.zip
Source52:       http://www.oocities.org/timessquare/stadium/4790/second.zip
Source53:       http://www.oocities.org/timessquare/stadium/4790/maltus.zip
Source54:       http://www.oocities.org/timessquare/stadium/4790/kyeling.zip
Source55:       http://www.oocities.org/timessquare/stadium/4790/gauntlet.zip
Source56:       http://www.oocities.org/timessquare/stadium/4790/timer.zip
Source57:       http://www.oocities.org/timessquare/stadium/4790/fast.zip
# Not good works SourceUrl from http://kye.8m.com/gfclevels.html
Source58:       Brink.zip
Source59:       Yellow.zip
Source60:       Rw.zip
# RGB Classic Games
# Author Colin Garbutt generously released this game as freeware on 18 February 2008.
# It was a Charity Shareware - you had to donate to Save the Children in order to register and get a lot of more levels.
# Not good works SourceUrl from http://www.classicdosgames.com/game/Kye.html
Source61:       levels.zip
BuildRequires:  dos2unix
BuildRequires:  unzip
Requires:       %{oname}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a clone of the original Kye game for Windows, by Colin Garbutt.

Kye is a puzzle game with arcade game elements. The game takes place
in a small playing area, where the player controls Kye - a
distinctive green blob. The player moves around and tries to collect
all of the diamonds. However, there are many other objects in the
game, which can obstruct, trap or kill the Kye.

Kye is one of those games like Chess, where a small number of
different playing pieces, obeying simple rules, combine to create a
game of enormous variety and complexity.

Level for Kye.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}

for l in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} \
         %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} \
         %{S:20} %{S:21} %{S:22} %{S:23} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36} \
         %{S:37} %{S:38} %{S:39} %{S:40} %{S:41} %{S:42} %{S:43} %{S:44}  %{S:46} \
         %{S:47} %{S:48} %{S:49} %{S:50} %{S:51} %{S:52} %{S:53} %{S:54} %{S:55} %{S:56} \
         %{S:57} %{S:58} %{S:59} %{S:60} ; do
     unzip $l -d %{buildroot}%{_datadir}/%{oname}
done

for l in %{S:24} %{S:25} %{S:26} %{S:27} %{S:28} %{S:29} %{S:30} ; do
     cp -a $l %{buildroot}%{_datadir}/%{oname}
done

# Delete double Levels and correct what fdupes didn't find
unzip %{S:61} -d %{buildroot}%{_datadir}/%{oname} -x JUNGLE.KYE NEWKYE.KYE travis.KYE

# rename txt files
cd %{buildroot}%{_datadir}/%{oname}
mv readme.txt vex.txt
mv Readme.txt Training.txt
mv "newkye_ french_engl.rtf" Newkye_french_english.rtf
mv Readit.txt TPsKye.txt
mv levels.kye Chris-levels.kye

# Convert to unix line end, all Files have DOS '^M' characters and some have
# ^Z but are not binary file and because this must be used -f
find -name "*.*" -exec dos2unix -f "{}" "+"

%files
%defattr(-,root,root,-)
%attr(0644,root,root) %{_datadir}/%{oname}/*
%dir %{_datadir}/%{oname}

%changelog
