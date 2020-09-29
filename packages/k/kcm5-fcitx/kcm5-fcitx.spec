#
# spec file for package kcm5-fcitx
#
# Copyright (c) 2020 SUSE LLC
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


%define		pkgname	kf5-kcm-fcitx
Name:           kcm5-fcitx
Version:        0.5.6
Release:        0
Summary:        KF5 control module for Fcitx
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            http://github.com/fcitx/kcm-fcitx
Source:         http://download.fcitx-im.org/kcm-fcitx/kcm-fcitx-%{version}.tar.xz
Source1:        input-keyboard.svg
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  kcmutils-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libtool
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  xz
BuildRequires:  pkgconfig(xkbfile)
Requires:       fcitx-kcm-icons
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KF5 control module for Fcitx.

You can config fcitx through "Configue Desktop" - "Locale" - Fcitx now.

%package -n %{pkgname}
Summary:        KF5 control module for Fcitx
Group:          System/I18n/Chinese
Requires:       fcitx-qt5
Requires:       plasma5-workspace
Supplements:    packageand(fcitx:plasma5-workspace)
Provides:       locale(plasma5-workspace:ko;zh_CN;zh_SG)
# for better user experience
Provides:       fcitx-config-kde5 = %{version}
Provides:       fcitx-config-kf5 = %{version}
Obsoletes:      fcitx-config-kde5 < %{version}
%{fcitx_requires}

%description -n %{pkgname}
KF5 control module for Fcitx.

You can config fcitx through "Configure Desktop" - "Locale" - Fcitx now.

%package -n %{pkgname}-icons
Summary:        Keyboard icons for %{pkgname}
Group:          System/I18n/Chinese
Requires:       %{pkgname} = %{version}
Supplements:    packageand(%{pkgname}:plasma5-workspace-branding-openSUSE)
Conflicts:      otherproviders(fcitx-kcm-icons)
Provides:       fcitx-config-kde5-icons = %{version}
Obsoletes:      fcitx-config-kde5-icons < %{version}
Provides:       fcitx-kcm-icons = %{version}
BuildArch:      noarch

%description -n %{pkgname}-icons
This package provides systemsettings5 icons for fcitx in plasma5-workspace.

%prep
%setup -q -n kcm-fcitx-%{version}

%build
%cmake_kf5 -d build
make %{?_smp_mflags}

%install
pushd build
%kf5_makeinstall
popd

ICONSIZE="16 22 32 48 64 128 256"
for i in $ICONSIZE; do
    mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/devices/
    rsvg-convert -h $i -w $i %{SOURCE1} -o %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/devices/input-keyboard.png
done

%find_lang kcm_fcitx

%{kf5_post_install}

%post -n %{pkgname} -p /sbin/ldconfig
%postun -n %{pkgname} -p /sbin/ldconfig

%files -n %{pkgname} -f kcm_fcitx.lang
%defattr(-,root,root,-)
%{_bindir}/kbd-layout-viewer
%{_libdir}/qt5/plugins/kcm_fcitx.so
%{_datadir}/kservices5/kcm_fcitx.desktop
%{_datadir}/applications/kbd-layout-viewer.desktop

%files -n %{pkgname}-icons
%defattr(-,root,root,-)
%{_datadir}/icons/hicolor/*/devices/input-keyboard.png

%changelog
