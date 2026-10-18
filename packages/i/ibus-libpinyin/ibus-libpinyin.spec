#
# spec file for package ibus-libpinyin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?is_opensuse}
%bcond_without cloud_input
%bcond_without opencc
%bcond_without lua
%bcond_with    boost
%endif
%if !0%{?is_opensuse}
%bcond_with cloud_input
%bcond_with lua
%bcond_with opencc
%bcond_with boost
%endif
Name:           ibus-libpinyin
Version:        1.16.6
Release:        0
Summary:        Intelligent Pinyin engine based on libpinyin for IBus
License:        GPL-3.0-or-later
URL:            https://github.com/libpinyin/ibus-libpinyin
Source:         https://github.com/libpinyin/ibus-libpinyin/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite3
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.11
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpinyin) >= 2.9.92
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
Provides:       locale(ibus:zh_CN;zh_SG)
%{ibus_requires}
%if %{with lua}
BuildRequires:  pkgconfig(lua)
%endif
%if %{with opencc}
BuildRequires:  pkgconfig(opencc) >= 1.0.0
%endif
%if %{with cloud_input}
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

%description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) input
method based on libpinyin for IBus.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure  \
%if %{with opencc}
           --enable-opencc \
%else
           --disable-opencc \
%endif
%if %{with boost}
           --enable-boost \
%else
           --disable-boost \
%endif
%if %{with lua}
           --enable-lua-extension \
%else
           --disable-lua-extension \
%endif
%if %{with cloud_input}
           --enable-cloud-input-mode \
%else
           --disable-cloud-input-mode \
%endif
%if 0%{?sle_version} < 150600 && 0%{?sle_version} >= 150000
           PYTHON=python3.10\
%else
           PYTHON=python3 \
%endif
           --libexecdir=%{_ibus_libexecdir} \
           --libdir=%{_libdir} \
           --datadir=%{_datadir} \
           --disable-static

%make_build

%install
%make_install %{?_smp_mflags}

%fdupes %{buildroot}
%find_lang %{name}

%fdupes %{buildroot}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS
%{_ibus_libexecdir}/ibus-engine-libpinyin
%{_ibus_libexecdir}/ibus-setup-libpinyin
%{_datadir}/applications/ibus-setup-libbopomofo.desktop
%{_datadir}/applications/ibus-setup-libpinyin.desktop
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
%if %{with lua}
%{_datadir}/%{name}/base.lua
%{_datadir}/%{name}/user.lua
%endif

%changelog
