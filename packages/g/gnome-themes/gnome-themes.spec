#
# spec file for package gnome-themes
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


Name:           gnome-themes
Version:        3.0.0
Release:        0
Summary:        GNOME Themes
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/%{name}/3.0/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM gnome-themes-disable-engine-test.patch bgo#642970 fcrozat@novell.com -- don't check for gtk-engines-3 at build time
Patch0:         gnome-themes-disable-engine-test.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gtk3-devel
BuildRequires:  icon-naming-utils
BuildRequires:  intltool
BuildRequires:  translation-update-upstream
Recommends:     %{name}-lang
BuildArch:      noarch

%description
GNOME themes, including Ximian Industrial and selected background
images.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0 -p1

%build
#needed by patch0
autoreconf -fiv

%configure\
        --enable-all-themes
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
# remove themes which are now in gnome-themes-standard
rm -rf %{buildroot}%{_datadir}/themes/{HighContrast,HighContrast-SVG,HighContrastInverse}
rm -rf %{buildroot}%{_datadir}/icons/{HighContrast,HighContrast-SVG,HighContrastInverse}
%find_lang %{name} %{?no_lang_C}
%{icon_theme_cache_create_ghost Crux}
%{icon_theme_cache_create_ghost HighContrastLargePrint}
%{icon_theme_cache_create_ghost HighContrastLargePrintInverse}
%{icon_theme_cache_create_ghost LargePrint}
%{icon_theme_cache_create_ghost Mist}
%fdupes %{buildroot}%{_datadir}

%post
%icon_theme_cache_post Crux
%icon_theme_cache_post HighContrastLargePrint
%icon_theme_cache_post HighContrastLargePrintInverse
%icon_theme_cache_post LargePrint
%icon_theme_cache_post Mist

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%ghost %{_datadir}/icons/*/icon-theme.cache
%{_datadir}/icons/Crux/
%{_datadir}/icons/HighContrastLargePrint/
%{_datadir}/icons/HighContrastLargePrintInverse/
%{_datadir}/icons/LargePrint/
%{_datadir}/icons/Mist/
%{_datadir}/themes/Clearlooks/
%{_datadir}/themes/ClearlooksClassic/
%{_datadir}/themes/Crux/
%{_datadir}/themes/Glider/
%{_datadir}/themes/Glossy/
%{_datadir}/themes/HighContrastLargePrint/
%{_datadir}/themes/HighContrastLargePrintInverse/
%{_datadir}/themes/Inverted/
%{_datadir}/themes/LargePrint/
%{_datadir}/themes/LowContrast/
%{_datadir}/themes/LowContrastLargePrint/
%{_datadir}/themes/Mist/
%{_datadir}/themes/Simple/

%files lang -f %{name}.lang

%changelog
