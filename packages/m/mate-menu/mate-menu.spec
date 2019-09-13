#
# spec file for package mate-menu
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


%define _name   mate_menu
Name:           mate-menu
Version:        19.04.0
Release:        0
Summary:        Advanced MATE menu
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/ubuntu-mate/mate-menu
Source:         https://github.com/ubuntu-mate/mate-menu/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE mate-menu-yast2-software.patch sor.alexei@meowr.ru -- Use YaST2 and GNOME PackageKit package managers.
Patch0:         mate-menu-yast2-software.patch
# PATCH-FEATURE-OPENSUSE mate-menu-glib-2.48.patch -- Restore GLib 2.48 support.
Patch1:         mate-menu-glib-2.48.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       glib2-tools
Requires:       gvfs
Requires:       mate-menus
Requires:       mozo
Requires:       python3-Unidecode
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-setproctitle
Requires:       python3-xdg
Requires:       python3-xlib
Requires:       xdg-utils
Recommends:     %{name}-lang
Recommends:     lsb-release
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description
An advanced menu for MATE. Supports filtering, favourites,
autosession, and many other features.

This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.

%lang_package

%prep
%autosetup -p1

sed -i 's/su-to-root/xdg-su/g' %{_name}/execute.py

# Do not use env for python sripts.
sed -i '/^#!/s|env python.*$|python3|' lib/*.py

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

%py3_compile %{buildroot}%{_datadir}/%{name}/plugins/
%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{python3_sitelib}/%{_name}/
%{python3_sitelib}/%{_name}-*
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateMenuAppletFactory.service
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
