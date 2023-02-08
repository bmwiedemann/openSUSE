#
# spec file for package terminus
#
# Copyright (c) 2023 SUSE LLC
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


Name:           terminus
Version:        2.1.0
Release:        0
Summary:        An X terminal written in Vala
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://www.rastersoft.com/programas/terminus.html
Source:         https://gitlab.com/rastersoft/terminus/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.30
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(vte-2.91)
Recommends:     %{name}-lang
Suggests:       gnome-shell-extension-terminus

%description
A terminal with the capabilities of Guake and Terminator.

%package -n     gnome-shell-extension-terminus
Summary:        Show Terminus Quake Mode
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-shell
BuildArch:      noarch

%description -n gnome-shell-extension-terminus
Allows to show the Quake-like terminal from Terminus by pressing the
defined hotkey.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}/%{_datadir}

rm %{buildroot}%{_datadir}/doc/terminus/CMakeLists.txt
rm %{buildroot}%{_datadir}/terminus/CMakeLists.txt

%files
%license LICENSE
%doc HISTORY.md README.md
%{_bindir}/terminus
%{_bindir}/terminus_showhide
%{_datadir}/applications/terminus.desktop
%{_datadir}/dbus-1/services/com.rastersoft.terminus.service
%{_datadir}/glib-2.0/schemas/org.rastersoft.terminus.gschema.xml
%{_datadir}/icons/hicolor/*/apps/terminus.??g
%{_datadir}/terminus/
%{_sysconfdir}/xdg/autostart/terminus_autorun.desktop

%files -n gnome-shell-extension-terminus
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/showTerminusQuakeWindow@rastersoft.com/

%files lang -f %{name}.lang

%changelog
