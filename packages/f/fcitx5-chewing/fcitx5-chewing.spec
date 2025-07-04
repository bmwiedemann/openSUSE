#
# spec file for package fcitx5-chewing
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


Name:           fcitx5-chewing
Version:        5.1.8
Release:        0
Summary:        Chewing Wrapper for Fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-chewing
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libchewing-devel
BuildRequires:  pkgconfig
BuildRequires:  zstd
Requires:       chewing-data
Requires:       fcitx5
Provides:       fcitx-chewing = %{version}
Obsoletes:      fcitx-chewing < %{version}
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Chewing Wrapper for Fcitx5.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1550
export CXX=%{_bindir}/g++-13
%endif
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README.md
%{_fcitx5_libdir}/libchewing.so
%{_fcitx5_addondir}/chewing.conf
%{_fcitx5_imconfdir}/chewing.conf
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-chewing*
%{_datadir}/icons/hicolor/*/apps/fcitx-chewing*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Chewing.metainfo.xml

%changelog
