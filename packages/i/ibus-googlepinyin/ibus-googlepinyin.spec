#
# spec file for package ibus-googlepinyin
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


Name:           ibus-googlepinyin
Version:        0.42.0
Release:        0
Summary:        This package is for IBus to use libgooglepinyin
License:        GPL-2.0+
Group:          System/I18n/Chinese 
Url:            https://github.com/openSUSE/ibus-googlepinyin
BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libgooglepinyin-devel
BuildRequires:  python3-devel
%if 0%{?suse_version}
BuildRequires:  sqlite3-devel
%else
BuildRequires:  desktop-notification-daemon
BuildRequires:  kdebase-runtime
BuildRequires:  notification-daemon
BuildRequires:  sqlite-devel
BuildRequires:  xfce4-notifyd
%endif
Source:         https://github.com/openSUSE/ibus-googlepinyin/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         do-not-install-gschemas_compiled.patch
Requires:       ibus
Requires:       libgooglepinyin0

%description
GooglePinyin
===

libgooglepinyin is a fork of Google Pinyin on Android, it features to have 
excellent input experience and uses little resource.

==
This package is for IBus to use libgooglepinyin. 


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_datadir}/%{name}
%{_libexecdir}/ibus-setup-googlepinyin
%{_datadir}/applications/ibus-setup-googlepinyin.desktop
%{_datadir}/ibus/component/googlepinyin.xml
%{_datadir}/glib-2.0/schemas/*

%changelog
