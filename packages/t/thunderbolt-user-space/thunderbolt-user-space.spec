#
# spec file for package thunderbolt-user-space
#
# Copyright (c) 2020 SUSE LLC
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


Name:           thunderbolt-user-space
Version:        0.9.3
Release:        0
Summary:        Thunderbolt Device Approval support
License:        BSD-3-Clause
Group:          System/Management
URL:            https://github.com/intel/thunderbolt-software-user-space
Source:         https://github.com/01org/thunderbolt-software-user-space/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-flags-add-boost_system-library.patch
# Add support for Thunderbolt devices using Secure Connection in initramfs
Patch1:         0002-initramfs-support.patch
BuildRequires:  cmake >= 2.4.6
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libdbus-c++-devel
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig
BuildRequires:  txt2tags
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(udev)
Requires:       procps
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel >= 1.33.1
%endif

%description
Thunderbolt is a hardware interface developed by Intel/Apple that
allows the connection of external peripherals to a computer.

These user-space components implement device approval support:

* Interaction with the kernel module for approving connected devices.
* ACL for auto-approving devices white-listed by the user.

%prep
%setup -q -n thunderbolt-software-user-space-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake \
  -DBUILD_TESTING:BOOL=OFF \
  -DEVENT_DISABLE_TESTS=ON
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/thunderbolt-user-space

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license COPYING
%doc README.md docs
%{_bindir}/tbtadm
%{_udevrulesdir}/60-tbtacl.rules
%{_udevrulesdir}/60-tbtxdomain.rules
%dir %{_prefix}/lib/dracut/modules.d/35thunderbolt/
%{_prefix}/lib/dracut/modules.d/35thunderbolt/module-setup.sh
%{_prefix}/lib/udev/tbtacl
%{_prefix}/lib/udev/tbtacl-write
%{_prefix}/lib/udev/tbtxdomain
%{_mandir}/man1/tbtadm.1%{?ext_man}
%{_datadir}/bash-completion/completions/tbtadm
%config %{_sysconfdir}/dracut.conf.d/35-thunderbolt.conf

%changelog
