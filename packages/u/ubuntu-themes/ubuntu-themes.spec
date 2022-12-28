#
# spec file for package ubuntu-themes
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


Name:           ubuntu-themes
Version:        20.10
Release:        0
Summary:        Eyecandy from Ubuntu
License:        GPL-3.0-or-later
URL:            https://launchpad.net/ubuntu-themes
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-xml

%description
Ubuntu GNU/Linux basic artwork.

%package -n metatheme-ambiance-common
Summary:        Ambiance Gtk Theme -- Common Files
Recommends:     humanity-icon-theme
Recommends:     ubuntu-mono-icon-theme
Suggests:       gtk2-metatheme-ambiance
Suggests:       gtk3-metatheme-ambiance

%description -n metatheme-ambiance-common
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n metatheme-radiance-common
Summary:        Radiance Gtk Theme -- Common Files
Recommends:     humanity-icon-theme
Recommends:     ubuntu-mono-icon-theme
Suggests:       gtk2-metatheme-radiance
Suggests:       gtk3-metatheme-radiance

%description -n metatheme-radiance-common
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n gtk2-metatheme-ambiance
Summary:        Ambiance Gtk Theme -- GTK+ 2 Support
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-ambiance-common = %{version}
Supplements:    (metatheme-ambiance-common and gtk2)

%description -n gtk2-metatheme-ambiance
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n gtk2-metatheme-radiance
Summary:        Radiance Gtk Theme -- GTK+ 2 Support
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-radiance-common = %{version}
Supplements:    (metatheme-radiance-common and gtk2)

%description -n gtk2-metatheme-radiance
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n gtk3-metatheme-ambiance
Summary:        Ambiance Gtk Theme -- GTK+ 3 Support
Requires:       gtk3
Requires:       metatheme-ambiance-common = %{version}
Supplements:    (metatheme-ambiance-common and gtk3)

%description -n gtk3-metatheme-ambiance
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n gtk3-metatheme-radiance
Summary:        Radiance Gtk Theme -- GTK+ 3 Support
Requires:       metatheme-radiance-common = %{version}
Supplements:    (metatheme-radiance-common and gtk3)

%description -n gtk3-metatheme-radiance
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n ubuntu-mono-icon-theme
Summary:        Ubuntu Mono Icon theme
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme
Provides:       ubuntu-mono = %{version}

%description -n ubuntu-mono-icon-theme
Dark and Light panel icons to make desktop beautiful.

%prep
%setup -q

sed -i '1s|^#!.*$|#!%{_bindir}/python3|' *.py

%build
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/themes/ %{buildroot}%{_datadir}/icons/
for theme in Ambiance Radiance; do
    cp -a $theme %{buildroot}%{_datadir}/themes/$theme
done
for i in ubuntu-mono-dark ubuntu-mono-light LoginIcons; do
    mkdir -p %{buildroot}%{_datadir}/icons/$i
    for d in $(find $i -type d); do
      mkdir -p %{buildroot}%{_datadir}/icons/${d}
    done
    for icon in $(find $i -type f); do
      real_icon=$(readlink -f $icon)
      cp -r ${real_icon} %{buildroot}%{_datadir}/icons/${icon}
    done
done
%icon_theme_cache_create_ghost ubuntu-mono-dark
%icon_theme_cache_create_ghost ubuntu-mono-light
%icon_theme_cache_create_ghost LoginIcons
%fdupes %{buildroot}%{_datadir}/themes/Ambiance/
%fdupes %{buildroot}%{_datadir}/themes/Radiance/
%fdupes %{buildroot}%{_datadir}/icons/

%files -n metatheme-ambiance-common
%license COPYING
%{_datadir}/themes/Ambiance/
%exclude %{_datadir}/themes/Ambiance/gtk-?.*/

%files -n metatheme-radiance-common
%license COPYING
%{_datadir}/themes/Radiance/
%exclude %{_datadir}/themes/Radiance/gtk-?.*/

%files -n gtk2-metatheme-ambiance
%{_datadir}/themes/Ambiance/gtk-2.*/

%files -n gtk2-metatheme-radiance
%{_datadir}/themes/Radiance/gtk-2.*/

%files -n gtk3-metatheme-ambiance
%{_datadir}/themes/Ambiance/gtk-3.*/

%files -n gtk3-metatheme-radiance
%{_datadir}/themes/Radiance/gtk-3.*/

%files -n ubuntu-mono-icon-theme
%license COPYING
%ghost %{_datadir}/icons/ubuntu-mono-dark/icon-theme.cache
%ghost %{_datadir}/icons/ubuntu-mono-light/icon-theme.cache
%ghost %{_datadir}/icons/LoginIcons/icon-theme.cache
%{_datadir}/icons/ubuntu-mono-dark
%{_datadir}/icons/ubuntu-mono-light
%{_datadir}/icons/LoginIcons/

%changelog
