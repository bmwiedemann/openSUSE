#
# spec file for package evdi
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


%define _dllibdir %{_libdir}/displaylink
%define lname   libevdi1
Name:           evdi
Release:        0
Version:        1.14.1
Summary:        Extensible Virtual Display Interface (EVDI) is a Linux Kernel Module
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Kernel
URL:            https://github.com/DisplayLink/evdi
Source0:        evdi-%{version}.tar
Source1:        evdi-kmp-preamble
Patch0:         evdi-Resolve-compiler-errors-when-compiling-against-Linux.patch
Patch1:         evdi-Enable-compilation-against-15.5.patch
Patch2:         evdi-Enable-compilation-against-15.6.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm)
# needssslcertforbuild
%kernel_module_package -p %{_sourcedir}/evdi-kmp-preamble -c %{_sourcedir}/_projectcert.crt

%description
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%package -n %{lname}
Summary:        LibEVDI Library
Group:          System/Libraries
Requires:       evdi-kmp

%description -n %{lname}
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%package devel
Summary:        Development files for libevdi Library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%prep
%setup -q
%patch0 -p1
%if 0%{?sle_version} == 150500
%patch1 -p1
%endif
%if 0%{?sle_version} == 150600
%patch2 -p1
%endif

%build
pushd library
%make_build
mv LICENSE LICENSE.library
popd

pushd module
sed -i 's:include/drm:/usr/src/linux/include/drm:' Makefile
sed -i 's:/kernel/drivers/gpu/drm/evdi:/extra:' Makefile
%make_build
mv LICENSE LICENSE.module

%install
pushd library
%make_install PREFIX=%{_prefix} LIBDIR=%{_dllibdir} CFLAGS="%{optflags}"
install -m644 -D evdi_lib.h %{buildroot}%{_includedir}/%{name}/evdi_lib.h
popd

pushd module
%make_install PREFIX=%{_prefix} LIBDIR=%{_dllibdir} CFLAGS="%{optflags}"

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license {library,module}/LICENSE.*
%doc README.md docs

%files -n %{lname}
%dir %{_dllibdir}
%{_dllibdir}/libevdi.so.1*

%files devel
%{_dllibdir}/libevdi.so
%{_includedir}/%{name}

%changelog
