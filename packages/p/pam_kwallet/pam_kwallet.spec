#
# spec file for package pam_kwallet
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

Name:           pam_kwallet
Version:        5.20.2
Release:        0
Summary:        A PAM Module for KWallet signing
License:        LGPL-2.1-only AND GPL-2.0-or-later AND GPL-3.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/kwallet-pam-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwallet-pam-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  pam-devel
BuildRequires:  socat
BuildRequires:  xz
BuildRequires:  cmake(KF5Wallet) >= 5.58.0
Requires:       %{name}-common = %{version}
%if 0%{?suse_version} >= 1330
Requires(post): coreutils pam pam-config
Requires(postun): coreutils pam pam-config
%endif

%description
This PAM module allows you to automatically open your kwallet
when signing into your account.

%package common
Summary:        Support files for the KWallet PAM module
Group:          System/GUI/KDE
Requires:       kwalletd5
Requires:       socat

%description common
This package contains support files used by the KWallet PAM
module.

%prep
%setup -q -n kwallet-pam-%{version}

%build
  %cmake_kf5 -d build -- -DLIBEXEC_INSTALL_DIR=%{_kf5_libexecdir} -DCMAKE_INSTALL_PREFIX=/
  %cmake_build

%install
  %kf5_makeinstall -C build

%if 0%{?suse_version} >= 1330
# Due to boo#728586 it is necessary to duplicate this in the 32bit variant.
# So you need to edit baselibs.conf if you change this.
%post
  %{_sbindir}/pam-config -a --kwallet5 || :

%postun
  if [ "$1" = "0" ]; then
    %{_sbindir}/pam-config -d --kwallet5 || :
  fi
%endif

%files
%license COPYING*
/%{_lib}/security/pam_kwallet5.so

%files common
%license COPYING*
%config %{_kf5_configdir}/autostart/pam_kwallet_init.desktop
%{_kf5_libexecdir}/pam_kwallet_init

%changelog
