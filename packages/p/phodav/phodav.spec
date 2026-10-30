#
# spec file for package phodav
#
# Copyright (c) 2024 SUSE LLC
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


%define shlib libphodav-3_0-0
Name:           phodav
Version:        3.2
Release:        0
Summary:        A WebDAV server using libsoup
License:        LGPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://wiki.gnome.org/phodav
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  asciidoc
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.80
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.2.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%{?systemd_ordering}

%description
phodav is a WebDav server implementation using libsoup (RFC 4918).

%package -n %{shlib}
Summary:        A library for file sharing with WebDAV
Group:          System/Libraries
# Provides for the translations (-lang package)
Provides:       phodav-3.0 = %{version}

%description -n %{shlib}
phodav is a WebDav server implementation using libsoup (RFC 4918).

This package provides the shared library for %{name}.

%package -n typelib-1_0-Phodav-3_0
Summary:        A library for file sharing with WebDAV
Group:          System/Libraries

%description -n typelib-1_0-Phodav-3_0
phodav is a WebDav server implementation using libsoup (RFC 4918).

This package provides the shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       typelib-1_0-Phodav-3_0 = %{version}

%description devel
phodav is a WebDav server implementation using libsoup (RFC 4918).

This package provides the files needed for developing software using %{name}.

%package -n     chezdav
Summary:        A simple WebDAV server program
Group:          Productivity/Networking/File-Sharing

%description -n chezdav
The chezdav package contains a simple tool to share a directory
with WebDAV. The service is announced over mDNS for clients to discover.

%package -n     spice-webdavd
Summary:        Spice daemon for the DAV channel
Group:          Productivity/Networking/Other
%{?systemd_requires}

%description -n spice-webdavd
The spice-webdavd package contains a daemon to proxy WebDAV request to
the Spice virtio channel.

%lang_package -n phodav-3.0

%prep
%autosetup -p1
echo "%{version}" > .tarball-version

%build
%meson \
    -Dlitmus=disabled \
    %{nil}
%meson_build

%install
%meson_install
%find_lang phodav-3.0 --with-gnome

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%pre -n spice-webdavd
%service_add_pre spice-webdavd.service

%post -n spice-webdavd
%service_add_post spice-webdavd.service

%preun -n spice-webdavd
%service_del_preun spice-webdavd.service

%postun -n spice-webdavd
%service_del_postun spice-webdavd.service

%files -n phodav-3.0-lang -f phodav-3.0.lang

%files -n %{shlib}
%{_libdir}/libphodav-3.0.so.0*

%files -n typelib-1_0-Phodav-3_0
%{_libdir}/girepository-1.0/Phodav-3.0.typelib

%files devel
%license COPYING
%dir %{_includedir}/libphodav-3.0/
%{_includedir}/libphodav-3.0/*
%{_libdir}/libphodav-3.0.so
%{_libdir}/pkgconfig/libphodav-3.0.pc
%{_datadir}/doc/phodav-3.0/
%{_datadir}/gir-1.0/Phodav-3.0.gir

%files -n chezdav
%{_bindir}/chezdav
%{_mandir}/man1/chezdav.1%{?ext_man}

%files -n spice-webdavd
%license COPYING
%{_sbindir}/spice-webdavd
%{_udevrulesdir}/70-spice-webdavd.rules
%{_unitdir}/spice-webdavd.service
%{_sysusersdir}/spice-webdavd.conf

%changelog
