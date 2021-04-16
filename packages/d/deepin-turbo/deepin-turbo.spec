#
# spec file for package deepin-turbo
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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

%define  sover  0

Name:           deepin-turbo
Version:        0.0.5
Release:        0
License:        LGPL-2.1+
Summary:        A screenshot tool
Url:            https://github.com/linuxdeepin/deepin-turbo
Group:          Productivity/Graphics/Convertors
Source:         https://github.com/linuxdeepin/deepin-turbo/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
This is a default screenshot app for Linux Deepin.

%package -n lib%{name}%{sover}
Summary:        Deepin Turbo libraries
Group:          System/Libraries

%description -n lib%{name}%{sover}
The package provides libraries for deepin-turbo.

%package devel
Summary:        Development tools for deepin turbo
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel
The deepin-turbo-devel package contains the header files for deepin-turbo.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake

%install
%cmake_install

%pre
%service_add_pre %{name}-booster-dtkwidget.service %{name}-booster-desktop.service

%post
%service_add_post %{name}-booster-dtkwidget.service %{name}-booster-desktop.service

%preun
%service_del_preun %{name}-booster-dtkwidget.service %{name}-booster-desktop.service

%postun
%service_del_postun %{name}-booster-dtkwidget.service %{name}-booster-desktop.service

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc README.md CHANGELOG
%license COPYING.LESSER
%{_bindir}/%{name}-single-instance
%{_bindir}/%{name}-invoker
%{_prefix}/lib/%{name}
%dir %{_prefix}/lib/binfmt.d
%{_prefix}/lib/binfmt.d/desktop.conf
%{_prefix}/lib/systemd/user/%{name}-booster-desktop.service
%{_prefix}/lib/systemd/user/%{name}-booster-dtkwidget.service

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog

