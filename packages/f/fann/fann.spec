#
# spec file for package fann
#
# Copyright (c) 2025 SUSE LLC
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


Name:           fann
Version:        2.2.0
Release:        0
Summary:        Artificial neural network library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://leenissen.dk/fann/wp/
Source:         http://downloads.sourceforge.net/project/fann/fann/%{version}/FANN-%{version}-Source.zip
Patch0:         fix-cmake-link-libraries.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  unzip

%description
FANN is a neural network library which implements multilayer
artificial neural networks in C with support for both fully connected
and sparsely connected networks. Execution in both fixed and floating
point are supported. It includes a framework for easy handling of
training data sets.

%package -n libfann2
Summary:        Artificial neural network library
Group:          System/Libraries

%description -n libfann2
FANN is a neural network library which implements multilayer
artificial neural networks in C with support for both fully connected
and sparsely connected networks. Execution in both fixed and floating
point are supported. It includes a framework for easy handling of
training data sets.

%package devel
Summary:        Development package for fann, an artificial neural network library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libfann2 = %{version}
Requires:       libstdc++-devel
Provides:       libfann-devel = %{version}-%{release}
Obsoletes:      libfann-devel < %{version}-%{release}

%description devel
FANN is a neural network library which implements multilayer
artificial neural networks in C with support for both fully connected
and sparsely connected networks.

This subpackage contains the headers for FANN.

%prep
%autosetup -p1 -n FANN-%{version}-Source

perl -pi -e "s| -L[^ ']*||g" *.pc.*
sed -i 's/\r//g' COPYING.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%ldconfig_scriptlets -n libfann2

%files -n libfann2
%{_libdir}/libfloatfann.so.2*
%{_libdir}/libdoublefann.so.2*
%{_libdir}/libfixedfann.so.2*
%{_libdir}/libfann.so.2*

%files devel
%license COPYING.txt
%doc README.txt
%{_libdir}/libfloatfann.so
%{_libdir}/libdoublefann.so
%{_libdir}/libfixedfann.so
%{_libdir}/libfann.so
%{_includedir}/compat_time.h
%{_includedir}/doublefann.h
%{_includedir}/fann*.h
%{_includedir}/fixedfann.h
%{_includedir}/floatfann.h
%{_libdir}/pkgconfig/fann.pc

%changelog
