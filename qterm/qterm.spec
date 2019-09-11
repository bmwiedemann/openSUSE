#
# spec file for package qterm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qterm
Version:        0.7.3
Release:        0
Summary:        QTerm is BBS client
License:        GPL-2.0-or-later
Group:          System/X11/Terminals
Url:            https://github.com/qterm/qterm
Source0:        https://github.com/qterm/%{name}/archive/%{version}.tar.gz#./%{name}-%{version}.tar.gz
Source1:        qterm.desktop
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - qcollectiongenerator has been merged into qhelpgenerator in Qt 5.12.0
Patch:          qterm-qt5qcollectiongenerator.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(openssl)

%description
QTerm is a full featured BBS client written in Qt.

%prep
%setup -q
%patch -p1

%build
%cmake -DQT5=YES
%make_jobs

%install
%cmake_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/
%fdupes -s %{buildroot}

%files
%{_datadir}/qterm
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_bindir}/*

%changelog
