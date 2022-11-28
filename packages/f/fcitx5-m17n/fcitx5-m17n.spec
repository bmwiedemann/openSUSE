#
# spec file for package fcitx5-m17n
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


Name:           fcitx5-m17n
Version:        5.0.11
Release:        0
Summary:        M17n input method engine for Fcitx5
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-m17n
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  m17n-lib-devel
BuildRequires:  pkgconfig
Requires:       fcitx5
Requires:       m17n-db
Provides:       fcitx-m17n = %{version}
Obsoletes:      fcitx-m17n <= 0.2.4
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
M17n input method engine for Fcitx5.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README.md
%{_fcitx5_libdir}/m17n.so
%{_fcitx5_addondir}/m17n.conf
%{_fcitx5_datadir}/m17n
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.M17N.metainfo.xml

%changelog
