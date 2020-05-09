#
# spec file for package freerdp
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


# X264 and OPENH264 are disabled because openSUSE does not provide the codecs
# enable -DWITH_GSSAPI=ON again after #gh/FreeRDP/FreeRDP/4348 has been fixed
#global _with_gss 1
#
%define major_version 2
%define uwac_version 0
%define uwac_package %{uwac_version}-%{uwac_version}
%ifarch aarch64 %{arm}
%define _lto_cflags %{nil}
%endif
Name:           freerdp
Version:        2.1.0
Release:        0
Summary:        Remote Desktop Viewer Client
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://www.freerdp.com/
Source0:        https://github.com/FreeRDP/FreeRDP/archive/%{version}.tar.gz#/FreeRDP-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgsm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
Requires:       lib%{name}%{major_version} = %{version}-%{release}
%if 0%{?sle_version} >= 150000
BuildRequires:  pkgconfig(libavcodec)
%endif

%description
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the client
application.

%package wayland
Summary:        Remote Desktop Viewer Client
Group:          Productivity/Networking/Other

%description wayland
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the
wayland-based client application.

%package server
Summary:        Remote Desktop Server
Group:          Productivity/Networking/Other

%description server
This package contains a server-side implementation which can export a desktop
via the Remote Desktop Protocol (RDP) following the Microsoft Open
Specifications.

%package proxy
Summary:        Remote Desktop Security and Monitorig Proxy Server
Group:          Productivity/Networking/Other

%description proxy
This package contains a proxy that allows to select specific features and
channels allowed for all connections passing through.
It allows monitoring of the running sessions.

%package -n lib%{name}%{major_version}
Summary:        Remote Desktop Viewer client library
Group:          System/Libraries
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} = %{version}-%{release}

%description -n lib%{name}%{major_version}
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the client.

%package devel
Summary:        Development Files for freerdp
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{major_version} = %{version}-%{release}

%description devel
This package contains development files necessary for developing applications
based on libfreerdp.

%package -n     libwinpr%{major_version}
Summary:        Windows Portable Runtime
Group:          Productivity/Networking/Other

%description -n libwinpr%{major_version}
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n winpr%{major_version}-devel
Summary:        Windows Portable Runtime development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libwinpr%{major_version} = %{version}-%{release}
Obsoletes:      libwinpr2-devel < %{version}-%{release}
Provides:       libwinpr2-devel = %{version}-%{release}

%description -n winpr%{major_version}-devel
This package contains header files for developing applications that
use the winpr and winpr-tools libraries.

%package -n     libuwac%{uwac_package}
Summary:        Use wayland as a client
Group:          Productivity/Networking/Other

%description -n libuwac%{uwac_package}
Using wayland as a client (uwac) is a library to provide common
functionality for wayland clients.

%package -n uwac%{uwac_package}-devel
Summary:        Remote Desktop Toolkit libuwac development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libuwac%{uwac_package} = %{version}-%{release}
Obsoletes:      libuwac0-devel < %{version}-%{release}
Provides:       libuwac0-devel = %{version}-%{release}

%description -n uwac%{uwac_package}-devel
This package contains header files for developing applications that
use the uwac library.

%prep
%setup -q -n FreeRDP-%{version}
%autopatch -p1

%build
if [ -z "$SOURCE_DATE_EPOCH" ]; then
find . -type f -name "*.c" -exec perl -i -pe 's{__(DATE|TIME)__}{""}g' "{}" "+"
fi
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE -pie"

%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DWITH_SERVER=ON \
	-DWITH_PCSC=ON \
	-DWITH_CAIRO=ON \
	-DWITH_CUPS=ON \
	-DWITH_JPEG=ON \
	-DWITH_X264=OFF \
	-DWITH_OPENH264=OFF \
	-DWITH_GSM=ON \
	-DWITH_GSSAPI=%{?_with_gss:ON}%{?!_with_gss:OFF} \
	-DWITH_CHANNELS=ON \
	-DBUILTIN_CHANNELS=ON \
	-DCHANNEL_URBDRC=ON \
	-DCHANNEL_URBDRC_CLIENT=ON

make %{?_smp_mflags}

%install
cd build
%make_install
%fdupes %{buildroot}%{_libdir}/cmake/

%post   -n lib%{name}%{major_version} -p /sbin/ldconfig
%postun -n lib%{name}%{major_version} -p /sbin/ldconfig
%post -n libwinpr%{major_version} -p /sbin/ldconfig
%postun -n libwinpr%{major_version} -p /sbin/ldconfig
%post -n libuwac%{uwac_package} -p /sbin/ldconfig
%postun -n libuwac%{uwac_package} -p /sbin/ldconfig

%files
%{_bindir}/x%{name}
%{_mandir}/man1/x%{name}.1%{?ext_man}
%{_mandir}/man7/wlog.7%{?ext_man}

%files wayland
%{_bindir}/wl%{name}
%{_mandir}/man1/wl%{name}.1%{?ext_man}

%files server
%{_bindir}/%{name}-shadow-cli
%{_bindir}/winpr-hash
%{_bindir}/winpr-makecert
%{_mandir}/man1/%{name}-shadow-cli.1%{?ext_man}
%{_mandir}/man1/winpr-hash.1%{?ext_man}
%{_mandir}/man1/winpr-makecert.1%{?ext_man}

%files proxy
%{_bindir}/%{name}-proxy

%files -n lib%{name}%{major_version}
%license LICENSE
%{_libdir}/lib%{name}%{major_version}.so.*
%{_libdir}/lib%{name}-client%{major_version}.so.*
%{_libdir}/lib%{name}-shadow%{major_version}.so.*
%{_libdir}/lib%{name}-server%{major_version}.so.*
%{_libdir}/lib%{name}-shadow-subsystem%{major_version}.so.*

%files devel
%{_libdir}/cmake/FreeRDP%{major_version}
%{_libdir}/cmake/FreeRDP-Client%{major_version}
%{_libdir}/cmake/FreeRDP-Server%{major_version}
%{_libdir}/cmake/FreeRDP-Shadow%{major_version}
%{_includedir}/%{name}%{major_version}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-client%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-server%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-shadow%{major_version}.pc

%files -n libwinpr%{major_version}
%license LICENSE
%{_libdir}/libwinpr%{major_version}.so.*
%{_libdir}/libwinpr-tools%{major_version}.so.*

%files -n winpr%{major_version}-devel
%{_libdir}/cmake/WinPR%{major_version}
%{_includedir}/winpr%{major_version}
%{_libdir}/libwinpr%{major_version}.so
%{_libdir}/libwinpr-tools%{major_version}.so
%{_libdir}/pkgconfig/winpr%{major_version}.pc
%{_libdir}/pkgconfig/winpr-tools%{major_version}.pc

%files -n libuwac%{uwac_package}
%license LICENSE
%{_libdir}/libuwac%{uwac_version}.so.*

%files -n uwac%{uwac_package}-devel
%{_libdir}/cmake/uwac%{uwac_version}
%{_includedir}/uwac%{uwac_version}
%{_libdir}/libuwac%{uwac_version}.so
%{_libdir}/pkgconfig/uwac%{uwac_version}.pc

%changelog
