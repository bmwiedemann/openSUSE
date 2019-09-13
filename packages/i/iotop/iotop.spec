#
# spec file for package iotop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           iotop
Version:        0.6
Release:        0
Summary:        Top Like UI to Show Per-Process I/O Going on
License:        GPL-2.0-only
Group:          System/Monitoring
Url:            http://guichaz.free.fr/iotop/
Source0:        http://guichaz.free.fr/iotop/files/iotop-%{version}.tar.bz2
Source1:        http://guichaz.free.fr/iotop/files/iotop-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch0:         iotop-0.6-python3_build.patch
Patch1:         iotop-0.6-python3-header.patch
Patch2:         iotop-0.6-noendcurses.patch
Patch3:         iotop-0.60-fix-proc-status-split.patch
Patch4:         iotop-0.6-ignore-invalid-lines-in-proc-status.patch
BuildRequires:  fdupes
BuildRequires:  python3-devel
Requires:       python3-curses
BuildArch:      noarch

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command).

Iotop is a Python program with a UI similar to top to show on behalf of
which process is the I/O going on.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --optimize=2 --root=%{buildroot}
%fdupes -s %{buildroot}

%files
%license COPYING
%doc NEWS THANKS
%{_sbindir}/iotop
%{_mandir}/man8/iotop.8%{ext_man}
%{python_sitelib}/*

%changelog
