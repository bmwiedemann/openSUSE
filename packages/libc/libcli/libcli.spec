#
# spec file for package libcli
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


%define	sover	1_10
%define libname %{name}%{sover}
Name:           libcli
Version:        1.10.7+git.20211009
Release:        0
Summary:        Cisco-like telnet command-line library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/dparrish/libcli
Source:         %{name}-%{version}.tar.xz
Patch0:         libcli-Makefile-lib64.diff
Patch1:         libcli-fix-calloc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%package -n %{libname}
Summary:        Cisco-like telnet command-line library
Group:          System/Libraries

%description -n %{libname}
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%package devel
Summary:        Cisco-like telnet command-line library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}"

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} install
rm %{buildroot}%{_libdir}/libcli.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-, root, root)
%doc README.md
%license COPYING
%{_libdir}/libcli.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libcli.so
%{_includedir}/libcli.h

%changelog
