#
# spec file for package qtdeclarative-imports-provides
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


%global qt_version @BUILD_FLAVOR@%nil

# Doesn't build, but makes factory-auto happy.
%if "%{qt_version}" == ""
Name:           qtdeclarative-imports-provides
%else
Name:           qtdeclarative-imports-provides-%{qt_version}
%endif
Version:        1.0
Release:        0
Summary:        RPM provides for QML modules from qtdeclarative
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://www.opensuse.org
Source0:        LICENSE
BuildRequires:  qml-autoreqprov
%if "%{qt_version}" == "qt6"
%global pkgname qt6-declarative-imports
%else
%global pkgname libQtQuick5
%endif
BuildRequires:  qmlpluginexports-%{qt_version}
BuildRequires:  %{pkgname}
%requires_eq %{pkgname}
%if "%{qt_version}" == ""
ExclusiveArch:  do_not_build
%endif
%(rpm -ql %{pkgname} | grep '/qmldir$' | %{_rpmconfigdir}/qmldirreqprov.sh --provides | sed 's/^/Provides: /')

%description
A separately built package to avoid a build cycle.

%prep
cp %{SOURCE0} .

%build

%install

%files
%license LICENSE

%changelog
