#
# spec file for package libqt5-qtgraphicaleffects
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define qt5_snapshot 0

Name:           libqt5-qtgraphicaleffects
Version:        5.13.0
Release:        0
Summary:        Qt 5 Graphical Effects
License:        BSD-3-Clause and (LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0)
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtgraphicaleffects-everywhere-src-5.13.0
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  libqt5-qtdeclarative-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
%requires_ge libQtQuick5

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%prep
%setup -q -n %{tar_version}

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

%files
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtGraphicalEffects

%changelog
