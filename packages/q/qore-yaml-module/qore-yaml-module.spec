#
# spec file for package qore-yaml-module
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules

Name:           qore-yaml-module
Version:        0.4
Release:        0
Summary:        YAML module for Qore
License:        LGPL-2.1+ or GPL-2.0+ or MIT
Group:          Development/Languages
Url:            http://qore.org
Source:         http://prdownloads.sourceforge.net/qore/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libyaml-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.5
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the yaml module for the Qore Programming Language.

YAML is a flexible and concise human-readable data serialization format.

%package doc
Summary:        Documentation and examples for the Qore yaml module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
yaml module.

%files doc
%defattr(-,root,root,-)
%doc docs/yaml docs/YamlRpcClient docs/YamlRpcHandler test examples

%prep
%setup -q
find examples -type f|xargs chmod 644

%build
%ifarch x86_64 ppc64 ppc64le x390x
c64=--enable-64bit
%endif
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug $c64
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{module_dir}
mkdir -p %{buildroot}%{_datadir}/doc/qore-yaml-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s docs

%files
%defattr(-,root,root,-)
%{module_dir}
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES ChangeLog AUTHORS

%changelog
