#
# spec file for package gdouros-unidings-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gdouros-unidings-fonts
Version:        9.17
Release:        0
Summary:        Font with Basic Icon Glyphs
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download URL
# http://users.teilar.gr/~g1951d/Unidings.zip
Source0:        Unidings-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       unidings-fonts = %{version}
Obsoletes:      unidings-fonts < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Unidings contains glyphs that may be used in a Last Resort font, as well as
icon glyphs for control and special characters, encoded in F200..F3B4 and
F400..F5B4 of the Private Use Area in BMP. Block names are from “Roadmaps,
a snapshot as of 2011-05-30”, http://std.dkuug.dk/JTC1/SC2/WG2/docs/n4056.htm

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
install -m 0644 %{SOURCE1} .

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Unidings.pdf
%{_ttfontsdir}

%changelog
