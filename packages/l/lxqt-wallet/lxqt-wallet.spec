#
# spec file for package lxqt-wallet
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


%define c_lib   lib%{name}6_0_0
%define srcname lxqt_wallet
Name:           lxqt-wallet
Version:        4.0.0
Release:        0
Summary:        Secure storage of information for LXQt
License:        BSD-2-Clause
Group:          System/GUI/LXQt
URL:            https://github.com/mhogomchungu/lxqt_wallet
Source0:        https://github.com/mhogomchungu/lxqt_wallet/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  cmake >= 3.18
BuildRequires:  gcc-c++
# Uses internal storage system
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-linguist-devel
BuildRequires:  cmake(KF5Notifications)
# Uses kwallet as backend
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
# Use libsecret as backend
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsecret-unstable)
Recommends:     %{name}-lang

%description
Secure storage of information in kwallet that can be presented in
key-values pair like user names-passwords pairs.

%package        -n %{c_lib}
Summary:        Library for %{name}
Group:          Development/Libraries/C and C++

%description    -n %{c_lib}
This package contains the library files for %{name}.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description    devel
This package contains the header files needed to develop application that
use %{name}.

%lang_package

%prep
%setup -q -n %{srcname}-%{version}

%build
%cmake \
    -DNOKDESUPPORT=false \
    -DNOSECRETSUPPORT=false

%make_build

%install
%cmake_install

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%license LICENSE
%doc README* changelog
%{_bindir}/lxqt_wallet-cli

%files devel
%{_includedir}/lxqt/
%{_libdir}/pkgconfig/lxqt-wallet.pc
%{_libdir}/liblxqt-wallet.so

%files -n %{c_lib}
%{_libdir}/liblxqt-wallet.so.*

%files lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations/
%dir %{_datadir}/lxqt/translations/lxqt-wallet/
%{_datadir}/lxqt/translations/lxqt-wallet/*.qm

%changelog
