#
# spec file for package dai-banna-fonts
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


%define fontname DaiBanna
Name:           dai-banna-fonts
Version:        4.000
Release:        0
Summary:        SIL New Tai Lue Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/daibanna/
Source0:        https://software.sil.org/downloads/r/daibanna/DaiBannaSIL-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Dai Banna SIL is a Unicode font package for rendering New Tai Lue
(Xishuangbanna Dai) characters.

%prep
%autosetup -n %{fontname}SIL-%{version}

%build
dos2unix *.txt
chmod a-x *.txt documentation/pdf/*.pdf

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license OFL*.txt
%doc documentation/pdf/*.pdf README.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
