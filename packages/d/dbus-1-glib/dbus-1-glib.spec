#
# spec file for package dbus-1-glib
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


%define soname libdbus-glib-1-2

Name:           dbus-1-glib
Version:        0.112
Release:        0
Summary:        GLib-based library for using D-Bus
License:        AFL-2.1 OR GPL-2.0-or-later
URL:            https://dbus.freedesktop.org/
Source0:        https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
Source1:        https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz.asc
Source2:        https://db.debian.org/fetchkey.cgi?fingerprint=DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90#/%{name}.keyring
Source99:       baselibs.conf

BuildRequires:  libexpat-devel
BuildRequires:  libselinux-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1) >= 1.8
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40

%description
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

%package -n %{soname}
Summary:        GLib-based library for using D-Bus
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# Split provides: libdbus-glib-1.so.2 used to be in dbus-1-glib before 0.112
Provides:       %{name}:%{_libdir}/libdbus-glib-1.so.2

%description -n %{soname}
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

This package contains the shared library files.

%package -n dbus-1-glib-devel
Summary:        Developer package for D-Bus/GLib bindings
Requires:       %{soname} = %{version}
Requires:       dbus-1-glib-tool = %{version}

%description -n dbus-1-glib-devel
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

This package contains the devel and header files.

%package -n dbus-1-glib-doc
Summary:        Documentation for the D-Bus/GLib bindings
BuildArch:      noarch

%description -n dbus-1-glib-doc
D-Bus add-on library to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

This package contains developer documentation.

%package -n dbus-1-glib-tool
Summary:        Tool package for D-Bus/GLib bindings
Requires:       %{name} = %{version}

%description -n dbus-1-glib-tool
D-Bus add-on tool to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

This package contains dbus-binding-tool and manpage.

%package bash-completion
Summary:        Bash-completion package for D-Bus/GLib bindings
Requires:       dbus-1-glib-tool
Supplements:    (dbus-1-glib-tool and bash-completion)
# Up to version 0.112, the entire dbus-1-glib was in an unsplit package
Provides:       dbus-1-glib:/etc/bash_completion.d/dbus-bash-completion.sh
Conflicts:      dbus-1-glib < 0.112

%description bash-completion
D-Bus add-on tool to integrate the standard D-Bus library with the
GLib thread abstraction and main loop.

This package contains bash-completion support for %{name}.

%prep
%autosetup -p1 -n dbus-glib-%{version}

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
# Create and move dbus-bash-completion.sh to the correct folder for openSUSE
mkdir %{buildroot}%{_datadir}/bash-completion/
mkdir %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh \
  %{buildroot}%{_datadir}/bash-completion/completions/dbus-bash-completion.sh

%ldconfig_scriptlets -n %{soname}

%files -n %{soname}
%license COPYING
%doc NEWS
%{_libdir}/libdbus-glib-1.so.*

%files -n dbus-1-glib-devel
%{_includedir}/dbus-1.0/dbus/*
%{_libdir}/*glib*.so
%{_libdir}/pkgconfig/dbus-glib-1.pc

%files -n dbus-1-glib-doc
%doc CONTRIBUTING.md
%doc %{_datadir}/gtk-doc/html/dbus-glib

%files -n dbus-1-glib-tool
%{_bindir}/dbus-binding-tool
%{_mandir}/man?/dbus-binding-tool.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/dbus-bash-completion.sh
%{_libexecdir}/%{name}

%changelog
