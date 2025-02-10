#
# spec file for package xviewer
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


Name:           xviewer
Version:        3.4.8
Release:        0
Summary:        Fast and functional graphics viewer
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxmint/xviewer
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xapp)
Requires:       xapps-common
Suggests:       %{name}-plugins

%description
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%package -n      typelib-1_0-Xviewer-3_0
Summary:        Typelib for %{name}

%description -n  typelib-1_0-Xviewer-3_0
This package provides the typelib for %{name}

%package devel
Summary:        Fast and functional graphics viewer development files
Requires:       typelib-1_0-Xviewer-3_0 = %{version}

%description devel
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%package doc
Summary:        Html documentation for %{name}
BuildArch:      noarch

%description doc
This package provides the docs for %{name}

%lang_package

%prep
%autosetup

%build
%meson \
  -Dexempi=enabled \
  -Dexif=enabled \
  -Djpeg=enabled \
  -Dlcms=enabled \
  -Drsvg=enabled \
  -Ddocs=true \
  -Ddeprecated_warnings=true
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS README.md MAINTAINERS THANKS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/{actions,apps}/*.{png,svg}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.{enums,gschema}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/{icons,pixmaps}

%files -n typelib-1_0-Xviewer-3_0
%dir %{_libdir}/xviewer/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Xviewer-3.0.typelib

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}/lib%{name}.so
%{_datadir}/%{name}/gir-1.0/Xviewer-3.0.gir
%dir %{_datadir}/%{name}/gir-1.0
%dir %{_libdir}/%{name}

%files doc
%{_datadir}/help/*/%{name}/{,figures/}*.{png,page,xml}
%{_datadir}/gtk-doc/html/xviewer
%dir %{_datadir}/help/*/{%{name},%{name}/figures}

%files lang
%{_datadir}/locale/*/*/*.mo

%changelog
