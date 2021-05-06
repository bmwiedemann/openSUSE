#
# spec file for package opi
#
# Copyright (c) 2021 SUSE LLC
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


Name:           opi
Version:        2.0.0
Release:        0
Summary:        OBS Package Installer (CLI)
License:        GPL-3.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-termcolor
Requires:       sudo
Requires:       zypper
# rpm --import used curl but doesn't require it explicitly
Requires:       curl
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-termcolor
Requires:       zypper

%description
OBS Package Installer (CLI)

%prep
%setup -q

%build
help2man -s8 -N ./bin/opi > opi.8.gz
gzip opi.8.gz

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/metainfo
cp org.openSUSE.opi.appdata.xml %{buildroot}%{_datadir}/metainfo
mkdir -p %{buildroot}%{_datadir}/man/man8
cp opi.8.gz %{buildroot}%{_datadir}/man/man8

%check
python3 setup.py --version | grep %{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.openSUSE.opi.appdata.xml
%{_datadir}/man/man8/opi.8.gz
%{python3_sitelib}/*

%changelog
