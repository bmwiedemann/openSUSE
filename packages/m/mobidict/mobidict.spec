#
# spec file for package mobidict
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


Name:           mobidict
Version:        1.2
Release:        0
Summary:        A dictionary viewer for AZW/MOBI files
License:        GPL-3.0-only
Group:          Productivity/Office/Dictionary
Url:            https://github.com/ismail/mobidict
Source:         https://github.com/ismail/mobidict/releases/download/v%{version}/mobidict-%{version}.tar.xz
Source1:        https://github.com/ismail/mobidict/releases/download/v%{version}/mobidict-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.9.2
BuildRequires:  ninja
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A dictionary viewer for AZW/MOBI files.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -std=c11"
%define __builder ninja
%cmake

%install
%cmake_install

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/mobidict
%{_datadir}/pixmaps/mobidict.png
%{_datadir}/applications/mobidict.desktop

%changelog
