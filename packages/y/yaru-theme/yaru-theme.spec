#
# spec file for package yaru-theme
#
# Copyright (c) 2024 SUSE LLC
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


%define _name   yaru
Name:           yaru-theme
Version:        24.04.0
Release:        0
Summary:        Yaru theme from the Ubuntu community
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://community.ubuntu.com/c/desktop/theme-refresh
Source:         https://github.com/ubuntu/yaru/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.51
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This is the theme shaped by the community on the Ubuntu hub.

%package -n metatheme-yaru-common
Summary:        Common files for the Yaru Gtk Theme
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Recommends:     sound-theme-yaru
Recommends:     yaru-icon-theme
Suggests:       gtk2-metatheme-yaru
Suggests:       gtk3-metatheme-yaru

%description -n metatheme-yaru-common
This is the theme shaped by the community on the Ubuntu hub.

%package -n gnome-shell-theme-yaru
Summary:        Yaru GNOME shell themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       gnome-shell >= 46
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gnome-shell)

%description -n gnome-shell-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the GNOME Shell themes.

%package -n gtk2-metatheme-yaru
Summary:        GTK+ 2 support for the Yaru Gtk Theme
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       gtk2-engine-murrine
Requires:       gtk2-theming-engine-adwaita
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk2)

%description -n gtk2-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package provides the GTK+ 2 support for Yaru theme.

%package -n gtk3-metatheme-yaru
Summary:        GTK+ 3 support for the Yaru Gtk Theme
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       gtk3
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk3)

%description -n gtk3-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package provides the GTK+ 3 support for Yaru theme.

%package -n cinnamon-theme-yaru
Summary:        Yaru Cinnamon themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       cinnamon
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and cinnamon)

%description -n cinnamon-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the cinnamon themes.

%package -n xfwm4-theme-yaru
Summary:        Yaru Xfmw4 themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       metatheme-yaru-common = %{version}
Requires:       xfwm4
Supplements:    (metatheme-yaru-common and xfwm4)

%description -n xfwm4-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the Xfwm4 themes

%package -n metacity-theme-yaru
Summary:        Yaru Metacity themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
Requires:       metacity
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and metacity)

%description -n metacity-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the metacity themes.

%package -n gtksourceview-theme-yaru
Summary:        Yaru GtkSourceView themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only

%description -n gtksourceview-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the GtkSourceView theme.

%package -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA-4.0
Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme

%description -n yaru-icon-theme
This is the theme shaped by the community on the Ubuntu hub.

This package contains the icon theme.

%package -n sound-theme-yaru
Summary:        Yaru sound theme
License:        CC-BY-SA-4.0

%description -n sound-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the sound theme following the XDG theming
specification.

%prep
%setup -q -n %{_name}-%{version}

%build
%meson \
 -Dxfwm4=true \
 -Dcinnamon-shell=true
%meson_build

%install
%meson_install

rm %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
  %{buildroot}%{_datadir}/xsessions/Yaru-xorg.desktop \
  %{buildroot}%{_datadir}/wayland-sessions/Yaru.desktop \
  %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

%fdupes %{buildroot}%{_datadir}

%check

%define xfwm4_hidpi themes/Yaru*-*dpi/

%files -n metatheme-yaru-common
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/themes/Yaru*/
%exclude %{_datadir}/%{xfwm4_hidpi}
%exclude %{_datadir}/themes/Yaru*/gtk-?.*/
%exclude %{_datadir}/themes/Yaru*/xfwm4/
%exclude %{_datadir}/themes/Yaru*/metacity-1/
%exclude %{_datadir}/themes/Yaru*/cinnamon/
%exclude %{_datadir}/themes/Yaru*/gnome-shell

%files -n gnome-shell-theme-yaru
%dir %{_datadir}/themes/Yaru*/
%exclude %{_datadir}/%{xfwm4_hidpi}
%{_datadir}/themes/Yaru*/gnome-shell
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/theme/
%{_datadir}/gnome-shell/theme/Yaru*/
%dir %{_datadir}/gnome-shell/modes/
%{_datadir}/gnome-shell/modes/yaru.json

%files -n gtk2-metatheme-yaru
%dir %{_datadir}/themes/Yaru*/
%exclude %{_datadir}/%{xfwm4_hidpi}
%{_datadir}/themes/Yaru*/gtk-2.*/

%files -n gtk3-metatheme-yaru
%dir %{_datadir}/themes/Yaru*/
%exclude %{_datadir}/%{xfwm4_hidpi}
%{_datadir}/themes/Yaru*/gtk-3.*/

%files -n cinnamon-theme-yaru
%dir %{_datadir}/themes/Yaru*/
%exclude %{_datadir}/%{xfwm4_hidpi}
%{_datadir}/themes/Yaru*/cinnamon/

%files -n xfwm4-theme-yaru
%dir %{_datadir}/%{xfwm4_hidpi}
%dir %{_datadir}/themes/Yaru{,-dark}/
%{_datadir}/themes/Yaru*/xfwm4/

%files -n metacity-theme-yaru
%dir %{_datadir}/themes/Yaru{,-dark}/
%{_datadir}/themes/Yaru{,-dark}/metacity-1/

%files -n gtksourceview-theme-yaru
%{_datadir}/gtksourceview-*/
%{_datadir}/libgedit-gtksourceview-300/

%files -n yaru-icon-theme
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%ghost %{_datadir}/icons/Yaru/icon-theme.cache
%{_datadir}/icons/Yaru*/

%files -n sound-theme-yaru
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/sounds/Yaru/

%changelog
