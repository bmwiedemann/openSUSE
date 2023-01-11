#
# spec file for package libqt5-qtgraphicaleffects
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


%define qt5_snapshot 1
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtgraphicaleffects-everywhere-src-%{version}
Name:           libqt5-qtgraphicaleffects
Version:        5.15.8+kde0
Release:        0
Summary:        Qt 5 Graphical Effects
# Legal: the 'tools' folder is not built.
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
BuildRequires:  libqt5-qtdeclarative-devel >= %{real_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{real_version}
BuildRequires:  xz
%requires_ge    libQtQuick5
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%prep
%autosetup -p1 -n %{tar_version}

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

%files
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtGraphicalEffects

%changelog
