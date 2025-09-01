#
# spec file for package sil-busra-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           sil-busra-fonts
Version:        9.000
Release:        0
Summary:        A font family for the Khmer script
License:        OFL-1.1
URL:            https://software.sil.org/busra/
Source0:        https://software.sil.org/downloads/r/busra/Busra-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Busra font family is the latest version of the popular
Khmer Busra font first released as part of the Mondulkiri
project. This Khmer font has been improved and updated for
a wide range of uses, from print to web, and to support the
latest Khmer text encoding best practices.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 Busra-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc Busra-%{version}/*.txt Busra-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
