#
# spec file for package kchmviewer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kchmviewer
Version:        7.7
Release:        0
Summary:        KDE CHM Viewer
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            http://www.kchmviewer.net/
Source:         http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-build.patch
Patch0:         fix-build.patch
BuildRequires:  chmlib-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libzip)

%description
This is a viewer for the CHM files which are used for end user
documentation (MS Windows Compressed HTML Documents). It supports
complex searching for large books and has various viewing features.

%prep
%autosetup -p1

%build
%qmake5
%make_jobs

%install
mkdir -p %{buildroot}%{_bindir}
install bin/kchmviewer %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
install packages/kchmviewer.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install packages/kchmviewer.png %{buildroot}%{_datadir}/pixmaps

%files
%license COPYING
%doc ChangeLog FAQ README
%{_bindir}/kchmviewer
%{_datadir}/applications/kchmviewer.desktop
%{_datadir}/pixmaps/kchmviewer.*

%changelog
