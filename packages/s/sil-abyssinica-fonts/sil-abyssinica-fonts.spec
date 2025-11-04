#
# spec file for package sil-abyssinica-fonts
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


Name:           sil-abyssinica-fonts
Version:        2.300
Release:        0
Summary:        Ethiopic script font designed in a calligraphic style
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/abyssinica/
Source0:        https://software.sil.org/downloads/r/abyssinica/AbyssinicaSIL-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       sil-abyssinica = %{version}
Provides:       locale(so)
Obsoletes:      sil-abyssinica < %{version}
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Abyssinica SIL is an Ethiopic font (often called Ge’ez)
based on calligraphic traditions. The Ethiopic script is
currently used for writing at least 50 of the languages of
Ethiopia and Eritrea of sub-Saharan Africa. The traditional
Ge’ez language, and script, continues to be used
liturgically in the northern part of the Horn of Africa.

%prep
%setup -q -T -c sil-abyssinica -n sil-abyssinica
unzip -x %{SOURCE0}
find -type f -print0 | xargs -0 chmod -x
find -name '*.txt' -print0 | xargs -0 dos2unix

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 AbyssinicaSIL-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc AbyssinicaSIL-%{version}/*.txt AbyssinicaSIL-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
