#
# spec file for package namdhinggo-fonts
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           namdhinggo-fonts
Version:        3.100
Release:        0
Summary:        SIL Limbu Font
License:        OFL-1.1
URL:            https://software.sil.org/namdhinggo/
Source0:        https://software.sil.org/downloads/r/namdhinggo/Namdhinggo-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Namdhinggo is a Unicode Limbu font for this elegant writing system of Nepal.
It provides glyphs for the full range of Limbu characters (U+1900..U+194F)
as well as basic Latin.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 Namdhinggo-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc Namdhinggo-%{version}/*.txt  Namdhinggo-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
