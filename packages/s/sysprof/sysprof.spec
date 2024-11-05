#
# spec file for package sysprof
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2016 Bjørn Lie, Bryne, Norway.
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


%define apiver 6
%define sover 6
%define glib_version 2.76.0

Name:           sysprof
Version:        47.1
Release:        0
Summary:        A system-wide Linux profiler
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://wiki.gnome.org/Apps/Sysprof
Source0:        sysprof-%{version}.tar.zst
Patch0:         harden_sysprof3.service.patch
Patch1:         explicitly-include-unistd.patch

BuildRequires:  c++_compiler
%if 0%{?sle_version} && 0%{?sle_version} < 160000
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.alpha
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.30.0
BuildRequires:  pkgconfig(libdex-1) >= 0.3
BuildRequires:  pkgconfig(libpanel-1) >= 1.3.0
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.105
BuildRequires:  pkgconfig(systemd)
Requires:       hicolor-icon-theme
%{?systemd_ordering}

%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.

%package gtk
Summary:        Sysprof binary with GUI support
Obsoletes:      sysprof-ui < 3.49

%description gtk
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.

This package provides the sysprof binary with GUI support.

%package -n libsysprof-%{apiver}-%{sover}
Summary:        Sysprof Shared Library

%description -n libsysprof-%{apiver}-%{sover}
The libsysprof-%{apiver}-%{sover} package contains the Sysprof shared
library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Requires:       libsysprof-%{apiver}-%{sover} = %{version}
Obsoletes:      sysprof-capture-devel-static < 3.49

%description    devel
The %{name}-devel package contains header files for developing
applications that use %{name}.

%lang_package

%prep
%autosetup -N -n sysprof-%{version}
%patch -P 0 -p1
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%patch -P 1 -p1
%endif

%build
%if 0%{?sle_version} && 0%{?sle_version} < 160000
export CC=gcc-11
export CXX=g++-11
%endif
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%meson -Dgtk=true -Dtests=false
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%meson_test

%pre
%service_add_pre sysprof3.service

%preun
%service_del_preun sysprof3.service

%post
/sbin/ldconfig
%service_add_post sysprof3.service

%postun
/sbin/ldconfig
%service_del_postun sysprof3.service

%ldconfig_scriptlets -n libsysprof-%{apiver}-%{sover}

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/sysprof-agent
%{_bindir}/sysprof-cli
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof.Agent.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof3.conf
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof3.service
%{_datadir}/polkit-1/actions/org.gnome.sysprof3.policy
%{_libdir}/libsysprof-memory-%{apiver}.so
%{_libdir}/libsysprof-speedtrack-%{apiver}.so
%{_libdir}/libsysprof-tracer-%{apiver}.so
%{_libexecdir}/sysprofd
%{_unitdir}/sysprof3.service
%dir %{_datadir}/help/C/sysprof
%doc %{_datadir}/help/C/sysprof/*

%files gtk
%{_bindir}/sysprof
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.gnome.Sysprof.appdata.xml
%{_datadir}/mime/packages/sysprof-mime.xml

%files -n libsysprof-%{apiver}-%{sover}
%{_libdir}/libsysprof-%{apiver}.so.%{sover}
%{_libdir}/libsysprof-%{apiver}.so.%{sover}.?.?

%files devel
%doc AUTHORS
%{_libdir}/libsysprof-%{apiver}.so
%{_libdir}/pkgconfig/sysprof-%{apiver}.pc
%{_libdir}/libsysprof-capture-4.a
%{_libdir}/pkgconfig/sysprof-capture-4.pc
%{_includedir}/sysprof-%{apiver}/

%files lang -f %{name}.lang

%changelog
