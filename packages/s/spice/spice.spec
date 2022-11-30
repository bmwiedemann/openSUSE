#
# spec file for package spice
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without lz4
%bcond_without libcard
%bcond_with celt051

%define libname libspice-server1
Name:           spice
Version:        0.15.1
Release:        0
Summary:        SPICE client and server library
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://www.spice-space.org/
Source:         https://www.spice-space.org/download/releases/spice-server/%{name}-%{version}.tar.bz2
Source1:        https://www.spice-space.org/download/releases/spice-server/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source99:       %{name}.rpmlintrc

BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-pyparsing
BuildRequires:  python3-six
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(orc-0.4)
BuildRequires:  pkgconfig(pixman-1) >= 0.17.7
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.14
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-libav
%if %{with celt051}
BuildRequires:  pkgconfig(celt051)
%endif
%if %{with libcard}
BuildRequires:  pkgconfig(libcacard)
%endif
%if %{with lz4}
BuildRequires:  pkgconfig(liblz4)
%endif

%description
The SPICE package provides the SPICE server library and client.
These components are used to provide access to a remote machine's
display and devices.

%package -n %{libname}
Summary:        Library for SPICE-server
Group:          System/Libraries
Obsoletes:      spice-client < %{version}-%{release}

%description -n %{libname}
Library for SPICE-server
The SPICE server is used to expose a remote machine's display
and devices.

%package -n libspice-server-devel
Summary:        Development files for building SPICE-server
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description -n libspice-server-devel
Development files for building SPICE-server.
The SPICE server is used to expose a remote machine's display
and devices.

%prep
%setup -q

%build
%configure \
        --disable-silent-rules \
        --disable-static \
        --disable-werror \
%if %{with libcard}
        --enable-smartcard \
%endif
%if %{with lz4}
        --enable-lz4 \
%endif
	--with-sasl=yes \
%if %{with celt051}
        --enable-celt051 \
%endif
        --enable-gstreamer
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README CHANGELOG.md
%license COPYING
%{_libdir}/libspice-server.so.*

%files -n libspice-server-devel
%{_libdir}/pkgconfig/spice-server.pc
%{_includedir}/spice-server/
%{_libdir}/libspice-server.so

%changelog
