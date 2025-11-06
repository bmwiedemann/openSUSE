#
# spec file for package sil-padauk-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           sil-padauk-fonts
Version:        6.000
Release:        0
Summary:        A font that supports the many diverse languages that use the Myanmar script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/padauk/
Source0:        https://software.sil.org/downloads/r/padauk/Padauk-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       locale(my)
Obsoletes:      sil-padauk < %{version}
Provides:       sil-padauk = %{version}
BuildArch:      noarch

%description
Padauk is a Unicode Myanmar font family with broad support for
writing systems that use the Myanmar script. This script is an
abugida, a writing system in which each consonant has an inherent
vowel.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 Padauk-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc Padauk-%{version}/*.txt Padauk-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
