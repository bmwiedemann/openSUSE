#
# spec file for package notify-osd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _version 0.9.35+16.04.20160415
Name:           notify-osd
Version:        0.9.35~bzr20160415
Release:        0
Summary:        Streamlined Notification Daemon
License:        GPL-3.0+
Group:          System/X11/Utilities
Url:            https://launchpad.net/notify-osd
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
# PATCH-FEATURE-OPENSUSE notify-osd-leolik.patch -- Extend the configuration capabilities, patch by Roman Sukochev (Leolik) from https://launchpad.net/~leolik/+archive/leolik.
Patch0:         %{name}-leolik.patch
# PATCH-FIX-UPSTREAM notify-osd-fix-workarea.patch sor.alexei@meowr.ru -- Fix workarea on Gtk 3.22+.
Patch1:         %{name}-fix-workarea.patch
# PATCH-FIX-UPSTREAM notify-osd-fix-voidreturn.patch sor.alexei@meowr.ru -- Fix value non-return in display.c stack_layout().
Patch2:         %{name}-fix-voidreturn.patch
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake >= 1.8
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(pixman-1)
Provides:       dbus(org.freedesktop.Notifications)
%glib2_gsettings_schema_requires

%description
This notification daemon is an alternative to the
mate-notification-daemon package. It follows the freedesktop
notification specification and introduces some new policies for
streamlining the user-experience by discouraging the use of actions
and timeouts.

%prep
%setup -q -c
%patch0
%patch1 -p1
%patch2 -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --disable-schemas-compile
make %{?_smp_mflags} V=1

%install
%make_install
%fdupes %{buildroot}%{_datadir}/

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_libexecdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
%{_datadir}/glib-2.0/schemas/com.canonical.NotifyOSD.gschema.xml
%dir %{_datadir}/GConf/
%dir %{_datadir}/GConf/gsettings/
%{_datadir}/GConf/gsettings/notify-osd.convert

%changelog
