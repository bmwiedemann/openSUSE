#
# spec file for package qore-json-module
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


%define mod_ver 1.8.2

%{?_datarootdir: %global mydatarootdir %_datarootdir}
%{!?_datarootdir: %global mydatarootdir /usr/share}

%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules
%global user_module_dir %{mydatarootdir}/qore-modules/

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

# see if we can determine the distribution type
%if 0%{!?dist:1}
%define rh_dist %(if [ -f /etc/redhat-release ];then cat /etc/redhat-release|sed "s/[^0-9.]*//"|cut -f1 -d.;fi)
%if 0%{?rh_dist}
%define dist .rhel%{rh_dist}
%else
%define dist .unknown
%endif
%endif

Summary:        JSON module for Qore
Name:           qore-json-module
Version:        %{mod_ver}
Release:        1%{dist}
License:        MIT
Group:          Development/Languages
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-json/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
BuildRequires:  cmake >= 3.5
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel
BuildRequires:  qore >= 1.12.4
BuildRequires:  qore-devel >= 1.12.4
BuildRequires:  qore-stdlib >= 1.12.4

%description
This package contains the json module for the Qore Programming Language.

JSON is a concise human-readable data serialization format.

%if 0%{?suse_version}
%endif

%prep
%setup -q

%build
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
make %{?_smp_mflags} docs
sed -i 's/#!\/usr\/bin\/env qore/#!\/usr\/bin\/qore/' test/*.qtest examples/*
%if 0%{?suse_version}
#%fdupes -s docs/json
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}
#chmod 0755 /usr/lib64/qore-modules/json-api-1.3.qmod

%files
%defattr(-,root,root,-)
%{module_dir}
%{user_module_dir}
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES AUTHORS

%check
qore -l ./json-api-1.3.qmod test/JsonRpcClient.qtest -v
qore -l ./json-api-1.3.qmod test/JsonRpcHandler.qtest -v
qore -l ./json-api-1.3.qmod test/json.qtest -v

%package doc
Summary:        JSON module for Qore
Group:          Development/Languages
BuildArch:      noarch

%description doc
This package contains the HTML documentation and example programs for the Qore
json module.

%files doc
%defattr(-,root,root,-)
%doc docs/json docs/JsonRpcConnection docs/JsonRpcHandler test examples

%changelog
