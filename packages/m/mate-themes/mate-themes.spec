#
# spec file for package mate-themes
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


# TODO: Split up packages into individual themes.
Name:           mate-themes
Version:        3.22.23
Release:        0
Summary:        Themes for the MATE desktop
License:        LGPL-2.1-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/themes/3.22/%{name}-%{version}.tar.xz
BuildRequires:  awk
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
Requires:       gtk2-engine-clearlooks
Requires:       gtk2-engine-hcengine
Requires:       gtk2-engine-murrine
Obsoletes:      %{name}-lang
BuildArch:      noarch

%description
Official themes for the MATE desktop

This package contains the official desktop themes of the MATE
desktop environment.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --enable-all-themes
%make_build

%install
%make_install

%icon_theme_cache_create_ghost ContrastHigh
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc NEWS README
# GTK+ themes.
%{_datadir}/themes/BlackMATE*/
%{_datadir}/themes/BlueMenta*/
%{_datadir}/themes/Blue-Submarine*/
%{_datadir}/themes/Green-Submarine*/
%{_datadir}/themes/GreenLaguna*/
%{_datadir}/themes/HighContrast/
%{_datadir}/themes/Menta*/
%{_datadir}/themes/Shiny/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/YaruOk/
%{_datadir}/themes/YaruGreen/
%dir %{_datadir}/themes/ContrastHigh/
%{_datadir}/themes/ContrastHigh/index.theme
%{_datadir}/themes/HighContrastInverse/
# Icon sets.
%{_datadir}/icons/ContrastHigh/
%ghost %{_datadir}/icons/ContrastHigh/icon-theme.cache
# Cursor themes.
%dir %{_datadir}/icons/mate/
%{_datadir}/icons/mate/cursors/
%dir %{_datadir}/icons/mate-black/
%{_datadir}/icons/mate-black/cursors/
%{_datadir}/icons/mate-black/index.theme

%changelog
