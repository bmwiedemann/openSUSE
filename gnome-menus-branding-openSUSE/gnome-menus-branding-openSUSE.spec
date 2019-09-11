#
# spec file for package gnome-menus-branding-openSUSE
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         build_openSUSE 1
%define         build_SLED 0
%define gnome_menus_version %(rpm -q --qf '%%{version}' gnome-menus)
# Do not edit this auto generated file! Edit gnome-menus-branding.spec.in.
Name:           gnome-menus-branding-openSUSE
Version:        42.1
Release:        0
Summary:        The GNOME Desktop Menu -- openSUSE Menus Definitions
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source:         gnome-menus-branding-COPYING
# PATCH-FIX-OPENSUSE gnome-menus-branding-remove-X-SuSE-ControlCenter.patch vuntz@opensuse.org -- Remove the desktop files with X-SuSE-YaST category from the Applications menu and explicitly add YaST launcher
Patch0:         gnome-menus-branding-remove-X-SuSE-ControlCenter.patch
BuildRequires:  gnome-menus
# To be in sync with upstream defaults, do branding as a patch for upstream file.
# WARNING: As this package conflicts with gnome-menus-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  gnome-menus-branding-upstream
Requires:       gnome-menus = %{gnome_menus_version}
Supplements:    packageand(gnome-menus:branding-openSUSE)
Conflicts:      gnome-menus-branding
Provides:       gnome-menus-branding = %{gnome_menus_version}
BuildArch:      noarch

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

http://www.freedesktop.org/Standards/menu-spec

This package provides the openSUSE definitions for menus.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} COPYING
# We will base menus on upstream menus:
cp -a %{_sysconfdir}/xdg/menus/*.menu .
%patch0

%build

%install
install -d %{buildroot}%{_sysconfdir}/xdg/menus
install -m0644 *.menu %{buildroot}%{_sysconfdir}/xdg/menus/

%files
%license COPYING

%{_sysconfdir}/xdg/menus/gnome-applications.menu

%changelog
