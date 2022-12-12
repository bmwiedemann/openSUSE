#
# spec file for package oxygen5-icon-theme
#
# Copyright (c) 2021 SUSE LLC
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_with autotests
# Only needed for the package signature condition
%bcond_without released
Name:           oxygen5-icon-theme
Version:        5.101.0
Release:        0
Summary:        Oxygen Icon Theme
License:        LGPL-3.0-only
URL:            https://www.kde.org
Source:         oxygen-icons5-%{version}.tar.xz
%if %{with released}
Source1:        oxygen-icons5-%{version}.tar.xz.sig
Source2:        frameworks.keyring
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
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  xz
Requires:       hicolor-icon-theme
Recommends:     oxygen5-icon-theme-large
Provides:       oxygen-icon-theme = 15.08
Obsoletes:      oxygen-icon-theme < 15.08
BuildArch:      noarch
%if %{with autotests}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
%endif

%description
This package contains the non-scalable icons of the Oxygen icon theme.

%prep
%autosetup -p1 -n oxygen-icons5-%{version}

%if %{without autotests}
sed -i -e's/.*autotests/# \0/' CMakeLists.txt
%endif

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/oxygen/base/22x22/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/oxygen/base/32x32/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/oxygen/base/48x48/apps/package-manager-icon.png
install -D -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/icons/oxygen/base/22x22/places/folder-html.png
install -D -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/icons/oxygen/base/32x32/places/folder-html.png
install -D -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/icons/oxygen/base/48x48/places/folder-html.png
install -D -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/icons/oxygen/base/64x64/places/folder-html.png
install -D -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/icons/oxygen/base/128x128/places/folder-html.png
install -D -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/icons/oxygen/base/256x256/places/folder-html.png
install -D -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/icons/oxygen/base/16x16/places/folder-html.png

for i in 16x16 22x22 32x32 48x48 64x64 128x128 256x256;
do
install -D -m 0644 %{buildroot}%{_datadir}/icons/oxygen/base/${i}/places/folder-html.png %{buildroot}%{_datadir}/icons/oxygen/base/${i}/places/folder_html.png
install -D -m 0644 %{buildroot}%{_datadir}/icons/oxygen/base/${i}/places/folder-documents.png %{buildroot}%{_datadir}/icons/oxygen/base/${i}/apps/document.png;
done

pushd build
cp -r ../scalable %{buildroot}%{_datadir}/icons/oxygen/base
popd

%fdupes %{buildroot}

%package scalable
Summary:        Oxygen Icon Theme
Requires:       %{name} = %{version}
Provides:       oxygen-icon-theme-scalable = 15.08
Obsoletes:      oxygen-icon-theme-scalable < 15.08

%description scalable
This package contains the scalable icons of the Oxygen icon theme.

%files scalable
%{_kf5_iconsdir}/oxygen/base/scalable

%package large
Summary:        Oxygen Icon Theme
Requires:       %{name} = %{version}
Provides:       oxygen-icon-theme-large = 15.08
Obsoletes:      oxygen-icon-theme-large < 15.08

%description large
This package contains the large (128x128 and larger) non-scalable icons of the Oxygen icon theme.

%files large
%{_kf5_iconsdir}/oxygen/base/128x128
%{_kf5_iconsdir}/oxygen/base/256x256

%files
%license COPYING*
%exclude %{_kf5_iconsdir}/oxygen/base/scalable
%exclude %{_kf5_iconsdir}/oxygen/base/128x128
%exclude %{_kf5_iconsdir}/oxygen/base/256x256
%{_kf5_iconsdir}/oxygen

%changelog
