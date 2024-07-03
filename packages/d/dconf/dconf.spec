#
# spec file for package dconf
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


Name:           dconf
Version:        0.40.0
Release:        0
Summary:        Key-based configuration system
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://live.gnome.org/dconf
Source0:        https://download.gnome.org/sources/dconf/0.40/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-gvdb-Restore-permissions-on-changed-files.patch bsc#971074 bgo#758066 bsc#1203344 fezhang@suse.com -- Restore permissions on files changed by dconf update.
Patch0:         0001-gvdb-Restore-permissions-on-changed-files.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.18.0
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# dconf provides a dbus service, but has no dependency on dbus in any way
# (because it uses gdbus), so we need an explicit Requires
Requires:       dbus-1

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

%package -n libdconf1
Summary:        Key-based configuration system
# The library doesn't really work if the dconf service is not reachable, so we
# need a Requires
Group:          System/Libraries
Requires:       %{name} >= %{version}
# libdconf-dbus-1-0 is no longer supported with dconf 0.25.x+
Obsoletes:      libdconf-dbus-1-0 < %{version}

%description -n libdconf1
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

%package -n gsettings-backend-dconf
Summary:        GSettings integration of the dconf key-based configuration system
Group:          System/Libraries
Requires:       %{name} >= %{version}
# We really want this to be used as the default GSettings backend
Supplements:    libgio-2_0-0
%{glib2_gio_module_requires}

%description -n gsettings-backend-dconf
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

This package provides a GSettings backend that uses dconf to store
the settings.

%package devel
Summary:        Development files for dconf, a key-based configuration system
Group:          Development/Libraries/GNOME
Requires:       libdconf1 = %{version}
# The libdbus-1 backend has been removed. Dconf now always uses GDBus (since 0.25.x)
Obsoletes:      libdconf-dbus-devel < %{version}

%description devel
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

%prep
%autosetup -p1

%build
%meson \
	-Dbash_completion=true \
	-Dman=true \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/dconf/{profile,db}

%post -n libdconf1 -p /sbin/ldconfig
%postun -n libdconf1 -p /sbin/ldconfig

%post -n gsettings-backend-dconf
%{glib2_gio_module_post}

%postun -n gsettings-backend-dconf
%{glib2_gio_module_postun}

%files
%license COPYING
%doc NEWS README
# small utility to read values in the database
%{_bindir}/dconf
# service is needed for write
%{_libexecdir}/dconf-service
%{_datadir}/dbus-1/services/ca.desrt.dconf.service
# Bash completion helper
%{_datadir}/bash-completion/completions/dconf
%{_mandir}/man[17]/dconf.[17]%{ext_man}
%{_mandir}/man1/dconf-service.1%{?ext_man}
# alternative databases
%{_sysconfdir}/dconf/
%{_userunitdir}/dconf.service

%files -n libdconf1
%{_libdir}/libdconf.so.*

%files -n gsettings-backend-dconf
%{_libdir}/gio/modules/libdconfsettings.so

%files devel
%doc HACKING
%doc %{_datadir}/gtk-doc/html/dconf/
%{_includedir}/dconf/
%{_libdir}/libdconf.so
%{_libdir}/pkgconfig/dconf.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/dconf.*

%changelog
