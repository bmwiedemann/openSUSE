#
# spec file for package qore-ssh2-module
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


%define qore_version 0.9.15
%define mod_ver 1.4.1
%define src_name module-ssh2-ssh2-release-%{version}
%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules
%define user_module_dir /usr/share/qore-modules
Name:           qore-ssh2-module
Version:        1.4.1
Release:        0
Summary:        SSH2 module for Qore
License:        LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-ssh2/releases/download/ssh2-release-%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libssh2-devel >= 1.1
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9.0
Requires:       /usr/bin/env
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
%setup -q
./configure RPM_OPT_FLAGS="$RPM_OPT_FLAGS" --prefix=/usr --disable-debug

%build
%{__make}
%make_build docs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{module_dir}
mkdir -p $RPM_BUILD_ROOT/%{user_module_dir}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/qore-ssh2-module
make install DESTDIR=$RPM_BUILD_ROOT
%fdupes %{buildroot}%{_datadir}
# Fix docs installed by RPM
%fdupes -s build/docs

%files
%defattr(-,root,root,-)
%{module_dir}
%{user_module_dir}
%license COPYING.LGPL COPYING.MIT README RELEASE-NOTES AUTHORS
%{_libdir}/qore-modules/*

%files doc
%defattr(-,root,root,-)
%doc docs/ssh2/ docs/SftpPoller/ test/

%changelog
