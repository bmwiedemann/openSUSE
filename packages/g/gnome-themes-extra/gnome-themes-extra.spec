#
# spec file for package gnome-themes-extra
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnome-themes-extra
Version:        3.28
Release:        0
Summary:        Extra GNOME Themes
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source:         http://download.gnome.org/sources/gnome-themes-extra/3.28/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  fdupes
# Needed to convert svg to gresource
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-2.0) >= 2.24.15
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.15
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.12
BuildRequires:  pkgconfig(librsvg-2.0)

%description
This packages contains extra GNOME themes from GNOME 3 and later.

%package -n metatheme-adwaita-common
Summary:        Common files for the Adwaita GNOME theme
Group:          System/GUI/GNOME
Suggests:       gtk2-metatheme-adwaita
Suggests:       gtk3-metatheme-adwaita
BuildArch:      noarch

%description -n metatheme-adwaita-common
Adwaita is the default GNOME theme in GNOME 3.

# Note: it's really a metatheme, and not just a gtk2 theme as we require metatheme-adwaita-common
%package -n gtk2-metatheme-adwaita
Summary:        GTK+ 2 support for the Adwaita GNOME theme
Group:          System/GUI/GNOME
# the theme is using the pixmap engine, shipped inside gtk2
Requires:       gtk2
Requires:       gtk2-theming-engine-adwaita = %{version}
Requires:       metatheme-adwaita-common = %{version}
Supplements:    packageand(metatheme-adwaita-common:gtk2)
BuildArch:      noarch

%description -n gtk2-metatheme-adwaita
Adwaita is the default GNOME theme in GNOME 3.

# Note: it's really a metatheme, and not just a gtk3 theme as we require metatheme-adwaita-common
%package -n gtk3-metatheme-adwaita
Summary:        GTK+ 3 support for the Adwaita GNOME theme
Group:          System/GUI/GNOME
Requires:       cantarell-fonts
Requires:       metatheme-adwaita-common = %{version}
Supplements:    packageand(metatheme-adwaita-common:gtk3)
BuildArch:      noarch

%description -n gtk3-metatheme-adwaita
Adwaita is the default GNOME theme in GNOME 3.

%package -n gtk2-theming-engine-adwaita
Summary:        Adwaita GTK+ Theming Engine
Group:          System/GUI/GNOME

%description -n gtk2-theming-engine-adwaita
Adwaita is the default GNOME theme in GNOME 3.

%package -n gnome-themes-accessibility
Summary:        Accessibility GNOME Themes
Group:          System/GUI/GNOME
Conflicts:      gnome-themes < 3.0.0
BuildArch:      noarch

%description -n gnome-themes-accessibility
This package contains high-contrast and low-contrast themes for GNOME.

%package -n gnome-themes-accessibility-gtk2
Summary:        Accessibility GNOME Themes
Group:          System/GUI/GNOME
Requires:       gtk2-engine-hcengine
Supplements:    packageand(gnome-themes-accessibility:gtk2)
BuildArch:      noarch

%description -n gnome-themes-accessibility-gtk2
This package contains high-contrast and low-contrast themes for gtk2 applications.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%{icon_theme_cache_create_ghost HighContrast}
%fdupes %{buildroot}%{_datadir}/icons/Adwaita/cursors/
%fdupes %{buildroot}%{_datadir}/icons/HighContrast/
%fdupes %{buildroot}%{_datadir}/themes/

%post -n gnome-themes-accessibility
%icon_theme_cache_post HighContrast

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore

%files -n metatheme-adwaita-common
%license LICENSE
%doc NEWS
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/Adwaita-dark
%{_datadir}/themes/Adwaita-dark/index.theme

%files -n gtk2-metatheme-adwaita
%{_datadir}/themes/Adwaita/gtk-2.0/
%{_datadir}/themes/Adwaita-dark/gtk-2.0/

%files -n gtk3-metatheme-adwaita
%{_datadir}/themes/Adwaita/gtk-3.0/
%dir %{_datadir}/themes/Adwaita-dark/gtk-3.0
%{_datadir}/themes/Adwaita-dark/gtk-3.0/gtk.css

%files -n gtk2-theming-engine-adwaita
%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so

%files -n gnome-themes-accessibility
%ghost %{_datadir}/icons/HighContrast/icon-theme.cache
%{_datadir}/icons/HighContrast/
%dir %{_datadir}/themes/HighContrast/
%{_datadir}/themes/HighContrast/index.theme
%{_datadir}/themes/HighContrast/gtk-3.0/

%files -n gnome-themes-accessibility-gtk2
%{_datadir}/themes/HighContrast/gtk-2.0/

%changelog
