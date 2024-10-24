#
# spec file for package colord
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


%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d

Name:           colord
Version:        1.4.6
Release:        0
Summary:        System Daemon for Managing Color Devices
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://github.com/hughsie/colord/
Source0:        https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
Source1:        https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FEATURE-OPENSUSE
Patch0:         harden_colord.service.patch
# Apparmor profile
Source3:        usr.lib.colord
Source4:        colord.sysusers
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM colord-CVE-2021-42523.patch boo#1202802 mgorse@suse.com -- fix a small memory leak on db open failure.
Patch1:         colord-CVE-2021-42523.patch

BuildRequires:  argyllcms
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.9
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb) >= 0.2.2
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(vapigen)
Requires:       argyllcms
Requires:       colord-color-profiles
%sysusers_requires
%{?systemd_requires}

%description
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n libcolord2
Summary:        Library for managing color devices
Group:          System/Libraries
Suggests:       %{name}

%description -n libcolord2
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n libcolorhug2
Summary:        Library for managing color devices
Group:          System/Libraries
Suggests:       %{name}

%description -n libcolorhug2
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package color-profiles
Summary:        Color profiles for colord
Group:          System/Libraries
# Last version of shared-color profiles packaged
Obsoletes:      shared-color-profiles <= 0.1.6
Provides:       shared-color-profiles = %{version}

%description    color-profiles
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

This package provides color profiles previously provided by shared-color-profiles

%package -n typelib-1_0-Colord-1_0
Summary:        Introspection bindings for libcolord
Group:          System/Libraries

%description -n typelib-1_0-Colord-1_0
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

This package provides the GObject Introspection bindings for the
libcolord library.

%package -n typelib-1_0-Colorhug-1_0
Summary:        Introspection bindings for libcolorhug
Group:          System/Libraries

%description -n typelib-1_0-Colorhug-1_0
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

This package provides the GObject Introspection bindings for the
libcolorhug library.

%package -n libcolord-devel
Summary:        Development files for libcolord
Group:          Development/Languages/C and C++
Requires:       %{name}-color-profiles = %{version}
Requires:       libcolord2 = %{version}
Requires:       libcolorhug2 = %{version}
Requires:       typelib-1_0-Colord-1_0 = %{version}
Requires:       typelib-1_0-Colorhug-1_0 = %{version}

%description -n libcolord-devel
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%lang_package

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}.conf
# Set ~2 GiB limit so that colprof is forced to work in chunks when
# generating the print profile rather than trying to allocate a 3.1 GiB
# chunk of RAM to put the entire B-to-A tables in.
ulimit -Sv 2000000

# Avoid boo#1228331 (incompatible pointer passed to a function)
%global optflags %{optflags} "-D_FILE_OFFSET_BITS=64" "-D_TIME_BITS=64"

%meson \
	-Dsession_example=false \
	-Dbash_completion=true \
	-Dsystemd=true \
	-Dlibcolordcompat=true \
	-Dargyllcms_sensor=true \
	-Dsane=false \
	-Dvapi=true \
	-Dprint_profiles=true \
	-Dtests=false \
	-Dinstalled_tests=false \
	-Ddaemon_user=colord \
	-Dman=true \
	-Ddocs=true \
	-Dudev_rules=true \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

# Install Apparmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/
install -c -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/

install -Dm0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
%find_lang %{name}

%pre -f %{name}.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%tmpfiles_create %{_tmpfilesdir}/colord.conf
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%post -n libcolord2 -p /sbin/ldconfig
%postun -n libcolord2 -p /sbin/ldconfig
%post -n libcolorhug2 -p /sbin/ldconfig
%postun -n libcolorhug2 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS
%{_unitdir}/colord.service
%{_sysusersdir}/%{name}.conf
%{_udevrulesdir}/*.rules
%attr(755,colord,colord) %dir %{_localstatedir}/lib/colord
%ghost %attr(755,colord,colord) %{_localstatedir}/lib/colord/icc
%attr(644,,-,-) %{_datadir}/bash-completion/completions/colormgr
%{_bindir}/cd-create-profile
%{_bindir}/cd-fix-profile
%{_bindir}/cd-iccdump
%{_bindir}/cd-it8
%{_bindir}/colormgr
%{_libdir}/colord-sensors/
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}-session
%{_datadir}/%{name}/
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorHelper.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorManager.*
%{_datadir}/dbus-1/services/org.freedesktop.ColorHelper.service
%{_datadir}/dbus-1/system-services/org.freedesktop.ColorManager.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.ColorManager.conf
%{_datadir}/glib-2.0/schemas/org.freedesktop.ColorHelper.gschema.xml
%{_datadir}/polkit-1/actions/org.freedesktop.color.policy
%{_mandir}/man1/cd-create-profile.1%{?ext_man}
%{_mandir}/man1/cd-fix-profile.1%{?ext_man}
%{_mandir}/man1/cd-it8.1%{?ext_man}
%{_mandir}/man1/colormgr.1%{?ext_man}
%dir %{_sysconfdir}/apparmor.d/
%config %{_sysconfdir}/apparmor.d/usr.lib.colord
%dir %{_libdir}/colord-plugins
%{_libdir}/libcolordcompat.so
%{_libdir}/colord-plugins/libcolord_sensor_camera.so
%{_libdir}/colord-plugins/libcolord_sensor_scanner.so
%{_userunitdir}/colord-session.service
%{_tmpfilesdir}/colord.conf

%files color-profiles
%{_datadir}/color/

%files -n libcolord2
%{_libdir}/libcolord.so.*
%{_libdir}/libcolordprivate.so.*

%files -n libcolorhug2
%{_libdir}/libcolorhug.so.*

%files -n typelib-1_0-Colord-1_0
%{_libdir}/girepository-1.0/Colord-1.0.typelib

%files -n typelib-1_0-Colorhug-1_0
%{_libdir}/girepository-1.0/Colorhug-1.0.typelib

%files -n libcolord-devel
%{_includedir}/colord-1/
%{_libdir}/libcolord.so
%{_libdir}/libcolordprivate.so
%{_libdir}/libcolorhug.so
%{_libdir}/pkgconfig/colord.pc
%{_libdir}/pkgconfig/colorhug.pc
%{_datadir}/gir-1.0/Colord-1.0.gir
%{_datadir}/gir-1.0/Colorhug-1.0.gir
%{_datadir}/vala/vapi/colord.deps
%{_datadir}/vala/vapi/colord.vapi
%{_datadir}/gtk-doc/html/colord/

%files lang -f %{name}.lang

%changelog
