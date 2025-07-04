#
# spec file for package ibus-libpinyin
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2023 Hillwood Yang <hillwood@opensuse.org>
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


%define   with_cloud_input   1

Name:           ibus-libpinyin
Version:        1.16.3
Release:        0
Summary:        Intelligent Pinyin engine based on libpinyin for IBus
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/libpinyin/ibus-libpinyin
Source0:        https://github.com/libpinyin/ibus-libpinyin/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  ibus-devel >= 1.5.11
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  opencc-devel >= 1.0.0
BuildRequires:  pkgconfig
BuildRequires:  sqlite3
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpinyin) >= 2.9.92
BuildRequires:  pkgconfig(lua)
%if %{with_cloud_input}
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
%endif
%if 0%{?sle_version} < 150600 && 0%{?sle_version} >= 150000
BuildRequires:  python310-base
Requires:       python310-base
Requires:       python310-gobject-Gdk
%else
BuildRequires:  python3-base
Requires:       python3-base
Requires:       python3-gobject-Gdk
%endif
Provides:       locale(ibus:zh_CN;zh_SG)
%{ibus_requires}

%description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) input
method based on libpinyin for IBus.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static \
           --enable-opencc \
           --disable-boost \
           --libexecdir=%{_ibus_libexecdir} \
           --libdir=%{_libdir} \
%if %{with_cloud_input}
           --enable-cloud-input-mode \
%endif
%if 0%{?sle_version} < 150600 && 0%{?sle_version} >= 150000
           PYTHON=python3.10
%else
           PYTHON=python3
%endif

%make_build

%install
%make_install

%fdupes %{buildroot}
%find_lang %{name}

%suse_update_desktop_file ibus-setup-libpinyin Utility DesktopUtility System
%suse_update_desktop_file ibus-setup-libbopomofo Utility DesktopUtility System

%fdupes %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%license COPYING
%doc AUTHORS README NEWS
%{_ibus_libexecdir}/ibus-engine-libpinyin
%{_ibus_libexecdir}/ibus-setup-libpinyin
%{_datadir}/applications/ibus-setup-libbopomofo.desktop
%{_datadir}/applications/ibus-setup-libpinyin.desktop
%{_datadir}/%{name}/base.lua
%{_datadir}/%{name}/user.lua
%{_datadir}/%{name}/db/english.db
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db
%dir %{_datadir}/metainfo
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/setup
%{_datadir}/%{name}/network.txt
%{_datadir}/%{name}/default.xml
%{_datadir}/ibus-libpinyin/db/table.db
%{_datadir}/metainfo/libpinyin.appdata.xml
%{_datadir}/ibus
%{_datadir}/glib-2.0/schemas/com.github.libpinyin.ibus-libpinyin.gschema.xml

%changelog
