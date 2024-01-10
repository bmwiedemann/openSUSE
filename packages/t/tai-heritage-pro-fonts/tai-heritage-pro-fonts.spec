#
# spec file for package tai-heritage-pro-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           tai-heritage-pro-fonts
Version:        2.600
Release:        0
Summary:        Tai Viet Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/taiheritage/
Source0:        https://software.sil.org/downloads/r/taiheritage/TaiHeritagePro-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Tai Heritage Pro font is a Unicode-encoded font designed to reflect the
traditional hand-written style of the Tai Viet script, which is used by the
Tai Dam, Tai Daeng and Tai Don people who live in northwestern Vietnam and
surrounding areas.

%prep
%setup -q -n TaiHeritagePro-%{version}

%build
dos2unix OFL*.txt FONTLOG.txt README.txt documentation/DOCUMENTATION.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%doc OFL*.txt FONTLOG.txt README.txt documentation
%{_ttfontsdir}

%changelog
