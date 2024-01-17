#
# spec file for package qmlpluginexports
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

%if "%{qt_version}" == ""
Name:           qmlpluginexports
%else
Name:           qmlpluginexports-%{qt_version}
%endif
Version:        1.0
Release:        0
Summary:        Tool to list exports provided by QML plugins
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://www.opensuse.org
Source0:        LICENSE
Source1:        qmlpluginexports.cpp
Source2:        qmlpluginexports.pro
#!BuildIgnore:  qml-autoreqprov
%if "%{qt_version}" == "qt6"
BuildRequires:  qt6-declarative-private-devel
%else
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
%endif
%if "%{qt_version}" == ""
ExclusiveArch:  do_not_build
%endif

%description
This tools loads a QML plugin and prints a list of identifiers and versions
to stdout. See qml-autoreqprov's README for details.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%if "%{qt_version}" == "qt6"
%qmake6 .
%qmake6_build
%else
%qmake5 .
%make_jobs
%endif

%install
install -D -m 755 qmlpluginexports %{buildroot}%{_bindir}/qmlpluginexports-%{qt_version}

%files
%license LICENSE
%{_bindir}/qmlpluginexports-%{qt_version}

%changelog
