#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "UI"
  %define enable_gtk true
  %define _name_suffix -ui
%else
  %define enable_gtk false
  %define _name_suffix %nil
%endif

%define sover 4
%define ui_sover 5

Name:           sysprof%{_name_suffix}
Version:        3.48.0
Release:        0
Summary:        A system-wide Linux profiler
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Debuggers
URL:            https://wiki.gnome.org/Apps/Sysprof
Source0:        https://download.gnome.org/sources/sysprof/3.48/sysprof-%{version}.tar.xz
Patch0:         harden_sysprof2.service.patch
Patch1:         harden_sysprof3.service.patch

BuildRequires:  c++_compiler
BuildRequires:  itstool
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.73.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.105
BuildRequires:  pkgconfig(systemd)
%if "%{flavor}" == "UI"
BuildRequires:  hicolor-icon-theme
BuildRequires:  sysprof-capture-devel-static
BuildRequires:  sysprof-devel
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.30.0
Requires:       hicolor-icon-theme
%endif
%{?systemd_ordering}

%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package capture-devel-static
Summary:        Library to read and write syspref's capture format
Group:          Development/Tools/Debuggers

%description capture-devel-static
This static library allows external tooling to read and write the
syspref's capture format.

%lang_package

%prep
%autosetup -p1 -n sysprof-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%meson -Dgtk=%{enable_gtk} -Dtests=false
%meson_build

%install
%meson_install
%if "%{flavor}" == "UI"
%suse_update_desktop_file org.gnome.Sysprof Profiling
for file in $(rpm -qla "*sysprof*"); do
  [ -f %{buildroot}${file} ] && rm %{buildroot}${file}
done
rm -rf %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/sysprof.mo %{buildroot}/%{_datadir}/help/*/sysprof
%else
%find_lang %{name} %{?no_lang_C}
%endif

%check
%meson_test

%if "%{flavor}" == ""
%pre
%service_add_pre sysprof3.service
%service_add_pre sysprof2.service

%preun
%service_del_preun sysprof3.service
%service_del_preun sysprof2.service
%endif

%post
/sbin/ldconfig
%if "%{flavor}" == ""
%service_add_post sysprof3.service
%service_add_post sysprof2.service
%endif

%postun
/sbin/ldconfig
%if "%{flavor}" == ""
%service_del_postun sysprof3.service
%service_del_postun sysprof2.service
%endif

%files
%license COPYING
%doc NEWS README.md
%if "%{flavor}" == "UI"
%{_bindir}/sysprof
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.gnome.Sysprof.appdata.xml
%{_datadir}/mime/packages/sysprof-mime.xml
%{_libdir}/libsysprof-ui-%{ui_sover}.so
%else
%{_bindir}/sysprof-agent
%{_bindir}/sysprof-cli
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof.Agent.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof3.conf
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof3.service
%{_datadir}/polkit-1/actions/org.gnome.sysprof3.policy
%{_libdir}/libsysprof-%{sover}.so
%{_libdir}/libsysprof-memory-%{sover}.so
%{_libdir}/libsysprof-speedtrack-%{sover}.so
%{_libexecdir}/sysprofd
%{_unitdir}/sysprof2.service
%{_unitdir}/sysprof3.service
%dir %{_datadir}/help/C/sysprof
%doc %{_datadir}/help/C/sysprof/*
%endif

%files devel
%doc AUTHORS
%if "%{flavor}" == "UI"
%{_includedir}/sysprof-ui-%{ui_sover}/
%{_libdir}/pkgconfig/sysprof-ui-%{ui_sover}.pc
%else
%{_includedir}/sysprof-%{sover}/
%{_libdir}/pkgconfig/sysprof-%{sover}.pc

%files capture-devel-static
%{_libdir}/libsysprof-capture-%{sover}.a
%{_libdir}/pkgconfig/sysprof-capture-%{sover}.pc

%files lang -f %{name}.lang
%endif

%changelog
