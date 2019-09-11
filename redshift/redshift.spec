#
# spec file for package redshift
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           redshift
Version:        1.12
Release:        0
Summary:        Tool for adjusting the color temperature of the screen
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            http://jonls.dk/redshift/
Source:         https://github.com/jonls/redshift/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         desktop.patch
Patch1:         fix_apparmor.patch
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
Recommends:     geoclue2
%{?systemd_requires}

%description
Redshift adjusts the color temperature of the screen according to time.
This may help easing eyestrain when working at night.
Time-independent manual operation and individual gamma curve
setting is possible as well.

%package gtk
Summary:        Gtk frontend for redshift
Group:          System/X11/Utilities
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       python3-xdg
%{?systemd_requires}
%if 0%{?sle_version} > 120100 || 0%{?suse_version} > 1320
Requires:       python3-gobject-Gdk
%else
Requires:       python3-gobject
%endif

%description gtk
A graphical user interface for the redshift tool that integrates into Gtk+ and GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
  --enable-apparmor \
  --enable-drm \
  --enable-gui \
  --enable-geoclue2 \
  --enable-randr \
  --enable-vidmode \
  --with-systemduserunitdir=%{_userunitdir}
%make_build

%install
%make_install
%fdupes -s %{buildroot}%{python3_sitelib}
%suse_update_desktop_file %{name}-gtk GTK X-SuSE-DesktopUtility
sed -i 's|/env python3|/python3|' %{buildroot}%{_bindir}/%{name}-gtk
mkdir %{buildroot}%{_sysconfdir}/apparmor.d/local
echo "# Site-specific additions and overrides for 'usr.bin.redshift'" \
  >%{buildroot}%{_sysconfdir}/apparmor.d/local/usr.bin.redshift

%find_lang %{name}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%post gtk
%systemd_user_post %{name}-gtk.service

%preun gtk
%systemd_user_preun %{name}-gtk.service

%files gtk -f %{name}.lang
%license COPYING
%{_bindir}/%{name}-gtk
%{python3_sitelib}/%{name}_gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-off.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-on.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_userunitdir}/%{name}-gtk.service
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}-gtk.appdata.xml

%files
%license COPYING
%doc README README-colorramp NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%dir %{_sysconfdir}/apparmor.d/
%config %{_sysconfdir}/apparmor.d/usr.bin.redshift
%dir %{_sysconfdir}/apparmor.d/local/
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.bin.redshift
%{_userunitdir}/%{name}.service

%changelog
