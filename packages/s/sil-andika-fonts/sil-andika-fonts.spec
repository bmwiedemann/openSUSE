#
# spec file for package sil-andika-fonts
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           sil-andika-fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Summary:        Sans serif, Unicode-compliant Font For Literacy Use
Version:        7.000
Release:        0
URL:            https://software.sil.org/andika/
Source0:        https://software.sil.org/downloads/r/andika/Andika-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Andika is a sans serif, Unicode-compliant font designed
especially for literacy use, taking into account the needs of
beginning readers. The focus is on clear, easy-to-perceive
letterforms that will not be readily confused with one another.

A sans serif font is preferred by some literacy personnel for
teaching people to read. Its forms are simpler and less cluttered
than those of most serif fonts.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 Andika-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc Andika-%{version}/*.txt Andika-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
