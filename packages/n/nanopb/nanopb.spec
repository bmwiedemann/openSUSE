#
# spec file for package nanopb
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


%define sover 0
%define src_install_dir %{_prefix}/src/%{name}
Name:           nanopb
Version:        0.4.7
Release:        0
Summary:        Protocol Buffers with small code size
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://jpa.kapsi.fi/nanopb/
Source:         https://github.com/nanopb/nanopb/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  protobuf-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-setuptools

%description
Nanopb is a C implementation of Google's Protocol Buffers data format. It is
targeted at 32 bit microcontrollers, but is also fit for other embedded systems
with tight (2-10 kB ROM, <1 kB RAM) memory constraints.

%package -n libprotobuf-nanopb%{sover}
Summary:        Shared library for nanopb
Group:          System/Libraries

%description -n libprotobuf-nanopb%{sover}
Shared library for nanopb - a C implementation of Google's Protocol Buffers
data format.

%package devel
Summary:        Development files for nanopb
Group:          Development/Libraries/C and C++
Requires:       libprotobuf-nanopb%{sover} = %{version}

%description devel
Development files for nanopb - a C implementation of Google's Protocol Buffers
data format.

%package source
Summary:        Source code of nanopb
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description source
Source code of nanopb - a C implementation of Google's Protocol Buffers data
format.

%prep
%autosetup

%build
%cmake \
  -DCMAKE_C_FLAGS=-DPB_ENABLE_MALLOC=1
%cmake_build

%install
%cmake_install
# Install source code
mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
find %{buildroot}%{src_install_dir} -name ".*" -exec rm -rfv \{\} +
# Fix env-script-interpreter rpmlint error
files=$(grep -rl '#!/usr/bin/env python' %{buildroot}%{src_install_dir}) && echo $files | xargs sed -i 's|#!/usr/bin/env python|#!%{_bindir}/python|'
# Fix name and interpreter
ln -s %{_bindir}/nanopb_generator.py %{buildroot}%{_bindir}/nanopb_generator
sed -i 's|env python3|python3|' %{buildroot}%{_bindir}/nanopb_generator.py

%fdupes %{buildroot}%{src_install_dir}

%post -n libprotobuf-nanopb%{sover} -p /sbin/ldconfig
%postun -n libprotobuf-nanopb%{sover} -p /sbin/ldconfig

%files -n libprotobuf-nanopb%{sover}
%license LICENSE.txt
%doc CHANGELOG.txt README.md
%{_libdir}/libprotobuf-nanopb.so.%{sover}

%files devel
%{_bindir}/nanopb_generator.py
%{_bindir}/nanopb_generator
%{_bindir}/protoc-gen-nanopb
%{python3_sitelib}/proto
%{_includedir}/pb.h
%{_includedir}/pb_common.h
%{_includedir}/pb_decode.h
%{_includedir}/pb_encode.h
%{_libdir}/cmake/nanopb
%{_libdir}/libprotobuf-nanopb.so

%files source
%{src_install_dir}

%changelog
