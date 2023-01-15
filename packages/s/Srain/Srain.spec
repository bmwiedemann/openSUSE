#
# spec file for package Srain
#
# Copyright (c) 2023 SUSE LLC
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


Name:           Srain
Version:        1.5.0
Release:        0
Summary:        An IRC client
License:        GPL-3.0-or-later AND ISC
URL:            https://srain.im
Source:         https://github.com/SrainApp/srain/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.15
BuildRequires:  pkgconfig(libconfig) >= 1.5
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(openssl)

%description
IRC client written in GTK3+.

%lang_package

%prep
%autosetup -p1 -n srain-%{version}

%build
%meson -Ddoc_builders=man
%meson_build

%install
%meson_install
%find_lang srain

%files
%license LICENSE
%doc README.rst
%dir %{_datadir}/srain
%dir %{_datadir}/srain/themes
%dir %{_sysconfdir}/srain
%config %{_sysconfdir}/srain/builtin.cfg
%{_bindir}/srain
%{_datadir}/applications/im.srain.%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/im.srain.%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/im.srain.%{name}.Red.png
%{_datadir}/metainfo/im.srain.%{name}.metainfo.xml
%{_datadir}/srain/themes/*.css
%{_mandir}/man1/srain.1%{?ext_man}

%files lang -f srain.lang

%changelog
