#
# spec file for package mate-netbook
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.22
Name:           mate-netbook
Version:        1.22.1
Release:        0
Summary:        MATE Desktop window management tool
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE mate-netbook-gtk-3.20.patch -- Restore GLib 2.48 and GTK+ 3.20 support.
Patch0:         mate-netbook-gtk-3.20.patch
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(xtst)
Requires:       mate-panel >= %{_version}
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
This package provides a simple window management tool which provides the
following functionality:
 * Allow to set basic rules for window types;
 * Allow exceptions to the rules based on string matching for window
   name and window class;
 * Allows reversing of rules when the user manually changes something;
 * Re-decorates windows on un-maximise

%lang_package

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%config %{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
%{_bindir}/mate-maximus
%{_libexecdir}/%{name}/
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.panel.MateWindowPicker.mate-panel-applet
%dir %{_datadir}/mate-panel/ui/
%{_datadir}/mate-panel/ui/mate-window-picker-applet-menu.xml
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_mandir}/man?/mate-maximus.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
