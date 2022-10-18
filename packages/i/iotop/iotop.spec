#
# spec file for package iotop
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


%define gitdate 20220308
%define gitversion HEAD-a14256a

Name:           iotop
Version:        0.6git.%{gitdate}
Release:        0
Summary:        Top Like UI to Show Per-Process I/O Going on
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://guichaz.free.fr/iotop/
Source0:        https://repo.or.cz/iotop.git/snapshot/HEAD.tar.gz#/%{name}-%{gitversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-curses

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command).

Iotop is a Python program with a UI similar to top to show on behalf of
which process is the I/O going on.

%prep
%autosetup -p1 -n %{name}-%{gitversion}

%build
%python3_build

%install
%python3_install

%fdupes -s %{buildroot}

%files
%license COPYING
%doc README NEWS THANKS
%{_sbindir}/iotop
%{_mandir}/man8/iotop.8%{?ext_man}
%{python3_sitearch}/*

%changelog
