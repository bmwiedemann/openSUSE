#
# spec file for package swift-im
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


%define _name swift
%if 0%{?sle_version} == 120300 || 0%{?sle_version} == 120200
%define _flags V=1 swiften_dll=1 test=none optimize=1 debug=0 cc=gcc-6 cxx=g++-6 cxxflags='%{optflags}'
%else
%define _flags V=1 swiften_dll=1 test=none optimize=1 debug=0 cxxflags='%{optflags}'
%endif
Name:           swift-im
Version:        4.0.2
Release:        0
Summary:        XMPP client
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://swift.im/
Source0:        http://swift.im/downloads/releases/%{_name}-%{version}/%{_name}-%{version}.tar.gz
Source1:        http://swift.im/downloads/releases/%{_name}-%{version}/%{_name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         swift-4.0-qt5.11-includes.patch
Patch1:         swift-im-boost-tribool.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-Qt-5.15.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Avoid-deprecated-boost-endianess-include.patch
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  lua53
BuildRequires:  pkgconfig
BuildRequires:  python2-base
BuildRequires:  python2-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} == 120300 || 0%{?sle_version} == 120200
BuildRequires:  -gcc
BuildRequires:  -gcc-c++
BuildRequires:  gcc6
BuildRequires:  gcc6-c++
%endif

%description
Swift is a Jabber/XMPP instant messaging chat application.

# -------------------------------- swiften ---------------------------

%package -n libSwiften4
Summary:        XMPP client/server library
Group:          System/Libraries

%description -n libSwiften4
Swiften is a C++ library for implementing XMPP applications.

# ------------------------------ swiften-devel -----------------------

%package -n swiften-devel
Summary:        Development files for the Swiften XMPP client/server library
Group:          Development/Libraries/C and C++
Requires:       libSwiften4 = %{version}

%description -n swiften-devel
Swiften is a C++ library for implementing XMPP applications.

%prep
%autosetup -p1 -n swift-%{version}

# Remove 3rd party libraries
# Following ones are used from distro:
find 3rdParty/Boost/src -delete
find 3rdParty/Expat/src -delete
find 3rdParty/LibIDN -delete
find 3rdParty/Lua -delete
find 3rdParty/ZLib -delete
find 3rdParty/OpenSSL -delete
find 3rdParty/DocBook -delete
# P2P
find 3rdParty/LibMiniUPnPc -delete
find 3rdParty/LibNATPMP -delete
# DNS (they use it on Android)
find 3rdParty/Unbound -delete
find 3rdParty/Ldns -delete
# Only for developers
find 3rdParty/LCov -delete
# Not used by swift yet
find 3rdParty/Breakpad/src -delete
find 3rdParty/SQLite -delete
# They use scons in a way that doesnt allow us to use our CppUnit
# find 3rdParty/CppUnit -delete
# Needed for tests
# find 3rdParty/HippoMocks -delete

%build
./scons %{_flags} Swift Swiften %{?_smp_mflags} boost_bundled_enable=false

%install
./scons %{_flags} \
    SWIFT_INSTALLDIR=%{buildroot}%{_prefix} \
    SWIFTEN_INSTALLDIR=%{buildroot}%{_prefix} \
    SWIFTEN_LIBDIR=%{buildroot}%{_libdir} \
    %{buildroot}%{_prefix}

%fdupes %{buildroot}%{_prefix}
%suse_update_desktop_file -r %{_name} Network InstantMessaging

%post -n libSwiften4 -p /sbin/ldconfig
%postun -n libSwiften4 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/%{_name}-im
%{_bindir}/%{_name}-open-uri
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.xpm
%{_datadir}/icons/hicolor/*/apps/%{_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{_name}.xpm
%{_datadir}/icons/hicolor/scalable/apps/%{_name}.svg
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/sounds
%{_datadir}/%{_name}/sounds/message-received.wav
%dir %{_datadir}/%{_name}/translations
%{_datadir}/%{_name}/translations/swift_*.qm

%files -n libSwiften4
%{_libdir}/libSwiften.so.*

%files -n swiften-devel
%{_bindir}/swiften-config
%{_includedir}/Swiften
%{_libdir}/libSwiften.so

%changelog
