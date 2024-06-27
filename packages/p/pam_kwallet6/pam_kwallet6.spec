#
# spec file for package pam_kwallet6
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

%define rname kwallet-pam

%bcond_without released
Name:           pam_kwallet6
Version:        6.1.1
Release:        0
Summary:        A PAM Module for KWallet signing
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
# PATCH-FEATURE-OPENSUSE
Patch0:         0002-Use-GNUInstallDirs-instead-of-KDEInstallDirs.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  socat
BuildRequires:  pkgconfig(libgcrypt) >= 1.5.0
# PAM modules need to be available for all archs of PAM on the system, otherwise pam-config
# will not enable it.
# Technically there can be different suffixes than just -32bit, but that's the most common.
# Expressing a hard dependency the other way around in baselibs.conf is not possible.
Requires:       (%{name}-32bit if pam-32bit)
Requires:       pam_kwallet6-common = %{version}
Requires(post): coreutils
Requires(post): pam
Requires(post): pam-config
Requires(postun): coreutils
Requires(postun): pam
Requires(postun): pam-config
Provides:       pam_kwallet = %{version}
Obsoletes:      pam_kwallet < %{version}

%description
This PAM module allows you to automatically open your kwallet
when signing into your account.

%package common
Summary:        Support files for the KWallet PAM module
Requires:       kwalletd6
Requires:       socat
Provides:       pam_kwallet-common = %{version}
Obsoletes:      pam_kwallet-common < %{version}
BuildArch:      noarch

%description common
This package contains support files used by the KWallet PAM
module.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# Before usrmerge, the PAM module goes into /lib*/security/
%cmake_kf6 -DKWALLETD_BIN_PATH=%{_kf6_bindir}/kwalletd6 \
    -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
%if 0%{?suse_version} < 1550
    -DCMAKE_INSTALL_LIBDIR=/%{_lib}
%endif

%kf6_build

%install
%kf6_install

# Try to enable it in %post already, but it might not work at this time.
# Due to boo#728586 it is necessary to duplicate this in the 32bit variant,
# so you need to edit baselibs.conf if you change this.
%post
%{_sbindir}/pam-config -a --kwallet5 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/pam-config -d --kwallet5 || :
fi

# Enable this in posttrans to win over the old package's %postun
# and to run once the modules are installed for all archs (boo#728586).
%posttrans
%{_sbindir}/pam-config -a --kwallet5 || :

%post common
%{systemd_user_post plasma-kwallet-pam.service}

%preun common
%{systemd_user_preun plasma-kwallet-pam.service}

%postun common
%{systemd_user_postun plasma-kwallet-pam.service}

%files
%license LICENSES/*
# Yes, it's still called pam_kwallet5. Not sure whether that's intentional,
# but it means PAM config doesn't need migration which is nice.
%if 0%{?suse_version} >= 1550
%{_pam_moduledir}/pam_kwallet5.so
%else
/%{_lib}/security/pam_kwallet5.so
%endif

%files common
%license LICENSES/*
%config %{_kf6_configdir}/autostart/pam_kwallet_init.desktop
%{_libexecdir}/pam_kwallet_init
%{_userunitdir}/plasma-kwallet-pam.service

%changelog
