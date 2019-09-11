#
# spec file for package ibus-pinyin
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


Name:           ibus-pinyin
Version:        1.5.0
Release:        0
Summary:        The PinYin engine for IBus platform
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
Provides:       locale(ibus:zh)
Url:            http://code.google.com/p/ibus/
Source0:        http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# PATCH-FIX-FEDORA ibus-pinyin-support-set-content-type-method.patch bnc#847718 tiwai@suse.de -- Fix visible password entry in GNOME lock screen.
Patch1:         ibus-pinyin-support-set-content-type-method.patch
# PATCH-FIX-FEDORA ibus-pinyin-fixes-lua-compile.patch fcrozat@suse.com -- Fix build with lua 5.2
Patch2:         ibus-pinyin-fixes-lua-compile.patch
# PATCH-FIX-OPENSUSE Wlogical-not-parentheses.patch schwab@suse.de boo#1041911 -- Fix -Wlogical-not-parentheses warning.
Patch3:         Wlogical-not-parentheses.patch
# PATFH-FIX-SUSE ibus-pinyin-default-full.patch qzhao@suse.com bsc#955325 -- Set fullpinyin beyond dconf database as default.
Patch4:         ibus-pinyin-default-full.patch
# PATCH-FIX-UPSTREAM ibus-pinyin-select-words-could-be-cleared.patch hillwood@opensuse.org boo#980890 -- The selected words could be cleared while use ibus-pinyin in Firefox.
Patch5:         ibus-pinyin-fix-select-words-could-be-cleared.patch
# PATCH-FIX-OPENSUSE ibus-pinyin-avoid-setup-crash.patch qzhao@suse.com boo#1116485 -- To avoid ibus-pinyin-setup crash in the mixed env of Python2 and Python3.
Patch6:         ibus-pinyin-avoid-setup-crash.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  python >= 2.5
BuildRequires:  sqlite3
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(lua) >= 5.1
BuildRequires:  pkgconfig(pyzy-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
Requires:       ibus >= 1.4.99
Requires:       opencc
Requires:       python3-xdg
Requires:       pyzy-db-android
Requires:       pyzy-db-open-phrase

%description
PinYin engine for IBus platform. It provides a Chinese PinYin input method.


%description -l zh_CN
IBus 输入平台的拼音输入法支持引擎，本软件包为 IBus 提供中文拼音输入支持。

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%configure --disable-static \
           --libexecdir=%{_prefix}/%{_lib}/ibus \
           --with-python=python3

# make -C po update-gmo
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name} 

%suse_update_desktop_file ibus-setup-pinyin Utility DesktopUtility System
%suse_update_desktop_file ibus-setup-bopomofo Utility DesktopUtility System

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_datadir}/ibus-pinyin
%{_datadir}/applications/ibus-*.desktop
%dir %{_datadir}/ibus
%dir %{_datadir}/ibus/component
%{_datadir}/ibus/component/*
%dir %{_libdir}/ibus
%{_libdir}/ibus/ibus-engine-pinyin
%{_libdir}/ibus/ibus-setup-pinyin

%changelog
