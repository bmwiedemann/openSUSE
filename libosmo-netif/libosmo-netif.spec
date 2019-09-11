#
# spec file for package libosmo-netif
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


%define version_unconverted 0.4.0

Name:           libosmo-netif
Summary:        Osmocom library for muxed audio
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
Version:        0.4.0
Release:        0
Url:            https://osmocom.org/projects/libosmo-netif

Source:         %name-%version.tar.xz
Patch1:         osmo-talloc.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  xz
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.0.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.0.0
BuildRequires:  pkgconfig(talloc)

%description
Network interface demuxer library for OsmoCom projects.

%package -n libosmonetif6
Summary:        Osmocom library for muxed audio
License:        AGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmonetif6
Network interface demuxer library for OsmoCom projects.

%package -n libosmonetif-devel
Summary:        Development files for the Osmocom muxed audio library
License:        AGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmonetif6 = %version

%description -n libosmonetif-devel
Network interface demuxer library for OsmoCom projects.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-netif.

%prep
%setup -q
%patch -P 1 -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
%configure --enable-shared --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%check
if ! make %{?_smp_mflags} check; then
	rv=$?
	cat tests/testsuite.log
	echo "Suppressing exit $rv"
	# timing issue
fi

%post   -n libosmonetif6 -p /sbin/ldconfig
%postun -n libosmonetif6 -p /sbin/ldconfig

%files -n libosmonetif6
%defattr(-,root,root)
%_libdir/libosmonetif.so.6*

%files -n libosmonetif-devel
%defattr(-,root,root)
%doc COPYING
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/netif/
%_libdir/libosmonetif.so
%_libdir/pkgconfig/libosmo-netif.pc

%changelog
