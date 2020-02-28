#
# spec file for package ubuntu-mate-artwork
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


%define _name   ubuntu-mate
Name:           ubuntu-mate-artwork
Version:        20.04.0
Release:        0
Summary:        Ubuntu MATE themes and artwork
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND CC-BY-SA-3.0
Group:          System/GUI/Other
URL:            https://github.com/ubuntu-mate/ubuntu-mate-artwork
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildArch:      noarch

%description
This package contains Ubuntu MATE themes and artwork.

%package -n metatheme-ambiant-mate-common
Summary:        Ambiant-MATE Gtk Theme -- Common Files
Group:          System/GUI/Other
Recommends:     %{_name}-icon-theme
Suggests:       dmz-icon-theme-cursors
Suggests:       gtk2-metatheme-ambiant-mate
Suggests:       gtk3-metatheme-ambiant-mate

%description -n metatheme-ambiant-mate-common
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n metatheme-radiant-mate-common
Summary:        Radiant-MATE Gtk Theme -- Common Files
Group:          System/GUI/Other
Recommends:     %{_name}-icon-theme
Suggests:       gtk2-metatheme-radiant-mate
Suggests:       gtk3-metatheme-radiant-mate

%description -n metatheme-radiant-mate-common
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

%package -n gtk2-metatheme-ambiant-mate
Summary:        Ambiant-MATE Gtk Theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-ambiant-mate-common = %{version}
Supplements:    (metatheme-ambiant-mate-common and gtk2)

%description -n gtk2-metatheme-ambiant-mate
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n gtk2-metatheme-radiant-mate
Summary:        Radiant-MATE Gtk Theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-radiant-mate-common = %{version}
Supplements:    (metatheme-radiant-mate-common and gtk2)

%description -n gtk2-metatheme-radiant-mate
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

%package -n gtk3-metatheme-ambiant-mate
Summary:        Ambiant-MATE Gtk Theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       metatheme-ambiant-mate-common = %{version}
Supplements:    (metatheme-ambiant-mate-common and gtk3)

%description -n gtk3-metatheme-ambiant-mate
Includes an Ambiant-MATE light-on-dark theme.

Introduced as the default theme in Ubuntu MATE 15.04.

%package -n gtk3-metatheme-radiant-mate
Summary:        Radiant-MATE Gtk Theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       metatheme-radiant-mate-common = %{version}
Supplements:    (metatheme-radiant-mate-common and gtk3)

%description -n gtk3-metatheme-radiant-mate
Includes an Radiant-MATE dark-on-light theme.

Introduced as one of the defaults in Ubuntu MATE 15.04.

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
%setup -q -n %{name}
# Remove unwanted: the Debian package, Plymouth theme, LightDM defaults.
rm -r debian/ .%{_sysconfdir} .%{_datadir}/ubuntu-mate/ .%{_datadir}/plymouth/
rm link-battery.sh

%build
# Nothing to build.

%install
cp -a --no-preserve=mode * %{buildroot}/
rm %{buildroot}/COPYING
for icons in Ambiant-MATE Radiant-MATE; do
    # %%icon_theme_cache_create_ghost fails to work.
    touch %{buildroot}%{_datadir}/icons/$icons/icon-theme.cache
done
%fdupes %{buildroot}/

%files -n metatheme-ambiant-mate-common
%license COPYING
%{_datadir}/themes/Ambiant-MATE*/
%exclude %{_datadir}/themes/Ambiant-MATE*/gtk-?.*/
%dir %{_datadir}/gtksourceview-?.0/
%dir %{_datadir}/gtksourceview-?.0/styles/
%{_datadir}/gtksourceview-?.0/styles/Ambiant-MATE*.xml

%files -n metatheme-radiant-mate-common
%license COPYING
%{_datadir}/themes/Radiant-MATE/
%exclude %{_datadir}/themes/Radiant-MATE/gtk-?.*/
%dir %{_datadir}/gtksourceview-?.0/
%dir %{_datadir}/gtksourceview-?.0/styles/
%{_datadir}/gtksourceview-?.0/styles/Radiant-MATE.xml

%files -n gtk2-metatheme-ambiant-mate
%{_datadir}/themes/Ambiant-MATE*/gtk-2.*/

%files -n gtk2-metatheme-radiant-mate
%{_datadir}/themes/Radiant-MATE/gtk-2.*/

%files -n gtk3-metatheme-ambiant-mate
%{_datadir}/themes/Ambiant-MATE*/gtk-3.*/

%files -n gtk3-metatheme-radiant-mate
%{_datadir}/themes/Radiant-MATE/gtk-3.*/

%files -n %{_name}-icon-theme
%license COPYING
%ghost %{_datadir}/icons/*/icon-theme.cache
%{_datadir}/icons/*/

%files -n %{_name}-wallpapers
%license COPYING
%{_datadir}/backgrounds/
%{_datadir}/mate-background-properties/

%changelog
