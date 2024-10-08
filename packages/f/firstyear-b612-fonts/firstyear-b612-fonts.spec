#
# spec file for package bitstream-vera-fonts
#
# Copyright (c) 2024 SUSE LLC
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


%define fontname     B612
Name:           firstyear-b612-fonts
Version:        4.20.69
Release:        0
Summary:        Aeronautical fonts designed for cockpits
License:        OFL-1.1 AND EPL-2.0 AND BSD-3-Clause
Group:          System/X11/Fonts
URL:            https://github.com/Firstyear/b612
Source:         https://github.com/Firstyear/b612/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
B612 is a legible font family designed and tested to be used on aircraft
cockpit screens.

This contains the B612 font family with patches from SUSE's
William Brown adjusting some characters for better readability.


%prep
%autosetup -p1 -n b612-%{version}

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m0644 fonts/ttf/*.ttf %{buildroot}/%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%license OFL.txt
%license EPL-2.0.html
%license edl-v10.html
%doc README.md
%{_ttfontsdir}

%changelog
