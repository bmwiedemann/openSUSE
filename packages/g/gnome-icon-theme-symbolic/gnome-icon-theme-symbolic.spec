#
# spec file for package gnome-icon-theme-symbolic
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gnome-icon-theme-symbolic
Version:        3.12.0
Release:        0
# FIXME: when we have icon-naming-utils > 0.8.90, we will have icontool-render, so check if something has to be changed.
Summary:        Symbolic icon theme for GNOME
License:        CC-BY-SA-3.0
Group:          System/X11/Icons
Url:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/gnome-icon-theme-symbolic/3.12/%{name}-%{version}.tar.xz
BuildRequires:  gnome-icon-theme
# This is just for gtk-update-icon-cache
BuildRequires:  gtk3-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
# The icon-naming-utils we have doesn't have icontool-render yet,
# so inkscape is not needed either
#BuildRequires:  inkscape
BuildRequires:  pkg-config
Requires:       gnome-icon-theme
Supplements:    gnome-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The purpose of this icon theme is to extend the base icon theme that
follows the Tango style guidelines for specific purposes. This would
include OSD messages, panel system/notification area, and possibly
menu icons.

Icons follow the naming specification, but have a -symbolic suffix, so
only applications specifically looking up these symbolic icons will
render them. If a -symbolic icon is missing, the app will fall back to
the regular name.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%clean
rm -rf %{buildroot}

%post
%icon_theme_cache_post gnome

%postun
%icon_theme_cache_postun gnome

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_datadir}/icons/gnome/scalable/*/*-symbolic.svg
%{_datadir}/pkgconfig/gnome-icon-theme-symbolic.pc

%changelog
