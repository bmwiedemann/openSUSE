#
# spec file for package gmp
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


Name:           gmp
Version:        6.1.2
Release:        0
Summary:        The GNU MP Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries
Url:            https://gmplib.org/
Source0:        https://gmplib.org/download/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gmplib.org/download/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         gmp-noexec.diff
Patch1:         gmp-6.1.2-conftest.patch
Patch2:         floating-point-format-no-lto.patch
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for calculating huge numbers (integer and floating point).

%package -n libgmp10
Summary:        Shared library for the GNU MP Library
Group:          System/Libraries

%description -n libgmp10
A library for calculating huge numbers (integer and floating point).

%package -n libgmpxx4
Summary:        C++ bindings for the GNU MP Library
Group:          System/Libraries
Requires:       libgmp10 >= %{version}

%description -n libgmpxx4
A library for calculating huge numbers (integer and floating point).

This package contains C++ bindings
C++ bindings for the GNU MP Library.

%package devel
Summary:        Include Files and Libraries for Development with the GNU MP Library
Group:          Development/Languages/C and C++
Requires:       libgmp10 = %{version}
Requires:       libgmpxx4 = %{version}
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
These libraries are needed to develop programs which calculate with
huge numbers (integer and floating point).

%prep
%setup -q
%patch0
%patch1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fexceptions"
%configure \
  --enable-cxx \
  --enable-fat
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make %{?_smp_mflags} check

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/libgmp.la
rm %{buildroot}%{_libdir}/libgmpxx.la
rm %{buildroot}%{_libdir}/libgmpxx.a

%post -n libgmp10 -p /sbin/ldconfig
%post -n libgmpxx4 -p /sbin/ldconfig

%postun -n libgmp10 -p /sbin/ldconfig
%postun -n libgmpxx4 -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files -n libgmp10
%defattr(-,root,root)
%license COPYING*
%{_libdir}/libgmp.so.10*

%files -n libgmpxx4
%defattr(-,root,root)
%{_libdir}/libgmpxx.so.4*

%files devel
%defattr(-,root,root)
%doc AUTHORS README NEWS
%doc demos
%{_infodir}/gmp.info*%{ext_info}
%{_libdir}/libgmp.a
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_includedir}/gmp.h
%{_includedir}/gmpxx.h

%changelog
