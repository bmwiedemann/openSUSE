#
# spec file for package libsysstat
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


%define  sover  1
Name:           libsysstat
Version:        1.0.0
Release:        0
Summary:        Library used to query system info and statistics
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/lxqt/libsysstat
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6
BuildRequires:  cmake(lxqt2-build-tools) >= 2.0.0

%description
libsysstat is a library to query system information like CPU and memory
usage or network traffic. libsysstat is used by plugin-sysstat of
lxqt-panel.

%package -n %{name}%{sover}
Summary:        Libraries for lxqt
Group:          System/Libraries
Provides:       %{name}

%description -n %{name}%{sover}
Development libraries for libsysstat

%package devel
Summary:        Devel files for libsysstat
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       pkgconfig

%description devel
sysstat libraries for development

%prep
%autosetup -p1

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%doc AUTHORS CHANGELOG README.md
%{_libdir}/%{name}-qt6.so.*
%license COPYING

%files devel
%{_includedir}/sysstat-qt6
%{_datadir}/cmake/sysstat-qt6
%{_libdir}/pkgconfig/sysstat-qt6.pc
%{_libdir}/%{name}-qt6.so

%changelog
