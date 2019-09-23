#
# spec file for package unifraktur-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           unifraktur-fonts
Version:        0.20170319
Release:        0
Summary:        Fonts from the UniFraktur project
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://unifraktur.sf.net/

Source:         http://downloads.sf.net/unifraktur/UnifrakturMaguntia.2017-03-19.zip
Source2:        http://downloads.sf.net/unifraktur/UnifrakturCook.2013-08-25.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Unifraktur provides a number of Fraktur blackletter font faces that
are optimized for @font-face embedding with CSS.

UnifrakturMaguntia is a weight-400 font baſed on Peter Wiegel’s font
"Berthold Mainzer Fraktur".

UnifrakturCook is a weight-700 font baſed on Peter Wiegel’s "Koch
Fette Deutſche Schrift". UnifrakturCook uſes the wideſt poſſible
range of modern ſmart font technologies for diſplaying the font’s
ligatures, OpenType, Apple Advanced Typography (AAT) and SIL
Graphite.

%prep
%setup -Tcqa0 -a2

%build
find . -type f -exec chmod a-x "{}" "+"

%install
c="%buildroot/%_ttfontsdir"
mkdir -p "$c"
cp -av Unifraktur*/*.ttf "$c/"

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/*.ttf
%doc UnifrakturMaguntia.2017-03-19/OFL.txt
%doc UnifrakturMaguntia.2017-03-19/OFL-FAQ.txt
%doc UnifrakturMaguntia.2017-03-19/FontLog.txt
%doc UnifrakturMaguntia.2017-03-19/Dokumentation_de_antiqua.pdf
%doc UnifrakturMaguntia.2017-03-19/Dokumentation_de_fraktur.pdf
%doc UnifrakturMaguntia.2017-03-19/Dokumentation_en_antiqua.pdf
%doc UnifrakturMaguntia.2017-03-19/Dokumentation_en_fraktur.pdf

%changelog
