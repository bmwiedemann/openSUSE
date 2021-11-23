#
# spec file for package ubuntu-mate-artwork
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   ubuntu-mate
Name:           ubuntu-mate-artwork
Version:        22.04.0
Release:        0
Summary:        Ubuntu MATE themes and artwork
License:        CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/ubuntu-mate/ubuntu-mate-artwork
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch

%description
This package contains Ubuntu MATE themes and artwork.

%package -n metatheme-yaru-mate-common
Summary:        Common files for the Yaru-MATE Gtk Themes
Group:          System/GUI/Other
Recommends:     %{_name}-icon-theme
Suggests:       gtk2-metatheme-yaru-mate
Suggests:       gtk3-metatheme-yaru-mate

%description -n metatheme-yaru-mate-common
Includes the Yaru-MATE themes.

Introduced as the default theme in Ubuntu MATE 21.04.

%package -n metatheme-ambiant-mate-common
Summary:        Common files for the Ambiant-MATE Gtk Theme
Group:          System/GUI/Other
Recommends:     %{_name}-icon-theme
Suggests:       dmz-icon-theme-cursors
Suggests:       gtk2-metatheme-ambiant-mate
Suggests:       gtk3-metatheme-ambiant-mate

%description -n metatheme-ambiant-mate-common
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n metatheme-radiant-mate-common
Summary:        Common files for the Radiant-MATE Gtk Theme
Group:          System/GUI/Other
Recommends:     %{_name}-icon-theme
Suggests:       gtk2-metatheme-radiant-mate
Suggests:       gtk3-metatheme-radiant-mate

%description -n metatheme-radiant-mate-common
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

%package -n gtk2-metatheme-yaru-mate
Summary:        GTK+ 2 support for the Yaru-MATE Gtk Themes
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-yaru-mate-common = %{version}
Supplements:    (metatheme-yaru-mate-common and gtk2)

%description -n gtk2-metatheme-yaru-mate
Includes the Yaru-MATE themes.

Introduced as the default theme in Ubuntu MATE 21.04.

%package -n gtk2-metatheme-ambiant-mate
Summary:        GTK+ 2 support for the Ambiant-MATE Gtk Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-ambiant-mate-common = %{version}
Supplements:    (metatheme-ambiant-mate-common and gtk2)

%description -n gtk2-metatheme-ambiant-mate
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n gtk2-metatheme-radiant-mate
Summary:        GTK+ 2 support for the Radiant-MATE Gtk Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-radiant-mate-common = %{version}
Supplements:    (metatheme-radiant-mate-common and gtk2)

%description -n gtk2-metatheme-radiant-mate
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

%package -n gtk3-metatheme-yaru-mate
Summary:        GTK+ 3 support for the Yaru-MATE Gtk Themes
Group:          System/GUI/Other
Requires:       metatheme-yaru-mate-common = %{version}
Supplements:    (metatheme-yaru-mate-common and gtk3)

%description -n gtk3-metatheme-yaru-mate
Includes the Yaru-MATE themes.

Introduced as the default theme in Ubuntu MATE 21.04.

%package -n gtk3-metatheme-ambiant-mate
Summary:        GTK+ 3 support for the Ambiant-MATE Gtk Theme
Group:          System/GUI/Other
Requires:       metatheme-ambiant-mate-common = %{version}
Supplements:    (metatheme-ambiant-mate-common and gtk3)

%description -n gtk3-metatheme-ambiant-mate
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n gtk3-metatheme-radiant-mate
Summary:        GTK+ 3 support for the Radiant-MATE Gtk Theme
Group:          System/GUI/Other
Requires:       metatheme-radiant-mate-common = %{version}
Supplements:    (metatheme-radiant-mate-common and gtk3)

%description -n gtk3-metatheme-radiant-mate
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

%package -n gtk4-metatheme-yaru-mate
Summary:        GTK+ 4 support for the Yaru-MATE Gtk Themes
Group:          System/GUI/Other
Requires:       metatheme-yaru-mate-common = %{version}
Supplements:    (metatheme-yaru-mate-common and gtk4)

%description -n gtk4-metatheme-yaru-mate
Includes the Yaru-MATE themes.

Introduced as the default theme in Ubuntu MATE 21.04.

%package -n %{_name}-icon-theme
Summary:        Icon themes from Ubuntu MATE
Group:          System/X11/Icons
Requires:       humanity-icon-theme
Requires:       ubuntu-mono-icon-theme

%description -n %{_name}-icon-theme
This package contains icon themes from Ubuntu MATE.

%package -n %{_name}-wallpapers
Summary:        Wallpaper and background images from Ubuntu MATE
Group:          System/GUI/Other

%description -n %{_name}-wallpapers
The default Ubuntu MATE wallpapers for the Ubuntu MATE releases.

%prep
%autosetup -n %{name}
# Remove unwanted: the Debian package, Plymouth theme, LightDM defaults.
rm -r debian/ .%{_sysconfdir} .%{_datadir}/ubuntu-mate/ .%{_datadir}/plymouth/
rm link-battery.sh

%build
# Nothing to build.

%install
cp -a --no-preserve=mode * %{buildroot}/
rm %{buildroot}/COPYING
for icons in Yaru-MATE-dark Yaru-MATE-light Ambiant-MATE Radiant-MATE; do
    # %%icon_theme_cache_create_ghost fails to work.
    touch %{buildroot}%{_datadir}/icons/$icons/icon-theme.cache
done
%fdupes %{buildroot}/%{_prefix}

%files -n metatheme-yaru-mate-common
%license COPYING
%{_datadir}/themes/Yaru-MATE-dark/
%exclude %{_datadir}/themes/Yaru-MATE-dark/gtk-2.*/
%exclude %{_datadir}/themes/Yaru-MATE-dark/gtk-3.*/
%exclude %{_datadir}/themes/Yaru-MATE-dark/gtk-4.*/
%{_datadir}/themes/Yaru-MATE-light/
%exclude %{_datadir}/themes/Yaru-MATE-light/gtk-2.*/
%exclude %{_datadir}/themes/Yaru-MATE-light/gtk-3.*/
%exclude %{_datadir}/themes/Yaru-MATE-light/gtk-4.*/
%dir %{_datadir}/gtksourceview-*/
%dir %{_datadir}/gtksourceview-*/styles/
%{_datadir}/gtksourceview-*/styles/Yaru-MATE-dark*.xml
%{_datadir}/gtksourceview-*/styles/Yaru-MATE-light*.xml

%files -n metatheme-ambiant-mate-common
%license COPYING
%{_datadir}/themes/Ambiant-MATE*/
%exclude %{_datadir}/themes/Ambiant-MATE*/gtk-2.*/
%exclude %{_datadir}/themes/Ambiant-MATE*/gtk-3.*/
%dir %{_datadir}/gtksourceview-*/
%dir %{_datadir}/gtksourceview-*/styles/
%{_datadir}/gtksourceview-*/styles/Ambiant-MATE*.xml

%files -n metatheme-radiant-mate-common
%license COPYING
%{_datadir}/themes/Radiant-MATE/
%exclude %{_datadir}/themes/Radiant-MATE/gtk-2.*/
%exclude %{_datadir}/themes/Radiant-MATE/gtk-3.*/
%dir %{_datadir}/gtksourceview-*/
%dir %{_datadir}/gtksourceview-*/styles/
%{_datadir}/gtksourceview-*/styles/Radiant-MATE.xml

%files -n gtk2-metatheme-yaru-mate
%{_datadir}/themes/Yaru-MATE-dark/gtk-2.*/
%{_datadir}/themes/Yaru-MATE-light/gtk-2.*/

%files -n gtk2-metatheme-ambiant-mate
%{_datadir}/themes/Ambiant-MATE*/gtk-2.*/

%files -n gtk2-metatheme-radiant-mate
%{_datadir}/themes/Radiant-MATE/gtk-2.*/

%files -n gtk3-metatheme-yaru-mate
%{_datadir}/themes/Yaru-MATE-dark/gtk-3.*/
%{_datadir}/themes/Yaru-MATE-light/gtk-3.*/

%files -n gtk3-metatheme-ambiant-mate
%{_datadir}/themes/Ambiant-MATE*/gtk-3.*/

%files -n gtk3-metatheme-radiant-mate
%{_datadir}/themes/Radiant-MATE/gtk-3.*/

%files -n gtk4-metatheme-yaru-mate
%{_datadir}/themes/Yaru-MATE-dark/gtk-4.*/
%{_datadir}/themes/Yaru-MATE-light/gtk-4.*/

%files -n %{_name}-icon-theme
%license COPYING
%ghost %{_datadir}/icons/*/icon-theme.cache
%{_datadir}/icons/*/

%files -n %{_name}-wallpapers
%license COPYING
%{_datadir}/backgrounds/
%{_datadir}/mate-background-properties/

%changelog
