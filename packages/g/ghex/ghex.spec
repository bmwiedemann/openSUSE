#
# spec file for package ghex
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ghex
Version:        3.41.0
Release:        0
Summary:        GNOME Binary Editor
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Ghex
Source:         https://download.gnome.org/sources/ghex/3.41/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk) >= 1.0.0
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.3.8

%description
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package -n libgtkhex-3-0
Summary:        GNOME Binary Editor -- Library
Group:          System/Libraries

%description -n libgtkhex-3-0
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package devel
Summary:        GNOME Binary Editor -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgtkhex-3-0 = %{version}

%description devel
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%suse_update_desktop_file -r org.gnome.GHex GNOME Utility Editor
%find_lang %{name} ghex-3.0.lang %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%post -n libgtkhex-3-0 -p /sbin/ldconfig
%postun -n libgtkhex-3-0 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md COPYING-DOCS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/ghex
%{_datadir}/metainfo/org.gnome.GHex.appdata.xml
%{_datadir}/applications/org.gnome.GHex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.GHex*

%files -n libgtkhex-3-0
%{_libdir}/libgtkhex-3.so.*

%files devel
%{_includedir}/gtkhex-3/
%{_libdir}/libgtkhex-3.so
%{_libdir}/pkgconfig/gtkhex-3.pc

%files lang -f %{name}-3.0.lang

%changelog
