#
# spec file for package ibus-table
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


Name:           ibus-table
Version:        1.17.6
Release:        0
Summary:        The Table engine for IBus platform
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/mike-fabian/ibus-table/
Source:         https://github.com/mike-fabian/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  docbook-utils-minimal
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  gnome-common
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(python3)
Requires:       ibus >= 1.4.99
Requires:       python3
Requires:       python3-curses
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The package contains general Table engine for IBus platform.

%package devel
Summary:        Development package for ibus-table
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package contains the files required for the development of ibus-table.

%prep
%setup -q
chmod -x AUTHORS COPYING README

%build
export PYTHON=python3
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static \
           --enable-additional \
           --libexecdir=%{_ibus_libexecdir}
%make_build

%install
%make_install NO_INDEX=true

%find_lang %{name}
%fdupes %{buildroot}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/%{name}-createdb
%{_ibus_libexecdir}/ibus-engine-table
%{_ibus_libexecdir}/ibus-setup-table
%{_datadir}/applications/ibus-setup-table.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
%{_ibus_componentdir}/table.xml
%{_mandir}/man1/%{name}-createdb.1.gz
%{_datadir}/metainfo/ibus-table.appdata.xml
%{_datadir}/icons/hicolor/16x16/apps/ibus-table.png
%{_datadir}/icons/hicolor/22x22/apps/ibus-table.png
%{_datadir}/icons/hicolor/32x32/apps/ibus-table.png
%{_datadir}/icons/hicolor/48x48/apps/ibus-table.png
%{_datadir}/icons/hicolor/64x64/apps/ibus-table.png
%{_datadir}/icons/hicolor/128x128/apps/ibus-table.png
%{_datadir}/icons/hicolor/256x256/apps/ibus-table.png
%{_datadir}/icons/hicolor/scalable/apps/ibus-table.svg

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
