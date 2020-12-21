#
# spec file for package qore-xml-module
#
# Copyright (c) 2020 SUSE LLC
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


%define module_api %(qore --latest-module-api 2>/dev/null)

Name:           qore-xml-module
Version:        1.4.1
Release:        0
Summary:        XML module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source:         https://github.com/qorelanguage/module-xml/releases/download/v1.4.1/qore-xml-module-1.4.1.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.3
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the xml module for the Qore Programming Language.

XML is a markup language for encoding information.

%package doc
Summary:        Documentation and examples for the Qore xml module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%files doc
%defattr(-,root,root,-)
%doc docs/xml docs/XmlRpcHandler test examples

%prep
%setup -q

%build
%ifarch x86_64 ppc64 ppc64le s390x
c64=--enable-64bit
%endif
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug $c64
make %{?_smp_mflags}
find test -type f|xargs chmod 644
find docs -type f|xargs chmod 644

%install
mkdir -p %{buildroot}%{_datadir}/doc/qore-xml-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s docs

%files
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES
%{_bindir}/soaputil
%{_datadir}/qore-modules
%{_libdir}/qore-modules

%changelog
