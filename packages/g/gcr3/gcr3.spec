#
# spec file for package gcr3
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _name gcr
Name:           gcr3
Version:        3.41.2
Release:        0
# FIXME: Verify if the requires in typelib-1_0-Gcr-3 is still correct and required (see bgo#725501).
Summary:        Library for Crypto UI related tasks
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org
Source0:        %{_name}-%{version}.tar.zst
Source1:        baselibs.conf
# PATCH-FIX-SLE gcr-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com -- use libgcrypt allocators for FIPS mode
Patch1:         gcr-bsc932232-use-libgcrypt-allocators.patch

# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  gobject-introspection-devel >= 1.34
BuildRequires:  libgcrypt-devel >= 1.4.5
BuildRequires:  meson >= 0.52
BuildRequires:  pkgconfig(gi-docgen)
# configure is looking for the gpg2 path
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.18.0.22
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1) >= 0.19.0
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(systemd)

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package viewer
Summary:        Viewer for Crypto Files
Group:          Productivity/Security
Provides:       %{_name}-viewer = %{version}
Conflicts:      %{_name}-viewer

%description viewer
This packages provides the viewer for crypto files on the GNOME desktop.

%package data
Summary:        Data and icon set for gcr
Group:          System/Libraries
Provides:       %{_name}-data = %{version}
Obsoletes:      %{_name}-data <= %{version}
Conflicts:      %{_name}-data
BuildArch:      noarch

%description data
This package provides the GSettings schemas and a collection of icons
needed by libgcr.

%package prompter
Summary:        Prompt dialog for gcr
Group:          System/Libraries
Provides:       %{_name}-prompter = %{version}
Obsoletes:      %{_name}-prompter <= %{version}
Conflicts:      %{_name}-prompter

%description prompter
This package provides the prompt dialog needed by libgcr.

%package ssh-askpass
Summary:        SSH password callback helper for gcr
Group:          System/Libraries
Obsoletes:      %{_name}-ssh-askpass <= %{version}
Supplements:    (gpg2 and gnome-shell)

%description ssh-askpass
gcr-ssh-askpass allows an ssh command to callback for a password.

%package ssh-agent
Summary:        SSH agent binary for gcr
Group:          System/Libraries
Provides:       %{_name}-ssh-agent = %{version}
Obsoletes:      %{_name}-ssh-agent <= %{version}
Conflicts:      %{_name}-ssh-agent
Supplements:    (gpg2 and gnome-shell)

%description ssh-agent
gcr-ssh-agent as a standalone binary, so that it can easily be
managed through systemd.

%package -n libgcr-3-1
Summary:        Library for Crypto UI related tasks
Group:          System/Libraries
Requires:       %{_name}-data >= %{version}
Requires:       %{_name}-prompter >= %{version}
Recommends:     %{_name}-ssh-agent
Recommends:     %{name}-ssh-askpass
# https://bugzilla.opensuse.org/show_bug.cgi?id=1204071 - to properly manage keys using gnome-keyring
Requires:       (%{name}-ssh-askpass if gnome-keyring)
Recommends:     %{_name}-viewer
# To make lang package installable
Provides:       %{name} = %{version}

%description -n libgcr-3-1
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n typelib-1_0-Gcr-3
Summary:        Introspection bindings for gcr, a library for crypto UI related tasks
# Due to broken typelib files, this one cannot be automatically inspected
Group:          System/Libraries
Requires:       typelib-1_0-Gck-1

%description -n typelib-1_0-Gcr-3
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

This package provides the GObject Introspection bindings for GCR.

%package -n typelib-1_0-GcrUi-3
Summary:        Introspection bindings for gcr, a library for crypto UI related tasks
Group:          System/Libraries

%description -n typelib-1_0-GcrUi-3
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

This package provides the GObject Introspection bindings for GCR.

%package -n libgcr3-devel
Summary:        Development files for gcr, a library for crypto UI related tasks
Group:          Development/Libraries/GNOME
Requires:       libgcr-3-1 = %{version}
Requires:       typelib-1_0-Gcr-3 = %{version}
Requires:       typelib-1_0-GcrUi-3 = %{version}

%description -n libgcr3-devel
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n libgck-1-0
Summary:        GObject library to access PKCS#11 modules
# Small hack, to help gnome-keyring subpackage containing gck
# modules have a proper dependency, without having to care about
# the soname.
Group:          System/Libraries
Provides:       gck = %{version}

%description -n libgck-1-0
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package -n typelib-1_0-Gck-1
Summary:        Introspection bindings for gck, a GObject library to access PKCS#11 modules
Group:          System/Libraries

%description -n typelib-1_0-Gck-1
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

This package provides the GObject Introspection bindings for GCK.

%package -n libgck1-devel
Summary:        Development files for gck, a GObject library to access PKCS#11 modules
Group:          Development/Libraries/GNOME
Requires:       libgck-1-0 = %{version}
Requires:       typelib-1_0-Gck-1 = %{version}

%description -n libgck1-devel
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package devel-docs
Summary:        Development documents for gcr and gck
Group:          Development/Libraries/GNOME
BuildArch:      noarch

%description devel-docs
Development documents for gcr and gck.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
%if 0%{?sle_version}
%patch -P 1 -p1
%endif

%build
%meson \
  -Dgpg_path=%{_bindir}/gpg2
%meson_build

%install
%meson_install
%find_lang %{_name}
%fdupes -s %{buildroot}/%{_datadir}/doc/

%ldconfig_scriptlets -n libgcr-3-1
%ldconfig_scriptlets -n libgck-1-0

%post -n %{name}-ssh-agent
%systemd_user_post gcr-ssh-agent.service

%preun -n %{name}-ssh-agent
%systemd_user_preun gcr-ssh-agent.service

%postun -n %{name}-ssh-agent
%systemd_user_postun_with_restart gcr-ssh-agent.service

%files viewer
%license COPYING
%doc NEWS
%{_bindir}/gcr-viewer
%{_datadir}/applications/gcr-viewer.desktop
%{_datadir}/mime/packages/gcr-crypto-types.xml

%files data
%doc NEWS
%{_datadir}/icons/hicolor/*/apps/*
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp.convert
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml

%files prompter
%{_libexecdir}/gcr-prompter
%{_datadir}/applications/gcr-prompter.desktop
%{_datadir}/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%{_datadir}/dbus-1/services/org.gnome.keyring.SystemPrompter.service

%files ssh-askpass
%{_libexecdir}/gcr-ssh-askpass

%files ssh-agent
%{_libexecdir}/gcr-ssh-agent
%{_userunitdir}/gcr-ssh-agent.service
%{_userunitdir}/gcr-ssh-agent.socket

%files -n libgcr-3-1
%license COPYING
%doc NEWS
%{_libdir}/libgcr-base-3.so.*
%{_libdir}/libgcr-ui-3.so.*

%files -n typelib-1_0-Gcr-3
%{_libdir}/girepository-1.0/Gcr-3.typelib

%files -n typelib-1_0-GcrUi-3
%{_libdir}/girepository-1.0/GcrUi-3.typelib

%files -n libgcr3-devel
%{_libdir}/libgcr-base-3.so
%{_libdir}/libgcr-ui-3.so
%{_libdir}/pkgconfig/gcr-3.pc
%{_libdir}/pkgconfig/gcr-base-3.pc
%{_libdir}/pkgconfig/gcr-ui-3.pc
%{_includedir}/gcr-3/
%{_datadir}/gir-1.0/GcrUi-3.gir
%{_datadir}/gir-1.0/Gcr-3.gir

%files -n libgck-1-0
%license COPYING
%doc NEWS
%{_libdir}/libgck-1.so.*

%files -n typelib-1_0-Gck-1
%{_libdir}/girepository-1.0/Gck-1.typelib

%files -n libgck1-devel
%{_libdir}/libgck-1.so
%{_libdir}/pkgconfig/gck-1.pc
%{_includedir}/gck-1/
%{_datadir}/gir-1.0/Gck-1.gir
%{_datadir}/vala/vapi/

%files devel-docs
%doc %{_datadir}/doc/gcr*/
%doc %{_datadir}/doc/gck*/

%files lang -f %{_name}.lang

%changelog
