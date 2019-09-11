#
# spec file for package thunderbolt-user-space
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


Name:           thunderbolt-user-space
Version:        0.9.3
Release:        0
Summary:        Thunderbolt Device Approval support
License:        BSD-3-Clause
Group:          System/Management
Url:            https://github.com/01org/thunderbolt-software-user-space/archive/v%{version}.tar.gz
Source:         v0.9.3.tar.gz
Patch0:         0001-flags-add-boost_system-library.patch
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel >= 1.33.1
%endif
BuildRequires:  cmake >= 2.4.6
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libdbus-c++-devel
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig
BuildRequires:  txt2tags
BuildRequires:  pkgconfig(udev)
Requires:       procps

%description
Thunderbolt is a hardware interface developed by Intel/Apple that
allows the connection of external peripherals to a computer.

These user-space components implement device approval support:

* Interaction with the kernel module for approving connected devices.
* ACL for auto-approving devices white-listed by the user.

%prep
%setup -q -n thunderbolt-software-user-space-%{version}
%patch0 -p1

%build
%cmake \
	-DBUILD_TESTING:BOOL=OFF \
	 -DBUILD_SHARED_LIBS:BOOL=ON \
	 -DEVENT_DISABLE_TESTS=ON \
../
make %{?_smp_mflags}

%install
%cmake_install 

%files
%dir %{_datadir}/doc/thunderbolt-user-space

%{_bindir}/tbtadm
%{_udevrulesdir}/60-tbtacl.rules
%{_udevrulesdir}/60-tbtxdomain.rules
%{_prefix}/lib/udev/tbtacl
%{_prefix}/lib/udev/tbtacl-write
%{_prefix}/lib/udev/tbtxdomain
%{_datadir}/doc/thunderbolt-user-space/copyright
%{_mandir}/man1/tbtadm.1%{ext_man}
%{_datadir}/bash-completion/completions/tbtadm

%changelog
