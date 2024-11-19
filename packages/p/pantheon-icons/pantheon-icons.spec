#
# spec file for package pantheon-icons
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid io.elementary.icons
Name:           pantheon-icons
Version:        8.1.0
Release:        0
Summary:        A Tango-styled icon theme
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/icons
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.61.0
BuildRequires:  rsvg-convert
BuildRequires:  xcursorgen
BuildArch:      noarch
Provides:       elementary-icon-theme = %{version}
Obsoletes:      elementary-icon-theme < %{version}

%description
An original set of vector icons designed specifically for Pantheon.

%package        gimp-palette
Summary:        Copic Colors for The Gimp Palettes
Requires:       %{name} = %{version}
Supplements:    (gimp and %{name})

%description    gimp-palette
An original set of vector icons designed specifically for Pantheon.

This package contains a palette file for the GIMP.

%package        inkscape-palette
Summary:        Copic Colors for The Inkscape Palettes
Requires:       %{name} = %{version}
Requires:       inkscape
Supplements:    (inkscape and %{name})

%description    inkscape-palette
An original set of vector icons designed specifically for Pantheon.

This package contains a palette file for Inkscape.

%prep
%autosetup -n icons-%{version}

%build
%meson \
  -Dvolume_icons=false
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/icons/

%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_datadir}/icons/elementary
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files gimp-palette
%dir %{_datadir}/{gimp,gimp/2.0,gimp/2.0/palettes}
%{_datadir}/gimp/2.0/palettes/elementary.gpl

%files inkscape-palette
%dir %{_datadir}/{inkscape,inkscape/palettes}
%{_datadir}/inkscape/palettes/elementary.gpl

%changelog
