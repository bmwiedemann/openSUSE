#
# spec file for package sil-doulos-fonts
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


Name:           sil-doulos-fonts
# Provides:       locale(vi)
Version:        7.000
Release:        0
Summary:        A font that provides complete support for the International Phonetic Alphabet
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/doulos
Source0:        https://software.sil.org/downloads/r/doulos/DoulosSIL-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      sil-doulos < %{version}
Provides:       sil-doulos = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Doulos SIL is a Unicode-based font family that supports the wide
range of languages that use the Latin and Cyrillic scripts, whether
used for phonetic or orthographic needs. Linguists appreciate the
wide range of characters and symbols useful in their work.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 DoulosSIL-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license DoulosSIL-%{version}/OFL*.txt
%doc DoulosSIL-%{version}/README.txt DoulosSIL-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
