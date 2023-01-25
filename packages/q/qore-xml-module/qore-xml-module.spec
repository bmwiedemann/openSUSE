#
# spec file for package qore-xml-module
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


%global mod_ver 1.8.0

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

# see if we can determine the distribution type
%if 0%{!?dist:1}
%global rh_dist %(if [ -f /etc/redhat-release ];then cat /etc/redhat-release|sed "s/[^0-9.]*//"|cut -f1 -d.;fi)
%if 0%{?rh_dist}
%global dist .rhel%{rh_dist}
%else
%global dist .unknown
%endif
%endif

Summary:        XML module for Qore
Name:           qore-xml-module
Version:        %{mod_ver}
Release:        1%{dist}
License:        MIT
Group:          Development/Languages/Other
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-xml/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  qore >= 1.12.4
BuildRequires:  qore-devel >= 1.12.4
BuildRequires:  qore-stdlib >= 1.12.4
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  timezone
%else
BuildRequires:  tzdata
%endif

%description
This package contains the xml module for the Qore Programming Language.

XML is a markup language for encoding information.

%if 0%{?suse_version}
%endif

%package doc
Summary:        Documentation and examples for the Qore xml module
Group:          Development/Languages
BuildArch:      noarch

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%files doc
%defattr(-,root,root,-)
%doc docs/xml docs/XmlRpcHandler docs/SalesforceSoapClient docs/SaxDataProvider docs/SoapClient docs/SoapDataProvider docs/SoapHandler docs/WSDL docs/XmlRpcConnection test examples

%prep
%setup -q

%build
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
%{__make}
%{__make} docs
sed -i 's/#!\/usr\/bin\/env qore/#!\/usr\/bin\/qore/' test/*.qtest bin/soaputil bin/webdav-server test/disabled/GlobalWeather.qtest.disabled examples/*.q

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s %{__builddir}/html docs

%files
%defattr(-,root,root,-)
%{module_dir}
%{user_module_dir}
%{_bindir}/soaputil
%{_bindir}/webdav-server
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES AUTHORS

%changelog
