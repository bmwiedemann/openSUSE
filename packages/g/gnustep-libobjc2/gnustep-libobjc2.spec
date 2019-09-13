#
# spec file for package gnustep-libobjc2
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


%define _oname  libobjc2
%define libname libobjc4_6
Name:           gnustep-libobjc2
Version:        2.0
Release:        0
Summary:        GNUstep Objective-C Runtime
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/gnustep/libobjc2
Source:         https://github.com/gnustep/libobjc2/archive/%{version}.tar.gz#/%{_oname}-%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  fdupes
BuildRequires:  gnustep-make
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-clang

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for the
GCC runtime.  It supports both a legacy and a modern ABI, allowing code
compiled with old versions of GCC to be supported without requiring
recompilation.  The modern ABI adds the following features:

- Non-fragile instance variables.
- Protocol uniquing.
- Object planes support.
- Declared property introspection.

%package -n %{libname}
Summary:        GNUstep Objective-C Runtime
Group:          System/Libraries

%description -n %{libname}
The GNUstep Objective-C runtime is designed as a drop-in replacement for the
GCC runtime.  It supports both a legacy and a modern ABI, allowing code
compiled with old versions of GCC to be supported without requiring
recompilation.  The modern ABI adds the following features:

- Non-fragile instance variables.
- Protocol uniquing.
- Object planes support.
- Declared property introspection.

%package -n %{_oname}-devel
Summary:        Header files for the GNUstep Objective-C runtime
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{_oname}-devel
This package contains all necessary include files and libraries needed
to develop applications with the GNUstep Objective-C runtime.

%prep
%setup -q -n %{_oname}-%{version}

%build
# clang does not support lto yet
%if 0%{?suse_version} > 1500
%define _lto_cflags %{nil}
%endif
mkdir build
pushd build
cmake .. \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DGNUSTEP_INSTALL_TYPE=SYSTEM \
    -DTESTS=FALSE
make %{?_smp_mflags}
popd

%install
pushd build
make  DESTDIR=%{buildroot} install/strip
popd

%fdupes -s %{buildroot}%{_includedir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libobjc.so.*

%files -n %{_oname}-devel
%license COPYING
%doc ANNOUNCE.* API README.md
%{_includedir}/objc
%{_includedir}/Block.h
%{_includedir}/Block_private.h
%{_libdir}/libobjc.so

%changelog
