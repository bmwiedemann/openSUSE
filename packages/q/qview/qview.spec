#
# spec file for package qview
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


Name:           qview
Version:        2.0
Release:        0
Summary:        Practical and minimal image viewer
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://interversehq.com/qview/
Source:         https://github.com/jurplel/qView/archive/%{version}.tar.gz#/qView-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9

%description
qView is a Qt image viewer designed with minimalism and usability in mind.
No cluttered interface, just your image and a titlebar.

%prep
%setup -q -n qView-%{version}

%build
%qmake5
%make_build

%install
INSTALL_ROOT=%{buildroot} %make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/*

%changelog
