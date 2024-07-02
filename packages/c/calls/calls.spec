#
# spec file for package calls
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


Name:           calls
Version:        46.3
Release:        0
Summary:        A phone dialer and call handler
License:        GPL-3.0-only AND MIT
URL:            https://gitlab.gnome.org/GNOME/calls
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  sofia-sip
BuildRequires:  vala
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcallaudio-0.1)
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(sofia-sip-ua-glib)

%description
%{summary}.

Calls is also a capable sip-client.

%package ofono
Summary:        Ofono support for %{name}
Requires:       %{name} = %{version}

%description ofono
%{summary}.

This package is not recommended, only install if you are sure you
want ofono support.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	--sysconfdir=%{_distconfdir} \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%find_lang call-ui %{?no_lang_C}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calls.desktop

## Some tests are failing in the build environment, so we manually just run a handful for now.
#LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
#%%meson_test manager plugins
#SH

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/provider
%dir %{_libdir}/%{name}/plugins/provider/mm
%dir %{_libdir}/%{name}/plugins/provider/dummy
%dir %{_libdir}/%{name}/plugins/provider/sip
%{_libdir}/%{name}/plugins/provider/mm/libmm.so
%{_libdir}/%{name}/plugins/provider/mm/mm.plugin
%{_libdir}/%{name}/plugins/provider/dummy/dummy.plugin
%{_libdir}/%{name}/plugins/provider/dummy/libdummy.so
%{_libdir}/%{name}/plugins/provider/sip/libsip.so
%{_libdir}/%{name}/plugins/provider/sip/sip.plugin
# ofono is dead upstream so we explicitly exclude the plugins from main package
%exclude %{_libdir}/%{name}/plugins/provider/ofono/libofono.so
%exclude %{_libdir}/%{name}/plugins/provider/ofono/ofono.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.Calls.gschema.xml
%{_datadir}/applications/org.gnome.Calls.desktop
%{_datadir}/dbus-1/services/org.gnome.Calls.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calls-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml
%{_mandir}/man1/gnome-calls.1%{?ext_man}
%{_distconfdir}/xdg/autostart/org.gnome.Calls-daemon.desktop

%files ofono
%dir %{_libdir}/%{name}/plugins/provider/ofono
%{_libdir}/%{name}/plugins/provider/ofono/libofono.so
%{_libdir}/%{name}/plugins/provider/ofono/ofono.plugin

%files lang -f %{name}.lang -f call-ui.lang

%changelog
