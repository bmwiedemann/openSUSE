#
# spec file for package mingzat-fonts
#
# Copyright (c) 2022 SUSE LLC
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


%define fontname Mingzat
Name:           mingzat-fonts
Version:        1.100
Release:        0
Summary:        Lepcha Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/mingzat/
Source0:        https://software.sil.org/downloads/r/mingzat/Mingzat-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Mingzat is a Unicode font based on Jason Glavy's JG Lepcha custom-encoded font.

%prep
%setup -q -n %{fontname}-%{version}

%build
dos2unix OFL*.txt README.txt FONTLOG.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%doc OFL*.txt documentation/*.pdf README.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
