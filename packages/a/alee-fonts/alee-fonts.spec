#
# spec file for package alee-fonts
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


Name:           alee-fonts
Version:        13.3
Release:        0
Summary:        Korean TrueType fonts
License:        Artistic-1.0+
Group:          System/X11/Fonts
URL:            https://packages.debian.org/unstable/source/ttf-alee
Source0:        http://deb.debian.org/debian/pool/main/f/fonts-alee/fonts-alee_%{version}.tar.xz
BuildRequires:  fontpackages-devel
Provides:       scalable-font-ko
Provides:       ttf-alee = %{version}
Provides:       locale(ko)
Obsoletes:      ttf-alee <= 12
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Korean TrueType fonts by A Lee.

%prep
%setup -q -n fonts-alee-%{version}

%build
chmod 644 debian/rules

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -c

%files
%license COPYING
%doc debian
%{_ttfontsdir}

%changelog
