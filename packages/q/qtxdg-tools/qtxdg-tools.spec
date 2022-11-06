#
# spec file for package qtxdg-tools
#
# Copyright (c) 2022 SUSE LLC
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
Version:        3.10.0
Release:        0
Summary:        User tools for libqtxg
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.11.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.15
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.9.0
BuildRequires:  pkgconfig(glib-2.0)

%description
User tools for libqtxdg.
qtxdg-tools contains a CLI MIME tool, qtxdg-mat, for handling file associations and opening files with their default applications.
It is maintained by the LXQt project and needed by LXQt Session, in order to be used by xdg-utils. Yet it can be used independently from LXQt, too.

%prep
%setup -q

%build
%cmake

%install
%cmake_install

%files
%{_bindir}/qtxdg-mat
%dir %{_datadir}/cmake/qtxdg-tools
%{_datadir}/cmake/qtxdg-tools/*.cmake

%changelog
