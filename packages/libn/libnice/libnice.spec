#
# spec file for package libnice
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


Name:           libnice
Version:        0.1.14
Release:        0
Summary:        Interactive Connectivity Establishment implementation
License:        MPL-1.1 OR LGPL-2.1-only
Group:          System/Libraries
URL:            http://nice.freedesktop.org/
Source:         http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  libgupnp-igd-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.91
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.91

%description
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package -n libnice10
Summary:        Interactive Connectivity Establishment implementation
Group:          System/Libraries

%description -n libnice10
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package -n gstreamer-libnice
Summary:        Interactive Connectivity Establishment implementation - GStreamer 1.0
Group:          System/Libraries
Supplements:    packageand(libnice10:gstreamer)

%description -n gstreamer-libnice
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE)

%package devel
Summary:        Interactive Connectivity Establishment implementation - development files
Group:          Development/Libraries/C and C++
Requires:       libnice10 = %{version}
Provides:       libnice-doc = %{version}
Obsoletes:      libnice-doc < %{version}

%description devel
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# We don't ship the examples...
rm %{buildroot}%{_bindir}/*-example

%check
# make check disabled - Since version 0.1.3, libnice tries to interact with NM during make check
#make check \
#%if 0%{?qemu_user_space_build}
#|| echo "ignore test suite failure in qemu, it is not threadsafe"
#%endif

%post   -n libnice10 -p /sbin/ldconfig
%postun -n libnice10 -p /sbin/ldconfig

%files
%{_bindir}/stunbdc
%{_bindir}/stund

%files -n libnice10
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/nice/
%{_includedir}/stun/
%{_datadir}/gtk-doc/html/libnice/

%files -n gstreamer-libnice
%{_libdir}/gstreamer-1.0/libgstnice.so

%changelog
