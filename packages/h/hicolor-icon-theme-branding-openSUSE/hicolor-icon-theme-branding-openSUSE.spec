#
# spec file for package hicolor-icon-theme-branding-openSUSE
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


%define         build_openSUSE 1
%define         build_SLED 0
%define hicolor_icon_theme_version %(rpm -q --qf '%%{version}' hicolor-icon-theme)
# Do not edit this auto generated file! Edit hicolor-icon-theme-branding.spec.in.
Name:           hicolor-icon-theme-branding-openSUSE
Version:        42.1
Release:        0
Summary:        Fallback Icon Theme -- openSUSE Icons
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:        suse-icon.tar.bz2
Source1:        COPYING
BuildRequires:  hicolor-icon-theme
Requires:       hicolor-icon-theme = %{hicolor_icon_theme_version}
Supplements:    packageand(hicolor-icon-theme:branding-openSUSE)
Conflicts:      hicolor-icon-theme-branding
Provides:       hicolor-icon-theme-branding = %{hicolor_icon_theme_version}
BuildArch:      noarch

%description
This is the default fallback theme used by implementations of the icon
theme specification.

This package provides openSUSE icons for hicolor-icon-theme.

%prep
%setup -q -c %{name}-%{version}
cp -a %{SOURCE1} .

%build

%install
for size in 16 22 32 48; do
  install -D -m 0644 suse${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/distributor.png
done
install -D -m 0644 suse.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/distributor.svg

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%license COPYING
%{_datadir}/icons/hicolor/*/*/*.*

%changelog
