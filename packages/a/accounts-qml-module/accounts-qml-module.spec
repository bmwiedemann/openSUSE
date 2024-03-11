#
# spec file for package accounts-qml-module
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


Name:           accounts-qml-module
Version:        0.7git.20231028T182937~05e79eb
Release:        0
Summary:        QML bindings for libaccounts-qt and libsignon-qt
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
Source:         %{name}-%{version}.tar.xz
BuildRequires:  qt6-tools-qdoc
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(SignOnQt6)

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package doc
Summary:        Documentation for accounts-qml-module
BuildArch:      noarch

%description doc
This package contains the developer documentation for accounts-qml-module.

%prep
%autosetup -p1

%build
%qmake6

%qmake6_build

%install
%qmake6_install

# Delete test executable
rm %{buildroot}%{_bindir}/tst_plugin

# Fix rpmlint warning
rm %{buildroot}%{_qt6_sharedir}/accounts-qml-module/doc/html/.gitignore

%files
%license COPYING
%doc README.md
%dir %{_qt6_qmldir}/SSO
%{_qt6_qmldir}/SSO/OnlineAccounts/

%files doc
%doc %{_qt6_sharedir}/accounts-qml-module/

%changelog
