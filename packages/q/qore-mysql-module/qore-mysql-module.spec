#
# spec file for package qore-mysql-module
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
%define src_name module-mysql-release-%{qore_version}
%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-mysql-module
Version:        2.0.2.1+qore%{qore_version}
Release:        0
Summary:        MySQL DBI module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later
Group:          Development/Languages/Other
Url:            https://qore.org
Source:         https://github.com/qorelanguage/module-mysql/archive/release-%{qore_version}/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libmysqlclient-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9
Requires:       %{_bindir}/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
MySQL DBI driver module for the Qore Programming Language. The MySQL driver is
character set aware and supports multithreading, transaction management, and
stored procedure execution.

%package doc
Summary:        MySQL DBI module for Qore
Group:          Development/Languages/Other
BuildArch:      noarch

%description doc
MySQL module for the Qore Programming Language.

This package provides API documentation, and example programs

%prep
%setup -q -n %{src_name}

%build
%cmake
%cmake_build
make %{?_smp_mflags} docs

%install
%cmake_install
%fdupes -s %{__builddir}/html

%files
%license COPYING.GPL COPYING.LGPL
%doc README RELEASE-NOTES AUTHORS
%{_libdir}/qore-modules

%files doc
%doc %{__builddir}/html

%changelog
