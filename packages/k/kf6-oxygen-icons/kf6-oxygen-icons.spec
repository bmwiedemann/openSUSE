#
# spec file for package kf6-oxygen-icons
#
# Copyright (c) 2024 SUSE LLC
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


%define qt6_version 6.6.0
%define rname oxygen-icons
# Full KF6 version (e.g. 6.0.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_with autotests
%bcond_without released
Name:           kf6-oxygen-icons
Version:        6.1.0
Release:        0
Summary:        Oxygen Icon Theme
License:        LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/oxygen-icons/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/oxygen-icons/%{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
Source99:       kf6-oxygen-icons-rpmlintrc
%endif
Source3:        22x22-package-manager-icon.png
Source4:        32x32-package-manager-icon.png
Source5:        48x48-package-manager-icon.png
Source6:        22x22_folder-html.png
Source7:        32x32_folder-html.png
Source8:        48x48_folder-html.png
Source9:        64x64_folder-html.png
Source10:       128x128_folder-html.png
Source11:       256x256_folder-html.png
Source12:       16x16_folder-html.png
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
# KDEInstallDirs6 needs qtpath
BuildRequires:  cmake(Qt6CoreTools) >= %{qt6_version}
Requires:       hicolor-icon-theme
Recommends:     kf6-oxygen-icons-large
Provides:       oxygen-icon-theme = 15.08
Obsoletes:      oxygen-icon-theme < 15.08
Provides:       oxygen5-icon-theme = %{version}
Obsoletes:      oxygen5-icon-theme < %{version}
BuildArch:      noarch
%if %{with autotests}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%endif

%description
This package contains the non-scalable icons of the Oxygen icon theme.

%package large
Summary:        Oxygen Icon Theme
Requires:       %{name} = %{version}
Provides:       oxygen-icon-theme-large = 15.08
Obsoletes:      oxygen-icon-theme-large < 15.08
Provides:       oxygen5-icon-theme-large = %{version}
Obsoletes:      oxygen5-icon-theme-large < %{version}

%description large
This package contains the large (128x128 and larger) non-scalable icons of the Oxygen icon theme.

%package scalable
Summary:        Oxygen Icon Theme
Requires:       %{name} = %{version}
Provides:       oxygen-icon-theme-scalable = 15.08
Obsoletes:      oxygen-icon-theme-scalable < 15.08
Provides:       oxygen5-icon-theme-scalable = %{version}
Obsoletes:      oxygen5-icon-theme-scalable < %{version}

%description scalable
This package contains the scalable icons of the Oxygen icon theme.

%prep
%autosetup -p1 -n %{rname}-%{version}

%if %{without autotests}
sed -i -e 's/.*autotests/# \0/' CMakeLists.txt
%endif

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

install -D -m 0644 %{SOURCE3} %{buildroot}%{_kf6_iconsdir}/oxygen/base/22x22/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE4} %{buildroot}%{_kf6_iconsdir}/oxygen/base/32x32/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE5} %{buildroot}%{_kf6_iconsdir}/oxygen/base/48x48/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE6} %{buildroot}%{_kf6_iconsdir}/oxygen/base/22x22/places/folder-html.png
install -D -m 0644 %{SOURCE7} %{buildroot}%{_kf6_iconsdir}/oxygen/base/32x32/places/folder-html.png
install -D -m 0644 %{SOURCE8} %{buildroot}%{_kf6_iconsdir}/oxygen/base/48x48/places/folder-html.png
install -D -m 0644 %{SOURCE9} %{buildroot}%{_kf6_iconsdir}/oxygen/base/64x64/places/folder-html.png
install -D -m 0644 %{SOURCE10} %{buildroot}%{_kf6_iconsdir}/oxygen/base/128x128/places/folder-html.png
install -D -m 0644 %{SOURCE11} %{buildroot}%{_kf6_iconsdir}/oxygen/base/256x256/places/folder-html.png
install -D -m 0644 %{SOURCE12} %{buildroot}%{_kf6_iconsdir}/oxygen/base/16x16/places/folder-html.png

for i in 16x16 22x22 32x32 48x48 64x64 128x128 256x256;
do
install -D -m 0644 %{buildroot}%{_kf6_iconsdir}/oxygen/base/${i}/places/folder-html.png %{buildroot}%{_kf6_iconsdir}/oxygen/base/${i}/places/folder_html.png
install -D -m 0644 %{buildroot}%{_kf6_iconsdir}/oxygen/base/${i}/places/folder-documents.png %{buildroot}%{_kf6_iconsdir}/oxygen/base/${i}/apps/document.png
done

pushd build
cp -r ../scalable %{buildroot}%{_kf6_iconsdir}/oxygen/base
popd

%fdupes %{buildroot}

%files
%license COPYING*
%exclude %{_kf6_iconsdir}/oxygen/base/scalable
%exclude %{_kf6_iconsdir}/oxygen/base/128x128
%exclude %{_kf6_iconsdir}/oxygen/base/256x256
%{_kf6_iconsdir}/oxygen/

%files large
%{_kf6_iconsdir}/oxygen/base/128x128/
%{_kf6_iconsdir}/oxygen/base/256x256/

%files scalable
%{_kf6_iconsdir}/oxygen/base/scalable/

%changelog
