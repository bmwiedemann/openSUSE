#
# spec file for package fcitx5-kkc
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


Name:           fcitx5-kkc
Version:        5.1.7
Release:        0
Summary:        Libkkc input method support for Fcitx5
License:        GPL-3.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/fcitx/fcitx5-kkc
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libkkc-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
BuildRequires:  zstd
Requires:       fcitx5
Requires:       kkc-data
Provides:       fcitx-kkc = %{version}
Obsoletes:      fcitx-kkc <= 0.1.4
Obsoletes:      fcitx5-kkc-qt6 <= 5.1.6
Supplements:    (fcitx5 and kkc-data)
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
This package provides libkkc input method support for Fcitx5.

%prep
%setup -q -n %{name}-%{version}

%build
%if 0%{?suse_version} == 1500
%cmake -DCMAKE_CXX_COMPILER=%{_bindir}/g++-13
%else
%cmake
%endif
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES
%dir %{_datadir}/fcitx5/inputmethod
%dir %{_datadir}/fcitx5/kkc
%{_libdir}/fcitx5/kkc.so
%{_libdir}/fcitx5/qt6/libfcitx5-kkc-config.so
%{_datadir}/fcitx5/addon/kkc.conf
%{_datadir}/fcitx5/inputmethod/kkc.conf
%{_datadir}/fcitx5/kkc/dictionary_list
%{_datadir}/fcitx5/kkc/rule
%{_datadir}/icons/hicolor/*/apps/fcitx_kkc.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_kkc.png
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Kkc.metainfo.xml

%changelog
