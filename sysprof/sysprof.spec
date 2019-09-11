#
# spec file for package sysprof
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sysprof
Version:        3.32.0
Release:        0
Summary:        A system-wide Linux profiler
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Debuggers
URL:            https://wiki.gnome.org/Apps/Sysprof
Source0:        https://download.gnome.org/sources/sysprof/3.32/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
Requires:       hicolor-icon-theme
%{?systemd_requires}

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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.Sysprof2 Profiling

%check
%meson_test

%pre
%service_add_pre sysprof2.service

%preun
%service_del_preun sysprof2.service

%post
/sbin/ldconfig
%service_add_post sysprof2.service

%postun
/sbin/ldconfig
%service_del_postun sysprof2.service

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/sysprof
%{_bindir}/sysprof-cli
%{_libdir}/libsysprof-2.so
%{_libdir}/libsysprof-ui-2.so
%dir %{_libexecdir}/sysprof
%{_libexecdir}/sysprof/sysprofd
%{_datadir}/applications/*.desktop
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/glib-2.0/schemas/org.gnome.sysprof2.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.gnome.Sysprof2.appdata.xml
%{_datadir}/mime/packages/sysprof-mime.xml
%{_datadir}/polkit-1/actions/org.gnome.sysprof2.policy
%{_unitdir}/sysprof2.service
%dir %{_datadir}/help/C/sysprof
%doc %{_datadir}/help/C/sysprof/*

%files devel
%doc AUTHORS TODO
%{_includedir}/sysprof-2/
%{_libdir}/pkgconfig/sysprof-2.pc
%{_libdir}/pkgconfig/sysprof-ui-2.pc

%files capture-devel-static
%{_libdir}/libsysprof-capture-2.a
%{_libdir}/pkgconfig/sysprof-capture-2.pc

%files lang -f %{name}.lang

%changelog
