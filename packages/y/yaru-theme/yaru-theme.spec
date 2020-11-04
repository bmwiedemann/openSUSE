#
# spec file for package yaru-theme
#
# Copyright (c) 2020 SUSE LLC
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
Version:        20.10.2
Release:        0
Summary:        Yaru theme from the Ubuntu community
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
URL:            https://community.ubuntu.com/c/desktop/theme-refresh
Source:         https://github.com/ubuntu/yaru/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This is the theme shaped by the community on the Ubuntu hub.

%package -n metatheme-yaru-common
Summary:        Common files for the Yaru Gtk Theme
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
Recommends:     sound-theme-yaru
Recommends:     yaru-icon-theme
Suggests:       gtk2-metatheme-yaru
Suggests:       gtk3-metatheme-yaru

%description -n metatheme-yaru-common
This is the theme shaped by the community on the Ubuntu hub.

%package -n gtk2-metatheme-yaru
Summary:        GTK+ 2 support for the Yaru Gtk Theme
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
Requires:       gtk2-engine-murrine
Requires:       gtk2-theming-engine-adwaita
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk2)

%description -n gtk2-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

%package -n gtk3-metatheme-yaru
Summary:        GTK+ 3 support for the Yaru Gtk Theme
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
Requires:       gtk3
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk3)

%description -n gtk3-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

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
%meson
%meson_build

%install
%meson_install

rm %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
  %{buildroot}%{_datadir}/xsessions/Yaru.desktop \
  %{buildroot}%{_datadir}/wayland-sessions/Yaru-wayland.desktop

%fdupes %{buildroot}%{_datadir}/themes/Yaru*/
%fdupes %{buildroot}%{_datadir}/gnome-shell/theme/Yaru*/
%fdupes %{buildroot}%{_datadir}/icons/Yaru/
%fdupes %{buildroot}%{_datadir}/sounds/Yaru/

%files -n metatheme-yaru-common
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/themes/Yaru/
%exclude %{_datadir}/themes/Yaru/gtk-?.*/
%{_datadir}/themes/Yaru-dark/
%exclude %{_datadir}/themes/Yaru-dark/gtk-?.*/
%{_datadir}/themes/Yaru-light/
%exclude %{_datadir}/themes/Yaru-light/gtk-?.*/
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/theme/
%{_datadir}/gnome-shell/theme/Yaru/
%{_datadir}/gnome-shell/theme/Yaru-dark/
%dir %{_datadir}/gnome-shell/modes/
%{_datadir}/gnome-shell/modes/yaru.json
%dir %{_datadir}/gnome-shell/extensions/
%dir %{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/
%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

%files -n gtk2-metatheme-yaru
%{_datadir}/themes/Yaru/gtk-2.*/
%{_datadir}/themes/Yaru-light/gtk-2.*/

%files -n gtk3-metatheme-yaru
%{_datadir}/themes/Yaru/gtk-3.*/
%{_datadir}/themes/Yaru-dark/gtk-3.*/
%{_datadir}/themes/Yaru-light/gtk-3.*/

%files -n yaru-icon-theme
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%ghost %{_datadir}/icons/Yaru/icon-theme.cache
%{_datadir}/icons/Yaru/

%files -n sound-theme-yaru
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/sounds/Yaru/

%changelog
