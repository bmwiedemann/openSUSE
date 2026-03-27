#
# spec file for package gnome-robots
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gnome-robots
Version:        50.0
Release:        0
Summary:        Robots Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://live.gnome.org/Robots
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz

BuildRequires:  cargo
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.86
BuildRequires:  pkgconfig(glib-2.0) >= 2.86
BuildRequires:  pkgconfig(gtk4) >= 4.20.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(glycin-2) >= 2.0
BuildRequires:  pkgconfig(glycin-gtk4-2) >= 2.0

%description
Robots is a graphical version of the original text based robots game,
which can be found on a number of UNIX systems. The player must outwit
the robots chasing him/her by getting them to run into each other.

%lang_package

%prep
%autosetup -p1 -a1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.Robots.desktop
%{_datadir}/dbus-1/services/org.gnome.Robots.service
%{_datadir}/glib-2.0/schemas/org.gnome.Robots.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.gnome.Robots.metainfo.xml
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_bindir}/%{name}

%files lang -f %{name}.lang

%changelog
