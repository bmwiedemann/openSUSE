#
# spec file for package terminator
#
# Copyright (c) 2022 SUSE LLC
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


%global __requires_exclude typelib\\(Gnome\\)
Name:           terminator
Version:        2.1.2
Release:        0
Summary:        Store and run multiple GNOME terminals in one window
License:        GPL-2.0-only
Group:          System/X11/Terminals
URL:            https://github.com/gnome-terminator/terminator
Source:         https://github.com/gnome-terminator/terminator/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         terminator-desktop.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-cairo
BuildRequires:  python3-configobj
BuildRequires:  python3-dbus-python
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  typelib(Vte) = 2.91
Requires:       gsettings-desktop-schemas
Requires:       python3-cairo
Requires:       python3-configobj
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires(post): hicolor-icon-theme
Requires(postun):hicolor-icon-theme
BuildArch:      noarch

%description
Multiple GNOME terminals in one window.  This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable
grid of terminals. As such, you can  produce a very flexible
arrangements of terminals for different tasks.

%lang_package

%prep
%autosetup -p0
# https://github.com/gnome-terminator/terminator/issues/554
sed -i 's:pytest-runner::' setup.py
# remove pointless shebangs
sed -i '/#! \?\/usr.*/d' terminatorlib/*.py

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}

rm %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications data/%{name}.desktop
%suse_update_desktop_file %{name}

%fdupes %{buildroot}
%find_lang %{name}

%check
xvfb-run python3 -m pytest

%files
%license COPYING
%dir %{_datadir}/icons/HighContrast
%dir %{_datadir}/icons/HighContrast/16x16
%dir %{_datadir}/icons/HighContrast/16x16/actions
%dir %{_datadir}/icons/HighContrast/16x16/apps
%dir %{_datadir}/icons/HighContrast/16x16/status
%dir %{_datadir}/icons/HighContrast/22x22
%dir %{_datadir}/icons/HighContrast/22x22/apps
%dir %{_datadir}/icons/HighContrast/24x24
%dir %{_datadir}/icons/HighContrast/24x24/apps
%dir %{_datadir}/icons/HighContrast/32x32
%dir %{_datadir}/icons/HighContrast/32x32/apps
%dir %{_datadir}/icons/HighContrast/48x48
%dir %{_datadir}/icons/HighContrast/48x48/apps
%dir %{_datadir}/icons/HighContrast/scalable
%dir %{_datadir}/icons/HighContrast/scalable/apps
%{_bindir}/%{name}*
%{_bindir}/remotinator
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
%{python3_sitelib}/terminatorlib/
%{python3_sitelib}/terminator-*.egg-info
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/icons/hicolor/*/*/%{name}*.svg
%{_datadir}/icons/HighContrast/*/*/%{name}*.png
%{_datadir}/icons/HighContrast/*/*/%{name}*.svg
%{_datadir}/icons/hicolor/16x16/status/terminal-bell.png
%{_datadir}/icons/HighContrast/16x16/status/terminal-bell.png
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/terminatorlib
%dir %{_datadir}/%{name}/terminatorlib/themes
%dir %{_datadir}/%{name}/terminatorlib/themes/Adwaita
%dir %{_datadir}/%{name}/terminatorlib/themes/Adwaita/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/Adwaita/gtk-3.0/apps
%dir %{_datadir}/%{name}/terminatorlib/themes/Ambiance
%dir %{_datadir}/%{name}/terminatorlib/themes/Ambiance/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/Ambiance/gtk-3.0/apps
%dir %{_datadir}/%{name}/terminatorlib/themes/Breeze
%dir %{_datadir}/%{name}/terminatorlib/themes/Breeze/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/Breeze/gtk-3.0/apps
%dir %{_datadir}/%{name}/terminatorlib/themes/HighContrast
%dir %{_datadir}/%{name}/terminatorlib/themes/HighContrast/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/HighContrast/gtk-3.0/apps
%dir %{_datadir}/%{name}/terminatorlib/themes/Radiance
%dir %{_datadir}/%{name}/terminatorlib/themes/Radiance/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/Radiance/gtk-3.0/apps
%dir %{_datadir}/%{name}/terminatorlib/themes/Raleigh
%dir %{_datadir}/%{name}/terminatorlib/themes/Raleigh/gtk-3.0
%dir %{_datadir}/%{name}/terminatorlib/themes/Raleigh/gtk-3.0/apps
%{_datadir}/%{name}/terminatorlib/themes/Adwaita/gtk-3.0/apps/terminator.css
%{_datadir}/%{name}/terminatorlib/themes/Ambiance/gtk-3.0/apps/terminator.css
%{_datadir}/%{name}/terminatorlib/themes/Ambiance/gtk-3.0/apps/terminator_styling.css
%{_datadir}/%{name}/terminatorlib/themes/Breeze/gtk-3.0/apps/terminator.css
%{_datadir}/%{name}/terminatorlib/themes/HighContrast/gtk-3.0/apps/terminator.css
%{_datadir}/%{name}/terminatorlib/themes/Radiance/gtk-3.0/apps/terminator.css
%{_datadir}/%{name}/terminatorlib/themes/Radiance/gtk-3.0/apps/terminator_styling.css
%{_datadir}/%{name}/terminatorlib/themes/Raleigh/gtk-3.0/apps/terminator.css

%files lang -f %{name}.lang

%changelog
