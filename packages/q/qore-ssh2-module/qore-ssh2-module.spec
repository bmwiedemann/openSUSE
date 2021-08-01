#
# spec file for package qore-ssh2-module
#
# Copyright (c) 2021 SUSE LLC
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


%define qore_version 0.9.15
%define src_name module-ssh2-release-%{qore_version}
%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-ssh2-module
Version:        1.3.0+qore%{qore_version}
Release:        0
Summary:        SSH2 module for Qore
License:        LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-ssh2/archive/refs/tags/release-%{qore_version}.tar.gz#/%{src_name}.tar.gz
# PATCH-FIX-UPSTREAM cmake-fix-missing-pthread.patch -- https://github.com/qorelanguage/module-ssh2/pull/106
Patch0:         cmake-fix-missing-pthread.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9.0
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(openssl)
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Suggests:       %{name}-doc = %{version}

%description
This module provides access to ssh2 sessions and the sftp protocol
via libssh2 in the Qore programming language.

%package doc
Summary:        Documentation and examples for the Qore SSH2 module
Group:          Development/Languages/Misc
Requires:       %{name} = %{version}

%description doc
SSH2 module for the Qore Programming Language.

This RPM provides API documentation, test and example programs

%prep
%setup -q -n %{src_name}
%patch0 -p1

%build
%cmake
%make_build docs

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}
# Fix docs installed by RPM
%fdupes -s build/docs


%files
%license COPYING.LGPL COPYING.MIT
%{_libdir}/qore-modules/*
%{_datadir}/qore-modules/SftpPoller.qm
%{_datadir}/qore-modules/SftpPollerUtil.qm
%{_datadir}/qore-modules/Ssh2Connections.qm

%files doc
%doc README build/docs/*

%changelog
