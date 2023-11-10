#
# spec file for package lxqt-menu-data
#
# Copyright (c) 2023 SUSE LLC
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


Name:           lxqt-menu-data
Version:        1.4.1
Release:        0
Summary:        FD.O compliant menu files for LXQt
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-menu-data
Source0:        https://github.com/lxqt/lxqt-menu-data/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/lxqt-menu-data/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
BuildRequires:  cmake >= 3.1.0
BuildRequires:  lxqt-build-tools-devel >= 0.13.0
BuildRequires:  cmake(Qt5LinguistTools)
BuildArch:      noarch

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt.

%package -n %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} >= %{version}
Requires:       cmake
BuildArch:      noarch

%description -n %{name}-devel
lxqt-menu-data libraries for development

%prep
%autosetup

%build
%cmake -DPULL_TRANSLATIONS=No
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/*.menu
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*.directory

%files -n %{name}-devel
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/*.cmake

%changelog
