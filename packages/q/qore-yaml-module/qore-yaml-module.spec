#
# spec file for package qore-yaml-module
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


%{?_datarootdir: %global mydatarootdir %_datarootdir}
%{!?_datarootdir: %global mydatarootdir /usr/share}

%global module_api %(qore --latest-module-api 2>/dev/null)
%global module_dir %{_libdir}/qore-modules
%global user_module_dir %{mydatarootdir}/qore-modules/

%if 0%{?sles_version}

%global dist .sles%{?sles_version}

%else
%if 0%{?suse_version}

# get *suse release major version
%global os_maj %(echo %suse_version|rev|cut -b3-|rev)
# get *suse release minor version without trailing zeros
%global os_min %(echo %suse_version|rev|cut -b-2|rev|sed s/0*$//)

%if %suse_version
%global dist .opensuse%{os_maj}_%{os_min}
%endif

%endif
%endif

%define src_name qore-yaml-module-%{version}
Name:           qore-yaml-module
Version:        0.7.3
Release:        0
Summary:        YAML module for Qore
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-yaml/releases/download/v%{version}/%{name}-%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
BuildRequires:  cmake >= 3.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libyaml-devel
BuildRequires:  timezone
BuildRequires:  qore >= 1.12.4
BuildRequires:  qore-devel >= 1.12.4
BuildRequires:  qore-stdlib >= 1.12.4
Suggests:       %{name}-doc = %{version}

%description
This package contains the yaml module for the Qore Programming Language.

YAML is a flexible and concise human-readable data serialization format.

%if 0%{?suse_version}
%endif

%package doc
Summary:        Documentation and examples for the Qore yaml module
Group:          Development/Languages/Misc
BuildArch:      noarch

%description doc
This package contains the HTML documentation and example programs for the Qore
yaml module.

%files doc
%defattr(-,root,root)
%doc docs/yaml docs/YamlRpcClient docs/YamlRpcHandler docs/DataStreamUtil docs/DataStreamClient docs/DataStreamRequestHandler test examples

%prep
%setup -q -n %{src_name}
find examples -type f|xargs chmod 644

%build
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
make %{?_smp_mflags} docs
sed -i 's/#!\/usr\/bin\/env qore/#!\/usr\/bin\/qore/' test/*.qtest examples/*

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s %{__builddir}/html docs

%files
%defattr(-,root,root)
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES AUTHORS
%{module_dir}
%{user_module_dir}

%check
export QORE_MODULE_DIR=$QORE_MODULE_DIR:qlib
qore -l ./yaml-api-1.3.qmod test/DataStreamClient.qtest -v
qore -l ./yaml-api-1.3.qmod test/DataStreamHandler.qtest -v
qore -l ./yaml-api-1.3.qmod test/DataStreamUtil.qtest -v
qore -l ./yaml-api-1.3.qmod test/YamlRpcHandler.qtest -v
qore -l ./yaml-api-1.3.qmod test/yaml.qtest -v

%changelog
