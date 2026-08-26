#
# spec file for package gpredict
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gpredict
Version:        2.6
Release:        0
Summary:        Realtime satellite tracking and orbit prediction application
# Legal-Review-Notice: every upstream source header grants GPL "version 2 ...
# or (at your option) any later version", and upstream's own AppStream
# metainfo declares GPL-2.0+. src/nxjson/ is bundled, listed in
# gpredict_SOURCES and thus compiled into the gpredict binary, under
# LGPL-3.0-or-later.
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://gpredict.oz9aec.net/
Source:         https://github.com/csete/gpredict/releases/download/v%{version}/gpredict-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.21
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(libcurl) >= 7.19
BuildRequires:  pkgconfig(libgps) >= 2.90
Recommends:     %{name}-lang
Recommends:     hamlib

%description
Gpredict is a real-time satellite tracking and orbit prediction
application. It can track a large number of satellites and display
their position and other data in lists, tables, maps, and polar plots
(radar view). Gpredict can also predict the time of future passes for a
satellite, and provide you with detailed information about each pass.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
%fdupes -s %{buildroot}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gpredict
%{_datadir}/applications/gpredict.desktop
%{_datadir}/gpredict/
%{_datadir}/pixmaps/gpredict/
%{_datadir}/icons/hicolor/scalable/apps/gpredict.svg
%{_datadir}/metainfo/dk.oz9aec.Gpredict.metainfo.xml
%{_mandir}/man1/gpredict.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
