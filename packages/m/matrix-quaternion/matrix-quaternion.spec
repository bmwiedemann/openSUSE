#
# spec file for package matrix-quaternion
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


Name:           matrix-quaternion
Version:        0.0.95.84+git.20230827.3d7083a
Release:        0
Summary:        QT Matrix client
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/quotient-im/Quaternion
Source0:        https://github.com/quotient-im/Quaternion/archive/%{version}/matrix-quaternion-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Olm) >= 3.2.5
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(QtOlm)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core) >= 5.9
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(QuotientQt6) >= 0.8
BuildRequires:  pkgconfig(openssl)
Requires:       %{name}-lang
Conflicts:      matrix-quaternion
Provides:       matrix-quaternion = %{version}
Provides:       matrix-quaternion-git = %{version}
Provides:       quaternion = %{version}
Provides:       quaternion-git = %{version}
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc11-c++
%endif

%description
Quaternion is a desktop IM client for the Matrix protocol using QT.

%lang_package

%prep
%setup -q
# Wan't extern libQuotient package
rm -rf ./lib

%build
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=g++-11
%endif
%cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_WITH_QT6=ON \
   -DUSE_INTREE_LIBQOLM=OFF \
   -DQuotient_ENABLE_E2EE=ON
%make_jobs

%install
%cmake_install

%post -p /sbin/ldconfig
%if 0%{?suse_version} < 1500
%icon_theme_cache_post
%endif

%postun -p /sbin/ldconfig
%if 0%{?suse_version} < 1500
%icon_theme_cache_postun
%endif

%files
%license LICENSES
%doc README.md
%{_bindir}/quaternion
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/metainfo
%dir %{_datadir}/Quotient
%dir %{_datadir}/Quotient/quaternion
%{_datadir}/metainfo/*

%files lang
%{_datadir}/Quotient/quaternion/translations/

%changelog
