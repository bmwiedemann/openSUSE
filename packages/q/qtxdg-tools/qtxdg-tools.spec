#
# spec file for package qtxdg-tools
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


Name:           qtxdg-tools
Version:        4.0.0
Release:        0
Summary:        User tools for libqtxg
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://github.com/lxqt/qtxdg-tools
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= 6.6.0
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(Qt6Xdg)
Requires:       xdg-utils

%description
User tools for libqtxdg.
qtxdg-tools contains a CLI MIME tool, qtxdg-mat, for handling file
associations and opening files with their default applications.
It is maintained by the LXQt project and needed by LXQt Session, in order
to be used by xdg-utils. Yet it can be used independently from LXQt, too.

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%files
%doc CHANGELOG README.md
%{_bindir}/qtxdg-mat
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/%{name}-config*.cmake
%{_datadir}/cmake/%{name}/%{name}-targets*.cmake
%license LICENSE

%changelog
