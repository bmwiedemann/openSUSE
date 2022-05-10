#
# spec file for package nuosu-fonts
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


%define src_name NuosuSIL
Name:           nuosu-fonts
Version:        2.200
Release:        0
Summary:        SIL Yi Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/nuosu/
Source0:        https://software.sil.org/downloads/r/nuosu/%{src_name}-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Nuosu SIL Font is a single Unicode font for the standardized
Yi script used by a large ethnic group in southwestern China.

%prep
%setup -q -n %{src_name}-%{version}

%build
dos2unix *.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc README.txt FONTLOG.txt OFL-FAQ.txt
%{_ttfontsdir}

%changelog
