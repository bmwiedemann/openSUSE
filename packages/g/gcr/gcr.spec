#
# spec file for package gcr
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gcr
Version:        4.1.0
Release:        0
# FIXME: Verify if the requires in typelib-1_0-Gcr-4 is still correct and required (see bgo#725501).
Summary:        Library for Crypto UI related tasks
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gcr/4.1/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-SLE gcr-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com -- use libgcrypt allocators for FIPS mode
Patch1:         gcr-bsc932232-use-libgcrypt-allocators.patch

# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  gobject-introspection-devel >= 1.34
# configure is looking for the gpg2 path
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  libgcrypt-devel >= 1.4.5
BuildRequires:  meson >= 0.59
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.18.0.22
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1) >= 0.19.0
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(systemd)

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package viewer
Summary:        Viewer for Crypto Files
Group:          Productivity/Security

%description viewer
This packages provides the viewer for crypto files on the GNOME desktop.
key stores.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package ssh-askpass
Summary:        SSH password callback helper for gcr
Group:          System/Libraries
Supplements:    (gpg2 and gnome-shell)

%description ssh-askpass
gcr-ssh-askpass allows an ssh command to callback for a password.

%package ssh-agent
Summary:        SSH agent binary for gcr
Group:          System/Libraries
Supplements:    (gpg2 and gnome-shell)

%description ssh-agent
gcr-ssh-agent as a standalone binary, so that it can easily be
managed through systemd.

%package -n libgcr-4-4
Summary:        Library for Crypto UI related tasks
Group:          System/Libraries
Recommends:     %{name}-ask-pass
Recommends:     %{name}-ssh-agent
Recommends:     %{name}-viewer = %{version}
# To make lang package installable
Provides:       %{name} = %{version}

%description -n libgcr-4-4
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n typelib-1_0-Gcr-4
Summary:        Introspection bindings for gcr, a library for crypto UI related tasks
# Due to broken typelib files, this one cannot be automatically inspected
Group:          System/Libraries
Requires:       typelib-1_0-Gck-2

%description -n typelib-1_0-Gcr-4
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

This package provides the GObject Introspection bindings for GCR.

%package -n libgcr-devel
Summary:        Development files for gcr, a library for crypto UI related tasks
Group:          Development/Libraries/GNOME
Requires:       libgcr-4-4 = %{version}
Requires:       typelib-1_0-Gcr-4 = %{version}

%description -n libgcr-devel
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n libgck-2-2
Summary:        GObject library to access PKCS#11 modules
# Small hack, to help gnome-keyring subpackage containing gck
# modules have a proper dependency, without having to care about
# the soname.
Group:          System/Libraries
Provides:       gck = %{version}

%description -n libgck-2-2
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package -n typelib-1_0-Gck-2
Summary:        Introspection bindings for gck, a GObject library to access PKCS#11 modules
Group:          System/Libraries

%description -n typelib-1_0-Gck-2
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

This package provides the GObject Introspection bindings for GCK.

%package -n libgck-devel
Summary:        Development files for gck, a GObject library to access PKCS#11 modules
Group:          Development/Libraries/GNOME
Requires:       libgck-2-2 = %{version}
Requires:       typelib-1_0-Gck-2 = %{version}

%description -n libgck-devel
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package doc
Summary:        Documentation for gcr
BuildArch:      noarch

%description doc
This packages provides the documentation for various gcr packages.

%lang_package

%prep
%setup -q -n gcr-%{version}
%if 0%{?sle_version}
%patch1 -p1
%endif

%build
%meson \
	-Dgpg_path=%{_bindir}/gpg2 \
	-Dgtk4=true \
	%nil
%meson_build

%install
%meson_install
%find_lang gcr-4

# Make default docdir ref openSUSE standard
mkdir -p %{buildroot}%{_docdir}
# Move docs from upstream docdir to openSUSE docdir standard
mv %{buildroot}%{_datadir}/doc/gcr-4* %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/gck-2* %{buildroot}%{_docdir}
%fdupes %{buildroot}%{_docdir}

%ldconfig_scriptlets -n libgcr-4-4
%ldconfig_scriptlets -n libgck-2-2

%post -n %{name}-ssh-agent
%systemd_user_post gcr-ssh-agent.service

%preun -n %{name}-ssh-agent
%systemd_user_preun gcr-ssh-agent.service

%files viewer
%license COPYING
%doc NEWS
%{_bindir}/gcr-viewer-gtk4

%files ssh-askpass
%{_libexecdir}/gcr4-ssh-askpass

%files ssh-agent
%{_libexecdir}/gcr-ssh-agent
%{_userunitdir}/gcr-ssh-agent.service
%{_userunitdir}/gcr-ssh-agent.socket

%files -n libgcr-4-4
%license COPYING
%doc NEWS
%{_libdir}/libgcr-4*.so.*

%files -n typelib-1_0-Gcr-4
%{_libdir}/girepository-1.0/Gcr-4.typelib

%files -n libgcr-devel
%{_libdir}/libgcr-4*.so
%{_libdir}/pkgconfig/gcr-4.pc
%{_includedir}/gcr-4/
%{_datadir}/gir-1.0/Gcr-4.gir
%{_datadir}/vala/vapi/gcr-4.deps
%{_datadir}/vala/vapi/gcr-4.vapi

%files -n libgck-2-2
%license COPYING
%doc NEWS
%{_libdir}/libgck-2.so.*

%files -n typelib-1_0-Gck-2
%{_libdir}/girepository-1.0/Gck-2.typelib

%files -n libgck-devel
%{_libdir}/libgck-2.so
%{_libdir}/pkgconfig/gck-2.pc
%{_includedir}/gck-2/
%{_datadir}/gir-1.0/Gck-2.gir
%{_datadir}/vala/vapi/gck-2.deps
%{_datadir}/vala/vapi/gck-2.vapi

%files lang -f gcr-4.lang

%files doc
%doc %{_docdir}/gcr-4*
%doc %{_docdir}/gck-2*

%changelog
