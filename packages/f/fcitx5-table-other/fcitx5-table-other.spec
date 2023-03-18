#
# spec file for package fcitx5-table-other
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fcitx5-table-other
Version:        5.0.11
Release:        0
Summary:        Other Non-Chinese table input methods for Fcitx5
License:        GPL-3.0-only AND SUSE-Public-Domain
URL:            https://github.com/fcitx/fcitx5-table-other
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libime-devel
Requires:       fcitx5
Provides:       fcitx-table-other = %{version}
Obsoletes:      fcitx-table-other < 4.99.0
Provides:       fcitx-table-amharic = %{version}
Provides:       fcitx-table-arabic = %{version}
Provides:       fcitx-table-cn-cns11643 = %{version}
Provides:       fcitx-table-emoji = %{version}
Provides:       fcitx-table-ipa-x-sampa = %{version}
Provides:       fcitx-table-latex = %{version}
Provides:       fcitx-table-malayalam-compose = %{version}
Provides:       fcitx-table-malayalam-phonetic = %{version}
Provides:       fcitx-table-ru-rustrad = %{version}
Provides:       fcitx-table-ru-translit = %{version}
Provides:       fcitx-table-ru-yawerty = %{version}
Provides:       fcitx-table-tamil-remington = %{version}
Provides:       fcitx-table-thai = %{version}
Provides:       fcitx-table-ua-translit = %{version}
Provides:       fcitx-table-vi-qr = %{version}
Obsoletes:      fcitx-table-amharic <= 0.2.4
Obsoletes:      fcitx-table-arabic <= 0.2.4
Obsoletes:      fcitx-table-cn-cns11643 <= 0.2.4
Obsoletes:      fcitx-table-emoji <= 0.2.4
Obsoletes:      fcitx-table-ipa-x-sampa <= 0.2.4
Obsoletes:      fcitx-table-latex <= 0.2.4
Obsoletes:      fcitx-table-malayalam-compose <= 0.2.4
Obsoletes:      fcitx-table-malayalam-phonetic <= 0.2.4
Obsoletes:      fcitx-table-ru-rustrad <= 0.2.4
Obsoletes:      fcitx-table-ru-translit <= 0.2.4
Obsoletes:      fcitx-table-ru-yawerty <= 0.2.4
Obsoletes:      fcitx-table-tamil-remington <= 0.2.4
Obsoletes:      fcitx-table-thai <= 0.2.4
Obsoletes:      fcitx-table-ua-translit <= 0.2.4
Obsoletes:      fcitx-table-vi-qr <= 0.2.4
BuildArch:      noarch
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-table-other provides some other Non-Chinese table for Fcitx.

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
%fdupes %{buildroot}

%files
%license LICENSES/GPL-3.0-only.txt
%doc README
%{_datadir}/icons/hicolor/*/apps/fcitx-*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-*
%{_fcitx5_imconfdir}/*.conf
%{_fcitx5_datadir}/table
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.TableOther.metainfo.xml

%changelog
