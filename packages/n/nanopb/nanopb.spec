#
# spec file for package nanopb
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


%define sover 0
%define src_install_dir /usr/src/%{name}

Name:           nanopb
Version:        0.3.9.2
Release:        0
Summary:        Protocol Buffers with small code size
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            https://jpa.kapsi.fi/nanopb/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  protobuf-devel
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros

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
Group:          Development/Sources
BuildArch:      noarch

%description source
Source code of nanopb - a C implementation of Google's Protocol Buffers data
format.

%prep
%setup -q
# Add support for tag numbers > 255 and fields larger than 255 bytes.
sed -i 's|/\* #define PB_FIELD_16BIT 1 \*/|#define PB_FIELD_16BIT 1|' ./pb.h

%build
%cmake -DBUILD_SHARED_LIBS=ON -DBUILD_STATIC_LIBS=OFF
%make_jobs

%install
%cmake_install
rm %{buildroot}%{python_sitelib}/nanopb_pb2.py
rm %{buildroot}%{python_sitelib}/plugin_pb2.py

mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix env-script-interpreter rpmlint error
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|' "{}" +
# Add support for tag numbers > 255 and fields larger than 255 bytes.
sed -i 's|/\* #define PB_FIELD_16BIT 1 \*/|#define PB_FIELD_16BIT 1|' %{buildroot}%{src_install_dir}/pb.h

%fdupes %{buildroot}%{src_install_dir}

%post -n libprotobuf-nanopb%{sover} -p /sbin/ldconfig
%postun -n libprotobuf-nanopb%{sover} -p /sbin/ldconfig

%files -n libprotobuf-nanopb%{sover}
%license LICENSE.txt
%doc CHANGELOG.txt README.md
%{_libdir}/libprotobuf-nanopb.so.%{sover}

%files devel
%{_includedir}/pb.h
%{_includedir}/pb_common.h
%{_includedir}/pb_decode.h
%{_includedir}/pb_encode.h
%{_libdir}/cmake/nanopb
%{_libdir}/cmake/nanopb/nanopb-config-version.cmake
%{_libdir}/cmake/nanopb/nanopb-config.cmake
%{_libdir}/cmake/nanopb/nanopb-targets-relwithdebinfo.cmake
%{_libdir}/cmake/nanopb/nanopb-targets.cmake
%{_libdir}/libprotobuf-nanopb.so

%files source
%{src_install_dir}

%changelog
