#
# spec file for package vlgothic-fonts
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


Name:           vlgothic-fonts
Version:        20220612
Release:        0
Summary:        VL-Gothic TrueType font family
License:        BSD-3-Clause AND mplus
Group:          System/X11/Fonts
URL:            http://dicey.org/vlgothic/
Source0:        https://en.osdn.net/dl/vlgothic/VLGothic-%{version}.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:  xz
Provides:       scalable-font-ja
Provides:       vlgothic = %{version}
Provides:       locale(ja)
Obsoletes:      vlgothic <= 20110722
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
This package provides "VLGothic" Japanese TrueType fonts which are
based on the M+ fonts and the Sazanami fonts.

%prep
%setup -q -n VLGothic

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
for i in *.ttf
do
    install -m 644 $i %{buildroot}%{_ttfontsdir}
done

%reconfigure_fonts_scriptlets -c

%files
%defattr(-,root,root)
%license LICENSE*
%doc README* Changelog*
%{_ttfontsdir}

%changelog
