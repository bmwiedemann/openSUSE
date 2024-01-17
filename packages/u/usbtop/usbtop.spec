#
# spec file for package usbtop
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


Name:           usbtop
Version:        1.0
Release:        1%{?dist}
Summary:        Visualizer for estimated instantaneous bandwidth on USB buses and devices
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://github.com/aguinet/usbtop
Source0:        https://github.com/aguinet/usbtop/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel >= 1.48.0
BuildRequires:  libboost_system-devel >= 1.48.0
BuildRequires:  libboost_thread-devel >= 1.48.0
BuildRequires:  libpcap-devel

%description
A top-like utility that shows an estimated instantaneous bandwidth on USB buses and devices.

Requires the usbmon kernel module to be loaded.

%prep
%setup -q -n %{name}-release-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
install -Dm 755 build/src/usbtop %{buildroot}%{_bindir}/usbtop

%files
%doc README.md
%license LICENSE
%{_bindir}/usbtop

%changelog
