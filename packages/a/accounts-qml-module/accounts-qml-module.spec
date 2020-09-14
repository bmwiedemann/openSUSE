#
# spec file for package accounts-qml-module
#
# Copyright (c) 2019 SUSE LLC
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
Version:        0.7
Release:        0
Summary:        QML bindings for libaccounts-qt + libsignon-qt
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
Source:         https://gitlab.com/accounts-sso/%{name}/-/archive/VERSION_%{version}/%{name}-VERSION_%{version}.tar.bz2
# PATCH-FIX-UPSTREAM
Patch0:         Fix-compilation-with-Qt-5.13.patch
# PATCH-FIX-UPSTREAM
Patch1:         Build-add-qmltypes-file-to-repository.patch
BuildRequires:  libqt5-qttools-doc
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(SignOnQt5)

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package doc
Summary:        Documentation for accounts-qml-module
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the developer documentation for accounts-qml-module.

%prep
%setup -q -n %{name}-VERSION_%{version}
%autopatch -p1
sed -e 's/-Werror//' -i common-project-config.pri

%build
mkdir build
pushd build
%qmake5 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    ..
%make_jobs
popd

%install
pushd build
%qmake5_install
popd

# remove tests
rm %{buildroot}%{_bindir}/tst_plugin
# avoid rpmlint warning
rm -f %{buildroot}/%{_datadir}/%{name}/doc/html/.gitignore

%files
%license COPYING
%doc README.md
%{_libqt5_archdatadir}/qml/Ubuntu

%files doc
%doc %{_datadir}/%{name}/

%changelog
