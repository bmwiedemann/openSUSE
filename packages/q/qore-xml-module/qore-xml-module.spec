#
# spec file for package qore-xml-module
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


%global mod_ver 1.5.3

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

%if %suse_version > 1010
%global dist .opensuse%{os_maj}_%{os_min}
%else
%global dist .suse%{os_maj}_%{os_min}
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
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Other
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-xml/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/bin/env
Requires:       qore-module(abi)%{?_isa} = %{module_api}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9.4
#Because of file conflict with qore-xml-module-tools-1.5.1+qore1.0.10-1.3
Obsoletes:      %{name}-tools  < %{version}

%description
This package contains the xml module for the Qore Programming Language.

XML is a markup language for encoding information.

%if 0%{?suse_version}
%endif

%package doc
Summary:        Documentation and examples for the Qore xml module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%files doc
%defattr(-,root,root,-)
%doc docs/xml docs/XmlRpcHandler docs/SalesforceSoapClient docs/SoapClient docs/SoapDataProvider docs/SoapHandler docs/WSDL docs/XmlRpcConnection test examples

%prep
%setup -q
./configure RPM_OPT_FLAGS="$RPM_OPT_FLAGS" --prefix=/usr --disable-debug

%build
%{__make}
find test -type f|xargs chmod 644
find docs -type f|xargs chmod 644

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{module_dir}
mkdir -p $RPM_BUILD_ROOT/%{user_module_dir}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/qore-xml-module
make install DESTDIR=$RPM_BUILD_ROOT
%fdupes -s %{__builddir}/html
# Fix scripts
find examples -name "*.q" -exec sed -i '1 s/env qore/qore/' \{\} +
for f in "%{buildroot}%{_bindir}/"{soaputil,webdav-server}; do sed -i '1 s/env qore/qore/' "$f"; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{module_dir}
%{user_module_dir}
%{_bindir}/soaputil
%{_bindir}/webdav-server
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES AUTHORS

%changelog
