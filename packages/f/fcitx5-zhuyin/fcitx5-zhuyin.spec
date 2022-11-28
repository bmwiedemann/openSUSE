#
# spec file for package fcitx5-zhuyin
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


Name:           fcitx5-zhuyin
Version:        5.0.11
Release:        0
Summary:        Libzhuyin Wrapper for Fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-zhuyin
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/data/model.text.20161206.tar.gz
Patch1:         %{name}-no-download.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libpinyin-devel
BuildRequires:  libzhuyin13
BuildRequires:  pkgconfig
Requires:       fcitx5
Provides:       fcitx-zhuyin = %{version}
Obsoletes:      fcitx-zhuyin <= 0.1.1
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Libzhuyin Wrapper for Fcitx5.

%prep
%setup -q
%patch1 -p1
cp -r %{SOURCE1} data

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README
%dir %{_fcitx5_datadir}/lua
%dir %{_fcitx5_datadir}/lua/imeapi
%dir %{_fcitx5_datadir}/lua/imeapi/extensions
%{_fcitx5_libdir}/zhuyin.so
%{_fcitx5_addondir}/zhuyin.conf
%{_fcitx5_imconfdir}/zhuyin.conf
%{_fcitx5_datadir}/zhuyin
%{_datadir}/icons/hicolor/*/apps/fcitx-zhuyin*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-zhuyin*
%{_fcitx5_datadir}/lua/imeapi/extensions/zhuyin.lua
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Zhuyin.metainfo.xml

%changelog
