#
# spec file for package gtk2-metatheme-sonar
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


%define _icon_version 11.3.1
Name:           gtk2-metatheme-sonar
Version:        11.3.0
Release:        0
Summary:        GTK+, Xfwm4 and Metacity Sonar Theme
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Source0:        metatheme-Sonar-%{version}.tar.bz2
Source1:        icon-theme-sonar-%{_icon_version}.tar.bz2
Source2:        COPYING.Sonar
Source3:        Sonar-xfwm4.tar.bz2
# PATCH-FIX-OPENSUSE metatheme-Sonar_compatibilty-with-murrine-0.98.patch badshah400@gmail.com -- Remove deprecated gradients options, (deprecated with murrine version 0.98). Sent upstream by mail
Patch0:         metatheme-Sonar_compatibilty-with-murrine-0.98.patch
# PATCH-FIX-UPSTREAM gtk2-metatheme-sonar-main-menu-theming.patch bnc#642956 vuntz@opensuse.org -- Correctly match the main menu button for correct theming
Patch1:         gtk2-metatheme-sonar-main-menu-theming.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils
BuildRequires:  pkgconfig
Requires:       gtk2-engine-murrine
Requires:       metatheme-sonar-common = %{version}
Enhances:       gtk2
BuildArch:      noarch

%description
GTK+, Xfwm4 and Metacity theme created for openSUSE 11.2.

%package -n metatheme-sonar-common
Summary:        GTK+, Xfwm4 and Metacity Sonar Theme -- Common Files
Group:          System/GUI/GNOME
Recommends:     sonar-icon-theme
Suggests:       gtk2-metatheme-sonar

%description -n metatheme-sonar-common
GTK+, Xfwm4 and Metacity theme created for openSUSE 11.2.

%package -n sonar-icon-theme
Version:        %{_icon_version}
Release:        0
Summary:        Sonar Icon Theme
Group:          System/GUI/GNOME
Requires:       hicolor-icon-theme
Suggests:       gtk2-metatheme-sonar
# Needed for old not-in-factory package
Provides:       icon-theme-sonar = 11.2.0
Obsoletes:      icon-theme-sonar < 11.2.0

%description -n sonar-icon-theme
Sonar icon theme based on the upcoming GNOME icon theme.

%prep
%setup -q -a1 -a3 -n Sonar
cp -a %{SOURCE2} COPYING.xfwm4
%patch0 -p1
%patch1 -p1

%build
pushd icon-theme-sonar-%{_icon_version}
%configure
make %{?_smp_mflags}
popd

%install
mkdir -p %{buildroot}%{_datadir}/themes/Sonar
cp -a Sonar/xfwm4 gtk-2.0 metacity-1 index.theme %{buildroot}%{_datadir}/themes/Sonar/
# install icons
pushd icon-theme-sonar-%{_icon_version}
%make_install
popd
%{icon_theme_cache_create_ghost Sonar}
%fdupes %{buildroot}

%post -n sonar-icon-theme
%icon_theme_cache_post Sonar

# No need for %%icon_theme_cache_postun in %postun since the theme won't exist anymore

%files
%{_datadir}/themes/Sonar/gtk-2.0/

%files -n metatheme-sonar-common
%doc AUTHORS
%license COPYING.xfwm4
%dir %{_datadir}/themes/Sonar
%{_datadir}/themes/Sonar/index.theme
%{_datadir}/themes/Sonar/metacity-1/
%{_datadir}/themes/Sonar/xfwm4/

%files -n sonar-icon-theme
%defattr (644, root, root, 755)
%license icon-theme-sonar-%{_icon_version}/COPYING
%doc icon-theme-sonar-%{_icon_version}/AUTHORS icon-theme-sonar-%{_icon_version}/NEWS icon-theme-sonar-%{_icon_version}/README
%ghost %{_datadir}/icons/Sonar/icon-theme.cache
%{_datadir}/icons/Sonar/

%changelog
