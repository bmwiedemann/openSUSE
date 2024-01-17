#
# spec file for package avesta-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           avesta-fonts
Version:        20121212
Release:        0
Summary:        Avestan Unicode Fonts
# in sourceforge there is GPLv3, but there is OFL in TTF names
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/avestafonts/files/Avestamanus/
Source0:        http://downloads.sourceforge.net/project/avestafonts/Avestamanus/avestamanus.tar.bz2
Source1:        OFL.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The glyph outlines origin from Yasna 10 of the manuscript of Tehran University 
Library, nr. 11263. The scanned manuscript can be viewed under Ave976 on
wwww.avesta-archive.org.

%prep
%setup -q -n avestamanus

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.odt OFL.txt *.pdf README
%{_ttfontsdir}

%changelog
