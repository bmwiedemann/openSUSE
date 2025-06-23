#
# spec file for package fcitx5-zhuyin
#
# Copyright (c) 2025 SUSE LLC
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
Version:        5.1.4
Release:        0
Summary:        Libzhuyin Wrapper for Fcitx5
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-zhuyin
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fmt-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  libpinyin-devel
BuildRequires:  pkgconfig
BuildRequires:  zstd
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

%build
%if 0%{?suse_version} < 1550
export CC=%{_bindir}/gcc-13
export CXX=%{_bindir}/g++-13
%endif
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
%{_datadir}/icons/hicolor/*/apps/fcitx-bopomofo*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-bopomofo*
%{_fcitx5_datadir}/lua/imeapi/extensions/zhuyin.lua
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Zhuyin.metainfo.xml

%changelog
