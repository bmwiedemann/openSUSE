#
# spec file for package fcitx5-rime
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


Name:           fcitx5-rime
Version:        5.0.15
Release:        0
Summary:        RIME support for Fcitx5
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-rime
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Patch:          %{name}-cmake-3.10.patch
BuildRequires:  brise
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  librime-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif
Requires:       fcitx5
Requires:       rime
Provides:       fcitx-rime = %{version}
Obsoletes:      fcitx-rime <= 0.3.2

%description
This package provides RIME support for Fcitx5.

%prep
%setup -q
%patch -p1

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES
%dir %{_datadir}/fcitx5/inputmethod
%{_libdir}/fcitx5/rime.so
%{_datadir}/fcitx5/addon/rime.conf
%{_datadir}/fcitx5/inputmethod/rime.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-rime*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-rime*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Rime.metainfo.xml
%{_datadir}/rime-data/fcitx5.yaml

%changelog
