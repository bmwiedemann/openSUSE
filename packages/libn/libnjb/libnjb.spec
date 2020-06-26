#
# spec file for package libnjb
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libnjb
Version:        2.2.7
Release:        0
Summary:        Nomad Jukebox API
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            http://libnjb.sourceforge.net
Source:         %{name}-%{version}.tar.gz
Patch0:         libnjb-no_m4_dir.diff
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  zlib-devel
Requires:       dbus-1

%description
Nomad Jukebox API

%package -n libnjb5
Summary:        Nomad Jukebox API
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description -n libnjb5
Nomad Jukebox API

%package devel
Summary:        Nomad Jukebox API
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       libusb-devel

%description devel
Nomad Jukebox API

%prep
%setup -q
%patch0

%build
autoreconf -fiv
%configure --program-prefix=njb- --disable-static --with-pic
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libnjb5 -p /sbin/ldconfig
%postun -n libnjb5 -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS FAQ README
%{_bindir}/njb-*

%files -n libnjb5
%{_libdir}/libnjb.so.*

%files devel
%{_libdir}/libnjb.so
%{_includedir}/libnjb.h
%{_libdir}/pkgconfig/libnjb.pc

%changelog
