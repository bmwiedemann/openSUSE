#
# spec file for package ksshaskpass5
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


%bcond_without released
Name:           ksshaskpass5
Version:        5.26.5
Release:        0
Summary:        Plasma 5 version of ssh-askpass
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/ksshaskpass-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/ksshaskpass-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
Recommends:     %{name}-lang
Supplements:    packageand(openssh:plasma5-workspace)
Provides:       ksshaskpass = %{version}
Obsoletes:      ksshaskpass < %{version}

%description
A Plasma 5 version of ssh-askpass with KWallet support.

%lang_package

%prep
%autosetup -p1 -n ksshaskpass-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} -DKDE_INSTALL_BINDIR=%{_libexecdir}/ssh
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%files
%license LICENSES/*
%dir %{_libexecdir}/ssh
%{_libexecdir}/ssh/ksshaskpass
%doc %lang(en) %{_kf5_mandir}/man1/ksshaskpass.1*

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
