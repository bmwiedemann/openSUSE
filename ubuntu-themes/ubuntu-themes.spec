#
# spec file for package ubuntu-themes
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


%define _version 16.10+18.04.20180122.1
Name:           ubuntu-themes
Version:        16.10~bzr20180122
Release:        0
Summary:        Eyecandy from Ubuntu
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Url:            https://launchpad.net/ubuntu-themes
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
BuildRequires:  python2-xml
%else
BuildRequires:  python
BuildRequires:  python-xml
%endif

%description
Ubuntu GNU/Linux basic artwork.

%package -n metatheme-ambiance-common
Summary:        Ambiance Gtk Theme -- Common Files
Group:          System/GUI/Other
Recommends:     humanity-icon-theme
Recommends:     ubuntu-mono-icon-theme
Suggests:       gtk2-metatheme-ambiance
Suggests:       gtk3-metatheme-ambiance

%description -n metatheme-ambiance-common
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n metatheme-radiance-common
Summary:        Radiance Gtk Theme -- Common Files
Group:          System/GUI/Other
Recommends:     humanity-icon-theme
Recommends:     ubuntu-mono-icon-theme
Suggests:       gtk2-metatheme-radiance
Suggests:       gtk3-metatheme-radiance

%description -n metatheme-radiance-common
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n gtk2-metatheme-ambiance
Summary:        Ambiance Gtk Theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-ambiance-common = %{version}
Supplements:    packageand(metatheme-ambiance-common:gtk2)

%description -n gtk2-metatheme-ambiance
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n gtk2-metatheme-radiance
Summary:        Radiance Gtk Theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.90.3
Requires:       metatheme-radiance-common = %{version}
Supplements:    packageand(metatheme-radiance-common:gtk2)

%description -n gtk2-metatheme-radiance
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n gtk3-metatheme-ambiance
Summary:        Ambiance Gtk Theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       gtk3
Requires:       metatheme-ambiance-common = %{version}
Supplements:    packageand(metatheme-ambiance-common:gtk3)

%description -n gtk3-metatheme-ambiance
Includes an Ambiance light-on-dark theme.

Introduced as the default theme in Ubuntu 10.04 LTS.

%package -n gtk3-metatheme-radiance
Summary:        Radiance Gtk Theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       metatheme-radiance-common = %{version}
Supplements:    packageand(metatheme-radiance-common:gtk3)

%description -n gtk3-metatheme-radiance
Includes an Radiance dark-on-light theme.

Introduced as one of the defaults in Ubuntu 10.04 LTS.

%package -n ubuntu-mono-icon-theme
Summary:        Ubuntu Mono Icon theme
Group:          System/X11/Icons
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme
Provides:       ubuntu-mono = %{version}

%description -n ubuntu-mono-icon-theme
Dark and Light panel icons to make desktop beautiful.

%prep
%setup -q -c
sed -i '1s|^#!.*$|#!%{_bindir}/python2|' *.py

%build
make %{?_smp_mflags} V=1

%install
mkdir -p %{buildroot}%{_datadir}/themes/ %{buildroot}%{_datadir}/icons/
for theme in Ambiance Radiance; do
    cp -a $theme %{buildroot}%{_datadir}/themes/$theme
done
for icons in ubuntu-mono-dark ubuntu-mono-light LoginIcons; do
    cp -a $icons %{buildroot}%{_datadir}/icons/$icons
    # %%icon_theme_cache_create_ghost fails to work here.
    touch %{buildroot}%{_datadir}/icons/$icons/icon-theme.cache
done
%fdupes %{buildroot}%{_datadir}/themes/Ambiance/
%fdupes %{buildroot}%{_datadir}/themes/Radiance/
%fdupes %{buildroot}%{_datadir}/icons/

%if 0%{?suse_version} < 1500
%post -n ubuntu-mono-icon-theme
%icon_theme_cache_post ubuntu-mono-dark
%icon_theme_cache_post ubuntu-mono-light
%icon_theme_cache_post LoginIcons

# No need for %%icon_theme_cache_postun in %%postun since themes won't exist anymore.
%endif

%files -n metatheme-ambiance-common
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{_datadir}/themes/Ambiance/
%exclude %{_datadir}/themes/Ambiance/gtk-?.*/

%files -n metatheme-radiance-common
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
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
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%ghost %{_datadir}/icons/ubuntu-mono-*/icon-theme.cache
%ghost %{_datadir}/icons/LoginIcons/icon-theme.cache
%{_datadir}/icons/ubuntu-mono*/
%{_datadir}/icons/LoginIcons/

%changelog
