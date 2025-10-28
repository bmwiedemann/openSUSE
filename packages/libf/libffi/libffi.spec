#
# spec file for package libffi
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%ifarch %ix86
%define _lto_cflags %{nil}
%endif
%define libffi_sover 8
Name:           libffi
Version:        3.5.2
Release:        0
Summary:        Foreign Function Interface Library
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://sourceware.org/libffi/
Source:         https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM - https://github.com/libffi/libffi/pull/943
Patch0:         943.patch
# for make check
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  makeinfo
BuildRequires:  pkgconfig

%description
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run
time.

%package devel
Summary:        Include files for development with libffi
Group:          Development/Languages/C and C++
Requires:       libffi%{libffi_sover} = %{version}

%description devel
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run
time.

%package -n libffi%{libffi_sover}
Summary:        Foreign Function Interface Library
Group:          System/Libraries

%description -n libffi%{libffi_sover}
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run
time.

%post -n libffi%{libffi_sover} -p /sbin/ldconfig
%postun -n libffi%{libffi_sover} -p /sbin/ldconfig

%prep
%autosetup -p1

%build
# https://github.com/libffi/libffi/pull/647
%configure --disable-exec-static-tramp
%make_build

%check
# do not disable "make check", FIX THE BUGS!
%make_build check

%install
%make_install
# do not package the static library
rm %{buildroot}%{_libdir}/libffi.a
rm %{buildroot}%{_libdir}/libffi.la

%files devel
%{_libdir}/libffi.so
%{_includedir}/ffi.h
%{_includedir}/ffitarget.h
%{_libdir}/pkgconfig/libffi.pc
%{_mandir}/man3/ffi.3%{?ext_man}
%{_mandir}/man3/ffi_call.3%{?ext_man}
%{_mandir}/man3/ffi_prep_cif.3%{?ext_man}
%{_mandir}/man3/ffi_prep_cif_var.3%{?ext_man}
%{_infodir}/libffi.info%{?ext_info}

%files -n libffi%{libffi_sover}
%license LICENSE
%{_libdir}/libffi.so.%{libffi_sover}*

%changelog
