#
# spec file for package libyaml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libyaml
Version:        0.2.2
Release:        0
Summary:        A YAML 1.1 parser and emitter written in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://pyyaml.org/wiki/LibYAML
Source:         http://pyyaml.org/download/libyaml/yaml-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
A YAML 1.1 parser and emitter written in C

%define lib_name libyaml-0-2

%package -n %{lib_name}
Summary:        A YAML 1.1 parser and emitter written in C
Group:          System/Libraries

%description -n %{lib_name}
This package holds the shared library of libyaml.

%package devel
Summary:        Development files for libyaml
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
This package holds the development files for libyaml,
a YAML 1.1 parser and emitter written in C.

%prep
%setup -q -n yaml-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%{_libdir}/libyaml-0.so.2
%{_libdir}/libyaml-0.so.2.0.*

%files devel
%{_includedir}/yaml.h
%{_libdir}/libyaml.so
%{_libdir}/pkgconfig/yaml-0.1.pc

%changelog
