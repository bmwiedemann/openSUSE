#
# spec file for package ksshaskpass6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0
%define rname ksshaskpass
%bcond_without released
Name:           ksshaskpass6
Version:        6.1.2
Release:        0
Summary:        Plasma 6 version of ssh-askpass
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
Supplements:    (openssh and plasma6-workspace)
Provides:       ksshaskpass = %{version}
Obsoletes:      ksshaskpass < %{version}
Provides:       ksshaskpass5 = %{version}
Obsoletes:      ksshaskpass5 < %{version}
Obsoletes:      ksshaskpass5-lang < %{version}

%description
A Plasma 6 version of ssh-askpass with KWallet support.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# KDE_INSTALL_BINDIR is redefined to install ksshaskpass in the same folder as ssh-askpass, gnome-ssh-askpass, etc...
%cmake_kf6 -DKDE_INSTALL_BINDIR:STRING=%{_libexecdir}/ssh

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%dir %{_libexecdir}/ssh
%{_libexecdir}/ssh/ksshaskpass
%doc %lang(en) %{_kf6_mandir}/man1/ksshaskpass.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
