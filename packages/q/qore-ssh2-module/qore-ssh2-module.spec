#
# spec file for package qore-ssh2-module
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


%define qore_version 0.9.15
%define mod_ver 1.4.2
%if 0%{?sles_version}

%define dist .sles%{?sles_version}

%else
%if 0%{?suse_version}

# get *suse release major version
%define os_maj %(echo %suse_version|rev|cut -b3-|rev)
# get *suse release minor version without trailing zeros
%define os_min %(echo %suse_version|rev|cut -b-2|rev|sed s/0*$//)

%if %suse_version > 1010
%define dist .opensuse%{os_maj}_%{os_min}
%else
%define dist .suse%{os_maj}_%{os_min}
%endif

%endif
%endif

%define src_name module-ssh2-ssh2-release-%{version}
%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules
%define user_module_dir /usr/share/qore-modules
Name:           qore-ssh2-module
Version:        %{mod_ver}
Release:        1%{dist}
Summary:        SSH2 module for Qore
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-ssh2/releases/download/ssh2-release-%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 3.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libssh2-devel >= 1.1
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  qore >= 1.18
BuildRequires:  qore-devel >= 1.18
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Suggests:       %{name}-doc = %{version}

%description
This module provides access to ssh2 sessions and the sftp protocol
via libssh2 in the Qore programming language.


%if 0%{?suse_version}
%endif

%package doc
Summary:        Documentation and examples for the Qore SSH2 module
Group:          Development/Languages/Misc
BuildArch:      noarch

%description doc
SSH2 module for the Qore Programming Language.

This RPM provides API documentation, test and example programs

%files doc
%defattr(-,root,root,-)
%doc docs/ssh2/ docs/SftpPoller/ docs/SftpPollerUtil/ docs/Ssh2Connections/ test/

%prep
%setup -q

%build
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
make %{?_smp_mflags} docs

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes %{buildroot}%{_datadir}
# Fix docs installed by RPM
%fdupes -s build/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{module_dir}
%{user_module_dir}
%license COPYING.LGPL COPYING.MIT README RELEASE-NOTES AUTHORS
%{_libdir}/qore-modules/*

%changelog
