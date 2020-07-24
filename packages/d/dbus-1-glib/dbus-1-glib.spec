#
# spec file for package dbus-1-glib
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


Name:           dbus-1-glib
Version:        0.110
Release:        0
Summary:        GLib-based library for using D-Bus
License:        AFL-2.1 OR GPL-2.0-or-later
URL:            https://dbus.freedesktop.org/
Source0:        http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  dbus-1-devel >= 1.8
BuildRequires:  glib2-devel >= 2.40
BuildRequires:  libexpat-devel
BuildRequires:  libselinux-devel
Requires:       dbus-1
Recommends:     dbus-1-glib-tool
#

%package -n dbus-1-glib-devel
Summary:        Developer package for D-Bus/GLib bindings
Requires:       dbus-1-devel
Requires:       dbus-1-glib = %{version}
Requires:       dbus-1-glib-tool = %{version}
Requires:       glib2-devel

%package -n dbus-1-glib-doc
Summary:        Documentation for the D-Bus/GLib bindings
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%package -n dbus-1-glib-tool
Summary:        Tool package for D-Bus/GLib bindings
Requires:       dbus-1-glib = %{version}

%description
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

%description -n dbus-1-glib-devel
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

%description -n dbus-1-glib-doc
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

%description -n dbus-1-glib-tool
D-Bus add-on tool to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

%prep
%setup -q -n dbus-glib-%{version}

%build
%configure \
    --libexecdir=%{_libexecdir}/%{name}	\
%if 0%{?_crossbuild}
    --with-dbus-binding-tool=%{_bindir}/dbus-binding-tool \
%endif
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove the exacutable bit from dbus-bash-completion.sh
chmod -x %{buildroot}/%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/*glib*.so.*
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libexecdir}/%{name}

%files -n dbus-1-glib-devel
%{_includedir}/dbus-1.0/dbus/*
%{_libdir}/*glib*.so
%{_libdir}/pkgconfig/dbus-glib-1.pc

%files -n dbus-1-glib-doc
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/dbus-glib

%files -n dbus-1-glib-tool
%{_bindir}/dbus-binding-tool
%{_mandir}/man?/dbus-binding-tool.1%{?ext_man}

%changelog
