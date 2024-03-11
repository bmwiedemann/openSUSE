#
# spec file for package signon-plugin-oauth2
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


Name:           signon-plugin-oauth2
Version:        0.25git.20231124T142245~fab6988
Release:        0
Summary:        Oauth2 plugin for the Single Sign On Framework
License:        LGPL-2.0-only
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsignon-qt6)
BuildRequires:  pkgconfig(signon-plugins)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Test)
# Needs QtWebengine
%ifarch x86_64 aarch64 riscv64
Requires:       signon-ui
%endif

%description
This package contains the Oauth2 plugin for the Single Sign On Framework.

%package devel
Summary:        Development files for signon-plugin-oauth2
Requires:       %{name} = %{version}

%description devel
This package contains the development files for the Oauth2 plugin for the Single
Sign On Framework.

%prep
%autosetup -p1

sed -i 's#/lib#/%{_lib}#g' src/signon-oauth2plugin.pc
sed -i 's#lib/#%{_lib}/#' src/src.pro

%build
# Reminder: adding build flavors is not needed for signon plugins
# See signon spec file for details
%qmake6 \
  LIBDIR=%{_libdir} \
  QMAKE_CXXFLAGS+="-Wno-error=deprecated-declarations"

%qmake6_build

%install
%qmake6_install

# Remove examples and tests
rm -r %{buildroot}%{_bindir} %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%dir %{_qt6_libdir}/signon/
%{_qt6_libdir}/signon/liboauth2plugin.so

%files devel
%dir %{_includedir}/signon-plugins/
%{_includedir}/signon-plugins/*.h
%{_qt6_pkgconfigdir}/signon-oauth2plugin.pc

%changelog
