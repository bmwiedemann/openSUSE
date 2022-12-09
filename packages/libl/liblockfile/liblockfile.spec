#
# spec file for package liblockfile
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%global sover   1
%global libname liblockfile%{sover}
Name:           liblockfile
Version:        1.17
Release:        0
Summary:        Library with NFS-safe locking functions
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/miquels/liblockfile
Source:         https://github.com/miquels/liblockfile/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
This library implements a number of functions found in -lmail on SysV
systems. These functions are designed to lock the standard mailboxes in
%{_localstatedir}/mail (or wherever the system puts them).

%package -n %{libname}
Summary:        Library with NFS-safe locking functions
Group:          System/Libraries

%description -n %{libname}
This library implements a number of functions found in -lmail on SysV
systems. These functions are designed to lock the standard mailboxes in
%{_localstatedir}/mail (or wherever the system puts them).

In addition, this library offers a number of functions to create,
manage and remove generic lockfiles.

%package -n lockfile
Summary:        Support and cli utilities based on liblockfile
Group:          System/Tools

%description -n lockfile
This package contains support binaries for the liblockfile library,
and the command-line utility "dotlockfile".

%package devel
Summary:        Development files for liblockfile
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This library implements a number of functions found in -lmail on SysV
systems. These functions are designed to lock the standard mailboxes in
%{_localstatedir}/mail (or wherever the system puts them).

This subpackage contains libraries and header files for developing
applications that want to make use of liblockfile.

%prep
%autosetup -p1
sed -i 's/-g root//' Makefile.in

%build
%configure \
    --enable-shared \
    --prefix=%{buildroot} \
    --bindir=%{buildroot}%{_bindir} \
    --mandir=%{buildroot}%{_mandir} \
    --libdir=%{buildroot}%{_libdir} \
    --includedir=%{buildroot}%{_includedir}
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/liblockfile.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
%make_build test

%files -n lockfile
%license COPYRIGHT licenses/*
%doc Changelog README
%{_bindir}/dotlockfile
%{_mandir}/man1/dotlockfile.1%{?ext_man}

%files -n %{libname}
%{_libdir}/liblockfile.so.%{sover}*

%files devel
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_libdir}/liblockfile.so
%{_mandir}/man3/lockfile_create.3%{?ext_man}
%{_mandir}/man3/maillock.3%{?ext_man}

%changelog
