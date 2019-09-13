#
# spec file for package alee-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           alee-fonts
Version:        13
Release:        0
Summary:        Korean TrueType fonts
License:        Artistic-1.0+
Group:          System/X11/Fonts
Url:            http://packages.debian.org/unstable/source/ttf-alee
Source0:        http://ftp.debian.org/debian/pool/main/t/ttf-alee/ttf-alee_%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-ko
Provides:       ttf-alee = %{version}
Provides:       locale(ko)
Obsoletes:      ttf-alee <= 12
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Korean TrueType fonts by A Lee.

%prep
%setup -q -n ttf-alee-%{version}

%build
chmod 644 debian/rules

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc COPYING
%doc debian
%{_ttfontsdir}

%changelog
