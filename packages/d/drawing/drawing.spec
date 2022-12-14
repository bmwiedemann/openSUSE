#
# spec file for package drawing
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


%define _name com.github.maoschanz.drawing
Name:           drawing
Version:        1.0.1
Release:        0
Summary:        A simple drawing application for Linux.
License:        GPL-3.0-only
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/maoschanz/drawing
Source:         https://github.com/maoschanz/drawing/archive/refs/tags/%{version}.tar.gz
Source2:        drawing-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pycairo
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       python3
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-pycairo
Recommends:     yelp
BuildArch:      noarch

%description
This application is a free basic image editor, similar to Microsoft Paint, is aiming at the GNOME desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, the app is well integrated in traditional-looking desktops, as well as an elementaryOS layout.

It should also be compatible with the Pinephone and Librem 5 smartphones.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/glib-2.0/schemas/%{_name}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/%{_name}.appdata.xml

%files lang -f %{name}.lang

%changelog
