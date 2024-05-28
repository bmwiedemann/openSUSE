#
# spec file for package qore-openldap-module
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


%define mod_ver 1.2.3
%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules

%if 0%{?sles_version}

%define dist .sles%{?sles_version}

%else
%if 0%{?suse_version}

# get *suse release major version
%define os_maj %(echo %suse_version|rev|cut -b3-|rev)
# get *suse release minor version without trailing zeros
%define os_min %(echo %suse_version|rev|cut -b-2|rev|sed s/0*$//)

%if %suse_version
%define dist .opensuse%{os_maj}_%{os_min}
%endif

%endif
%endif

Summary:        OPENLDAP module for Qore
Name:           qore-openldap-module
Version:        %{mod_ver}
Release:        1%{dist}
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Languages
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-openldap/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
BuildRequires:  gcc-c++
BuildRequires:  qore-devel >= 1.12.4
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  openldap2-devel
%else
BuildRequires:  openldap-devel
%endif
BuildRequires:  cmake >= 3.5
BuildRequires:  doxygen
BuildRequires:  qore >= 1.12.4

%description
This package contains the openldap module for the Qore Programming Language.

This module exposes functionality from the openldap library as a Qore API.

%if 0%{?suse_version}
%debug_package
%endif

%package doc
Summary:        Documentation and examples for the Qore openldap module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
openldap module.

%files doc
%defattr(-,root,root,-)
%doc docs/openldap test

%prep
%setup -q

%build
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
make %{?_smp_mflags} docs
sed -i 's/#!\/usr\/bin\/env qore/#!\/usr\/bin\/qore/' test/q*

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{module_dir}
%doc README RELEASE-NOTES AUTHORS
%license COPYING.MIT COPYING.LGPL

%changelog
