#
# spec file for package phodav
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


%define shlib libphodav-2_0-0
Name:           phodav
Version:        2.3
Release:        0
Summary:        A WebDAV server using libsoup
License:        LGPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing 
URL:            https://wiki.gnome.org/phodav
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  asciidoc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%{?systemd_ordering}

%description
phodav is a WebDav server implementation using libsoup (RFC 4918).

%package -n %{shlib}
Summary:        A library for file sharing with WebDAV
Group:          System/Libraries

%description -n %{shlib}
phodav is a WebDav server implementation using libsoup (RFC 4918).

This package provides the shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

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

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang phodav-2.0 --with-gnome
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcspice-webdavd

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

%files -n %{shlib} -f %{name}-2.0.lang
%{_libdir}/libphodav-2.0.so.0*

%files devel
%license COPYING
%dir %{_includedir}/libphodav-2.0/
%{_includedir}/libphodav-2.0/*
%{_libdir}/libphodav-2.0.so
%{_libdir}/pkgconfig/libphodav-2.0.pc
%{_datadir}/gtk-doc/html/phodav-2.0/

%files -n chezdav
%{_bindir}/chezdav
%{_mandir}/man1/chezdav.1%{?ext_man}

%files -n spice-webdavd
%license COPYING
%{_sbindir}/spice-webdavd
%{_sbindir}/rcspice-webdavd
%{_libexecdir}/udev/rules.d/70-spice-webdavd.rules
%{_unitdir}/spice-webdavd.service

%changelog
