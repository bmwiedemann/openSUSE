#
# spec file for package libimobiledevice-glue
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


%define libname libimobiledevice-glue-1_0-0
Name:           libimobiledevice-glue
Version:        0~git.20210925
Release:        0
Summary:        Native protocols library for iOS devices
License:        LGPL-2.1-or-later
URL:            https://www.libimobiledevice.org
Source:         %{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libplist-2.0) >= 2.2.0

%description
A library with common code used by libraries and tools around the libimobiledevice project.
It does not depend on any existing libraries from Apple.

%package -n %{libname}
Summary:        Native protocols library for iOS devices

%description -n %{libname}
A library with common code used by libraries and tools around the libimobiledevice project.
It does not depend on any existing libraries from Apple.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libplist-2.0)

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i -e '/Requires:/d' src/%{name}-1.0.pc.in
sed -i -e 's/-L${libdir}//' src/%{name}-1.0.pc.in

%build
autoreconf -fvi
%configure \
  --disable-silent-rules \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license COPYING
%{_libdir}/%{name}-1.0.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
