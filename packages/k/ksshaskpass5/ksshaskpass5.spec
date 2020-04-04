#
# spec file for package ksshaskpass5
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


%bcond_without lang
Name:           ksshaskpass5
Version:        5.18.4.1
Release:        0
Summary:        Plasma 5 version of ssh-askpass
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/5.18.4/ksshaskpass-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/5.18.4/ksshaskpass-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Patch1:         suse-tweaks.diff
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core) >= 5.4.0
%if %{with lang}
Recommends:     %{name}-lang
%endif
Supplements:    packageand(openssh:plasma5-workspace)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       ksshaskpass = %{version}
Obsoletes:      ksshaskpass < %{version}
%else
Conflicts:      ksshaskpass
%endif

%description
A Plasma 5 version of ssh-askpass with KWallet support.

%lang_package
%prep
%setup -q -n ksshaskpass-%{version}
%patch1 -p1

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

%files
%license COPYING*
%dir %{_kf5_prefix}/lib/ssh
%{_kf5_prefix}/lib/ssh/ksshaskpass
%doc %lang(en) %{_kf5_mandir}/man1/ksshaskpass.1*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
