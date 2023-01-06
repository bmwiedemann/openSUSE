#
# spec file for package pam_kwallet
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
Name:           pam_kwallet
Version:        5.26.5
Release:        0
Summary:        A PAM Module for KWallet signing
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/kwallet-pam-%{version}.tar.xz
%if %{with released}
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
BuildRequires:  cmake(KF5Wallet) >= 5.98.0
Requires:       %{name}-common = %{version}
# PAM modules need to be available for all archs of PAM on the system, otherwise pam-config
# will not enable it.
# Technically there can be different suffixes than just -32bit, but that's the most common.
# Expressing a hard dependency the other way around in baselibs.conf is not possible.
Requires:       (%{name}-32bit if pam-32bit)
%if 0%{?suse_version} >= 1330
Requires(post): coreutils pam pam-config
Requires(postun):coreutils pam pam-config
%endif

%description
This PAM module allows you to automatically open your kwallet
when signing into your account.

%package common
Summary:        Support files for the KWallet PAM module
Group:          System/GUI/KDE
Requires:       kwalletd5
Requires:       socat
BuildArch:      noarch

%description common
This package contains support files used by the KWallet PAM
module.

%prep
%setup -q -n kwallet-pam-%{version}

%build
  # Before usrmerge, the PAM module goes into /lib*/security/
  %{cmake_kf5 -d build -- \
  %if 0%{?suse_version} < 1550
      -DKDE_INSTALL_LIBDIR=/%{_lib}
  %endif
  }

  %cmake_build

%install
  %kf5_makeinstall -C build

# Due to boo#728586 it is necessary to duplicate this in the 32bit variant.
# So you need to edit baselibs.conf if you change this.
%post
  %{_sbindir}/pam-config -a --kwallet5 || :

%postun
  if [ "$1" = "0" ]; then
    %{_sbindir}/pam-config -d --kwallet5 || :
  fi

%post common
  %systemd_user_post plasma-kwallet-pam.service

%preun common
  %systemd_user_preun plasma-kwallet-pam.service

%postun common
  %systemd_user_postun plasma-kwallet-pam.service

%files
%license LICENSES/*
%if 0%{?suse_version} >= 1550
%{_pam_moduledir}/pam_kwallet5.so
%else
/%{_lib}/security/pam_kwallet5.so
%endif

%files common
%license LICENSES/*
%config %{_kf5_configdir}/autostart/pam_kwallet_init.desktop
%{_libexecdir}/pam_kwallet_init
%{_userunitdir}/plasma-kwallet-pam.service

%changelog
