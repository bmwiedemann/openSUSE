#
# spec file for package syncthing-gtk
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


%global __requires_exclude typelib\\((Caja|Nautilus|Nemo)\\)
%define _name   syncthing_gtk
Name:           syncthing-gtk
Version:        0.9.4.4
Release:        0
Summary:        Syncthing Gtk-based graphical interface
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/syncthing/syncthing-gtk
Source:         https://github.com/syncthing/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM syncthing-gtk-fix-config-read.patch sor.alexei@meowr.ru -- Fix configuration read with non-ASCII locales.
Patch0:         syncthing-gtk-fix-config-read.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  syncthing >= 0.14.50
BuildRequires:  update-desktop-files
Requires:       psmisc
Requires:       syncthing >= 0.14.50
Recommends:     %{name}-lang
Recommends:     librsvg
# caja-extension-syncthing-gtk was last used in openSUSE Leap 42.1.
Provides:       caja-extension-%{name} = %{version}
Obsoletes:      caja-extension-%{name} < %{version}
# nautilus-extension-syncthing-gtk was last used in openSUSE Leap 42.1.
Provides:       nautilus-extension-%{name} = %{version}
Obsoletes:      nautilus-extension-%{name} < %{version}
# nemo-extension-syncthing-gtk was last used in openSUSE Leap 42.1.
Provides:       nemo-extension-%{name} = %{version}
Obsoletes:      nemo-extension-%{name} < %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-bcrypt
Requires:       python2-cairo
Requires:       python2-gobject
Requires:       python2-gobject-Gdk
Requires:       python2-gobject-cairo
Requires:       python2-python-dateutil
Requires:       python2-xml
%else
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-bcrypt
Requires:       python-cairo
Requires:       python-dateutil
Requires:       python-gobject
Requires:       python-gobject-Gdk
Requires:       python-gobject-cairo
Requires:       python-xml
%endif

%description
Graphical user interface with notification area icon for Syncthing
based on GTK+ and Python.

Supported Syncthing features:
 * Everything what WebUI can display.
 * Adding / editing / deleting nodes.
 * Adding / editing / deleting repositories.
 * Restart / shutdown server.
 * Editing daemon settings.

Additional features:
 * First run wizard for initial configuration.
 * Running Syncthing daemon in background.
 * Half-automatic setup for new nodes and repositories.
 * Filesystem watching and instant synchronisation using inotify.
 * Caja, Nemo, and Nautilus file managers integration.
 * Desktop notifications.

%lang_package

%prep
%setup -q
%patch0 -p1
sed -i 's/^\(Exec=\).*$/\1%{name}/' %{name}.desktop

%build
python2 setup.py build_py \
  --nostdownloader

%install
python2 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

%suse_update_desktop_file -r %{name} Network FileTransfer
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/emblems/emblem-*.png
%{_datadir}/icons/hicolor/*/status/si-*.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*syncthingtk.appdata.xml
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
