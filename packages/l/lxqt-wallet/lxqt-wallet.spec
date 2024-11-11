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


%if 0%{?suse_version} >= 1699
%bcond_without kwallet
%endif
%define c_lib   lib%{name}6_0_0
Name:           lxqt-wallet
Version:        4.0.2
Release:        0
Summary:        Secure storage of information for LXQt
License:        BSD-2-Clause
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt_wallet
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# Uses kwallet as backend
%if %{with kwallet}
BuildRequires:  cmake(KF6Wallet)
%endif
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
# Uses internal storage system
BuildRequires:  pkgconfig(libgcrypt)
# Use libsecret as backend
BuildRequires:  pkgconfig(libsecret-1)
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
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%find_lang %{name} --with-qt

%ldconfig_scriptlets -n %{c_lib}

%files
%doc changelog README.md
%{_bindir}/lxqt_wallet-cli
%license LICENSE

%files devel
%dir %{_includedir}/lxqt/
%{_includedir}/lxqt/lxqt?wallet.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{c_lib}
%{_libdir}/lib%{name}.so.*

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
