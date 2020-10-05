#
# spec file for package Srain
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.1.3
Release:        0
Summary:        An IRC client
License:        GPL-3.0-or-later AND ISC
URL:            https://srain.im
Source:         https://github.com/SrainApp/srain/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Srain-no_implicit_declarations.patch
Patch0:         Srain-no_implicit_declarations.patch
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.48.2
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libconfig) >= 1.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(openssl)

%description
IRC client written in GTK3+.

%lang_package

%prep
%autosetup -p1 -n srain-%{version}

%build
%configure --disable-debug
%make_build

%install
%make_install
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
%{_datadir}/metainfo/im.srain.%{name}.metainfo.xml
%{_datadir}/srain/themes/*.css

%files lang -f srain.lang

%changelog
