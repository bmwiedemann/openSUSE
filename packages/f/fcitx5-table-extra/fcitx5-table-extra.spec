#
# spec file for package fcitx5-table-extra
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


Name:           fcitx5-table-extra
Version:        5.0.12
Release:        0
Summary:        Extra Chinese table input methods for Fcitx5
License:        GPL-3.0-or-later AND SUSE-Public-Domain
URL:            https://github.com/fcitx/fcitx5-table-extra
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libime-devel
Requires:       fcitx5
Provides:       fcitx-table-cn-cantonese = %{version}
Provides:       fcitx-table-cn-wu = %{version}
Provides:       fcitx-table-cn-wubi-large = %{version}
Provides:       fcitx-table-cn-zhengma = %{version}
Provides:       fcitx-table-cn-zhengma-large = %{version}
Provides:       fcitx-table-extra-lang = %{version}
Provides:       fcitx-table-hk-cantonese = %{version}
Provides:       fcitx-table-hk-jyutping = %{version}
Provides:       fcitx-table-hk-stroke5 = %{version}
Provides:       fcitx-table-t9 = %{version}
Provides:       fcitx-table-tw-array30 = %{version}
Provides:       fcitx-table-tw-array30-large = %{version}
Provides:       fcitx-table-tw-boshiamy = %{version}
Provides:       fcitx-table-tw-cangjie-large = %{version}
Provides:       fcitx-table-tw-cangjie3 = %{version}
Provides:       fcitx-table-tw-cangjie5 = %{version}
Provides:       fcitx-table-tw-easy-large = %{version}
Provides:       fcitx-table-tw-quick-classic = %{version}
Provides:       fcitx-table-tw-quick3 = %{version}
Provides:       fcitx-table-tw-quick5 = %{version}
Provides:       fcitx-table-tw-smart-cangjie6 = %{version}
Obsoletes:      fcitx-table-cn-cantonese <= 0.3.8
Obsoletes:      fcitx-table-cn-wu <= 0.3.8
Obsoletes:      fcitx-table-cn-wubi-large <= 0.3.8
Obsoletes:      fcitx-table-cn-zhengma <= 0.3.8
Obsoletes:      fcitx-table-cn-zhengma-large <= 0.3.8
Obsoletes:      fcitx-table-extra-lang <= 0.3.8
Obsoletes:      fcitx-table-hk-cantonese <= 0.3.8
Obsoletes:      fcitx-table-hk-jyutping <= 0.3.8
Obsoletes:      fcitx-table-hk-stroke5 <= 0.3.8
Obsoletes:      fcitx-table-t9 <= 0.3.8
Obsoletes:      fcitx-table-tw-array30 <= 0.3.8
Obsoletes:      fcitx-table-tw-array30-large <= 0.3.8
Obsoletes:      fcitx-table-tw-boshiamy <= 0.3.8
Obsoletes:      fcitx-table-tw-cangjie-large <= 0.3.8
Obsoletes:      fcitx-table-tw-cangjie3 <= 0.3.8
Obsoletes:      fcitx-table-tw-cangjie5 <= 0.3.8
Obsoletes:      fcitx-table-tw-easy-large <= 0.3.8
Obsoletes:      fcitx-table-tw-quick-classic <= 0.3.8
Obsoletes:      fcitx-table-tw-quick3 <= 0.3.8
Obsoletes:      fcitx-table-tw-quick5 <= 0.3.8
Obsoletes:      fcitx-table-tw-smart-cangjie6 <= 0.3.8
BuildArch:      noarch
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-table-extra provides extra table for Fcitx, including Boshiamy, Zhengma, Cangjie, and Quick.

%prep
%setup -q

%build
%cmake -DLibIMETable_DIR=%{_libdir}/cmake/LibIMETable \
  -DLibIMECore_DIR=%{_libdir}/cmake/LibIMECore \
  -DFcitx5Utils_DIR=%{_libdir}/cmake/Fcitx5Utils \
  -DFcitx5Core_DIR=%{_libdir}/cmake/Fcitx5Core \
  -DFcitx5Config_DIR=%{_libdir}/cmake/Fcitx5Config
%make_build

%install
%cmake_install

%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README
%{_datadir}/icons/hicolor/*/apps/fcitx-*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-*
%{_fcitx5_imconfdir}/*.conf
%{_fcitx5_datadir}/table
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.TableExtra.metainfo.xml

%changelog
