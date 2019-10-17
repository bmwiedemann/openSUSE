#
# spec file for package libffi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libffi_sover 7

Name:           libffi
Version:        3.2.1.git505
Release:        0
Summary:        Foreign Function Interface Library
License:        MIT
Group:          Development/Languages/C and C++
Url:            https://github.com/libffi/
Source:         %name-%version.tar.xz
Source99:       baselibs.conf
Patch1:         gccbug.patch
Patch2:         stdcall.patch
# Workaround from https://github.com/libffi/libffi/issues/498
Patch3:         aarch64.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkg-config
# for make check
BuildRequires:  dejagnu
BuildRequires:  expect

%description
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run
time.


%package devel
Summary:        Include files for development with libffi
Group:          Development/Languages/C and C++
Requires:       libffi%{libffi_sover} = %{version}
PreReq:         %{install_info_prereq}

%description devel
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run
time.

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/libffi.info.gz

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libffi.info.gz

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
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install
# do not package the static library
rm %{buildroot}%{_libdir}/libffi.a
rm %{buildroot}%{_libdir}/libffi.la

%files devel
%defattr(-,root,root)
%{_libdir}/libffi.so
%{_prefix}/include/ffi.h
%{_prefix}/include/ffitarget.h
%{_libdir}/pkgconfig/libffi.pc
%doc %{_mandir}/man3/ffi.3.gz
%doc %{_mandir}/man3/ffi_call.3.gz
%doc %{_mandir}/man3/ffi_prep_cif.3.gz
%doc %{_mandir}/man3/ffi_prep_cif_var.3.gz
%doc %{_infodir}/libffi.info.gz

%files -n libffi%{libffi_sover}
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libffi.so.%{libffi_sover}*

%changelog
