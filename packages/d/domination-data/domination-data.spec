#
# spec file for package domination-data
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define oname   domination

Name:           %{oname}-data
Version:        20140921
Release:        0
Summary:        Data files for Domination
License:        GPL-3.0
Group:          Amusements/Games/StrategyGame
Url:            http://domination.sourceforge.net/getmaps.shtml
Source0:        http://domination.sourceforge.net/maps/solar.zip
Source1:        http://domination.sourceforge.net/maps/bigeurope.zip
Source2:        http://domination.sourceforge.net/maps/google.zip
Source3:        http://domination.sourceforge.net/maps/europass.zip
Source4:        http://domination.sourceforge.net/maps/europe.zip
Source5:        http://domination.sourceforge.net/maps/artic.zip
Source6:        http://domination.sourceforge.net/maps/sudamerica.zip
Source7:        http://domination.sourceforge.net/maps/MiddleEast-Qatar.zip
Source8:        http://domination.sourceforge.net/maps/kosova.zip
Source9:        http://domination.sourceforge.net/maps/Falkland-Islands.zip
Source10:       http://domination.sourceforge.net/maps/england.zip
Source11:       http://domination.sourceforge.net/maps/sw_baltic.zip
Source12:       http://domination.sourceforge.net/maps/spain.zip
Source13:       http://domination.sourceforge.net/maps/swiss.zip
Source14:       http://domination.sourceforge.net/maps/france.zip
Source15:       http://domination.sourceforge.net/maps/austria.zip
Source16:       http://domination.sourceforge.net/maps/austria-hungary.zip
Source17:       http://domination.sourceforge.net/maps/eire.zip
Source18:       http://domination.sourceforge.net/maps/haiti.zip
Source19:       http://domination.sourceforge.net/maps/brasil.zip
Source20:       http://domination.sourceforge.net/maps/benelux.zip
Source21:       http://domination.sourceforge.net/maps/canada.zip
Source22:       http://domination.sourceforge.net/maps/germany.zip
Source23:       http://domination.sourceforge.net/maps/northeurope.zip
Source24:       http://domination.sourceforge.net/maps/germany1871.zip
Source25:       http://domination.sourceforge.net/maps/Deutsches_Reich_1871.zip
Source26:       http://domination.sourceforge.net/maps/eesti.zip
Source27:       http://domination.sourceforge.net/maps/estonia.zip
Source28:       http://domination.sourceforge.net/maps/mexico.zip
Source29:       http://domination.sourceforge.net/maps/serbia.zip
Source30:       http://domination.sourceforge.net/maps/fletzmap.zip
Source31:       http://domination.sourceforge.net/maps/greece.zip
Source32:       http://domination.sourceforge.net/maps/North_of_Italy.zip
Source33:       http://domination.sourceforge.net/maps/bayern.zip
Source34:       http://domination.sourceforge.net/maps/berlin.zip
Source35:       http://domination.sourceforge.net/maps/navarra.zip
Source36:       http://domination.sourceforge.net/maps/Illes_Balears.zip
Source37:       http://domination.sourceforge.net/maps/calw.zip
Source38:       http://domination.sourceforge.net/maps/wuppertal.zip
Source39:       http://domination.sourceforge.net/maps/kerzell.zip
Source40:       http://domination.sourceforge.net/maps/ennepe-ruhr-kreis.zip
Source41:       http://domination.sourceforge.net/maps/cologne.zip
Source42:       http://domination.sourceforge.net/maps/saarland.zip
Source43:       http://domination.sourceforge.net/maps/andorra.zip
Source44:       http://domination.sourceforge.net/maps/catalunya.zip
Source45:       http://domination.sourceforge.net/maps/astadt.zip
Source46:       http://domination.sourceforge.net/maps/dortmund.zip
Source47:       http://domination.sourceforge.net/maps/rio_de_janeiro.zip
Source48:       http://domination.sourceforge.net/maps/caribbean.zip
Source49:       http://domination.sourceforge.net/maps/Nuremberg_Public_Transit.zip
Source50:       http://domination.sourceforge.net/maps/discworld.zip
Source51:       http://domination.sourceforge.net/maps/aztec.zip
Source52:       http://domination.sourceforge.net/maps/GTA_SAN_AN.zip
Source53:       http://domination.sourceforge.net/maps/middleearth.zip
Source54:       http://domination.sourceforge.net/maps/LOTR2.zip
Source55:       http://domination.sourceforge.net/maps/wow.zip
Source56:       http://domination.sourceforge.net/maps/randland.zip
Source57:       http://domination.sourceforge.net/maps/Riskopoly.zip
Source58:       http://domination.sourceforge.net/maps/SuperRiskopoly.zip
Source59:       http://domination.sourceforge.net/maps/trivia.zip
Source60:       http://domination.sourceforge.net/maps/chutes.zip
Source61:       http://domination.sourceforge.net/maps/sudoku.zip
Source62:       http://domination.sourceforge.net/maps/conquest.zip
Source63:       http://domination.sourceforge.net/maps/chrono_trigger.zip
Source64:       http://domination.sourceforge.net/maps/startrek.zip
Source65:       http://domination.sourceforge.net/maps/usa8.zip
Source66:       http://domination.sourceforge.net/maps/civilwar.zip
Source67:       http://domination.sourceforge.net/maps/usa.zip
Source68:       http://domination.sourceforge.net/maps/hawaii.zip
Source69:       http://domination.sourceforge.net/maps/ohio.zip
Source70:       http://domination.sourceforge.net/maps/nyc.zip
Source71:       http://domination.sourceforge.net/maps/zertina.zip
Source72:       http://domination.sourceforge.net/maps/fortress.zip
Source73:       http://domination.sourceforge.net/maps/estlandr.zip
Source74:       http://domination.sourceforge.net/maps/periodictable.zip
Source75:       http://domination.sourceforge.net/maps/sylsia.zip
Source76:       http://domination.sourceforge.net/maps/troisdorf.zip
Source77:       http://domination.sourceforge.net/maps/wolken.zip
Source78:       http://domination.sourceforge.net/maps/castle.zip
Source79:       http://domination.sourceforge.net/maps/naerr.zip
Source80:       http://domination.sourceforge.net/maps/cow.zip
Source81:       http://domination.sourceforge.net/maps/westfalenhalle.zip
Source82:       http://domination.sourceforge.net/maps/union.zip
Source83:       http://domination.sourceforge.net/maps/rub.zip
Source84:       http://domination.sourceforge.net/maps/gymnasium.zip
Source85:       http://domination.sourceforge.net/maps/simpsons_world.zip
Source86:       http://domination.sourceforge.net/maps/simpsons.zip
Source87:       http://domination.sourceforge.net/maps/germany2.zip
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  dos2unix
BuildRequires:  unzip
Requires:       %{oname}
BuildArch:      noarch

%description
Domination is a board game that is a bit like the well known game Risk.

Domination is a game that is a bit like the well known board game of Risk
or RisiKo. It has many game options and includes many maps.

Written in java it includes a map editor, a simple map format, multiplayer
network play, single player, hotseat, 5 user interfaces and many more features,
it works in all OSs that run java.

Data files (cards, maps and images) for Domination.

%prep
# Convert to unix line end
find -name "*.cards" -print0 -or -name "*.map" -print0 | xargs -0 dos2unix

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}/maps

for d in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} \
         %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} \
         %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28} %{S:29} \
         %{S:30} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36} %{S:37} %{S:38} %{S:39} \
         %{S:40} %{S:41} %{S:42} %{S:43} %{S:44} %{S:45} %{S:46} %{S:47} %{S:48} %{S:49} \
         %{S:50} %{S:51} %{S:52} %{S:53} %{S:54} %{S:55} %{S:56} %{S:57} %{S:58} %{S:59} \
         %{S:60} %{S:61} %{S:62} %{S:63} %{S:64} %{S:65} %{S:66} %{S:67} %{S:68} %{S:69} \
         %{S:70} %{S:71} %{S:72} %{S:73} %{S:74} %{S:75} %{S:76} %{S:77} %{S:78} %{S:79} \
         %{S:80} %{S:81} %{S:82} %{S:83} %{S:84} %{S:85} %{S:86} %{S:87} ; do
     unzip $d -d %{buildroot}%{_datadir}/%{oname}/maps
done
# Correct Permissions
chmod 0644 %{buildroot}%{_datadir}/%{oname}/maps/*

%if 0%{?suse_version}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%{_datadir}/%{oname}

%changelog
