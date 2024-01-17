#
# spec file for package pam_csync
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


%if !%{defined _pam_moduledir}
%define _pam_moduledir /%{_lib}/security
%endif
Name:           pam_csync
Version:        0.43.0
Release:        0
Summary:        A PAM module for roaming home directories
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://www.csync.org/
Source0:        https://gitlab.com/csync/pam_csync/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM 0002-Update-FSF-address.patch
Patch2:         0002-Update-FSF-address.patch
BuildRequires:  cmake
BuildRequires:  libcsync-devel
BuildRequires:  libiniparser-devel
BuildRequires:  pam-devel

%description
This is a PAM module to provide roaming home directories for a user
session. The authentication module verifies the identity of a user and
triggers a synchronization with the server on the first login and the
last logout.

%prep
%autosetup -p1

%build
%cmake -DPAM_MODULE_INSTALL_DIR=%{_pam_moduledir}
%cmake_build

%install
%cmake_install

%files
%doc FAQ README
%license COPYING
%{_pam_moduledir}/pam_csync.so
%dir %{_sysconfdir}/security
%config(noreplace) %{_sysconfdir}/security/pam_csync.conf
%{_mandir}/man?/pam_csync.*

%changelog
