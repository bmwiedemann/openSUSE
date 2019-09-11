#
# spec file for package elementary-icon-theme
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


Name:           elementary-icon-theme
Version:        5.0.4
Release:        0
Summary:        A Tango-styled icon theme
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://elementary.io/
Source:         https://github.com/elementary/icons/archive/%{version}.tar.gz#/icons-%{version}.tar.gz
# PATCH-FIX-UPSTREAM elementary-icon-theme-chmod.patch mailaender@opensuse.org -- https://github.com/elementary/icons/pull/130
Patch0:         elementary-icon-theme-chmod.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
Suggests:       %{name}-gimp-palette
Suggests:       %{name}-inkscape-palette
BuildArch:      noarch

%description
An original set of vector icons designed specifically for Elementary
OS and its desktop environment, Pantheon.

%package        gimp-palette
Summary:        Copic Colors for The Gimp Palettes
Requires:       %{name} = %{version}
Requires:       gimp

%description    gimp-palette
An original set of vector icons designed specifically for Elementary
OS and its desktop environment, Pantheon.

This package contains a palette file for the GIMP.

%package        inkscape-palette
Summary:        Copic Colors for The Inkscape Palettes
Requires:       %{name} = %{version}
Requires:       inkscape

%description    inkscape-palette
An original set of vector icons designed specifically for Elementary
OS and its desktop environment, Pantheon.

This package contains a palette file for inkscape.

%prep
%setup -q -n icons-%{version}
%patch0 -p1

%build
%meson \
	-Dvolume_icons=false
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/icons/
%{icon_theme_cache_create_ghost elementary}

%post
%icon_theme_cache_post elementary

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore.

%files
%defattr(0644,root,root,0755)
%license COPYING
%doc AUTHORS CONTRIBUTING.md README.md
%{_datadir}/icons/elementary/
%ghost %{_datadir}/icons/elementary/icon-theme.cache

%files gimp-palette
%defattr(0644,root,root,0755)
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.0
%dir %{_datadir}/gimp/2.0/palettes
%{_datadir}/gimp/2.0/palettes/elementary.gpl

%files inkscape-palette
%defattr(0644,root,root,0755)
%dir %{_datadir}/inkscape
%dir %{_datadir}/inkscape/palettes
%{_datadir}/inkscape/palettes/elementary.gpl

%changelog
