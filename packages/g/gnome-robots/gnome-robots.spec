#
# spec file for package gnome-robots
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


Name:           gnome-robots
Version:        3.32.0
Release:        0
Summary:        Robots Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://live.gnome.org/Robots
Source0:        https://download.gnome.org/sources/gnome-robots/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gnome-games-scripts
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
Requires(pre):  pwdutils
Recommends:     %{name}-lang

%description
Robots is a graphical version of the original text based robots game,
which can be found on a number of UNIX systems. The player must outwit
the robots chasing him/her by getting them to run into each other.

%lang_package

%prep
%autosetup -p1

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
%{_datadir}/glib-2.0/schemas/org.gnome.Robots.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.gnome.Robots.appdata.xml
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_bindir}/%{name}

%files lang -f %{name}.lang

%changelog
