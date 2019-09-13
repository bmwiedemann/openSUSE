#
# spec file for package rttr
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


Name:           rttr
Version:        0.9.6
Release:        0
Summary:        Run Time Type Reflection for C++
License:        MIT
Group:          Development/Languages/C and C++
URL:            http://www.rttr.org/releases/rttr-%{version}-src.tar.gz
Source0:        %{name}-%{version}-src.tar.gz
#PATCH-FIX-OPENSUSE cxx11_compiler_flags.patch force c++11 mode on gcc4.8 (for Leap 42.3)
Patch0:         cxx11_compiler_flags.patch
#PATCH-FIX-OPENSUSE cmake_install_dir.patch fix cmake installation directories for SUSE standards
Patch1:         cmake_install_dir.patch
#PATCH-FIX-OPENSUSE doxygen_remove_date_time.patch remove date and time information from generated documentation
Patch2:         doxygen_remove_date_time.patch
#PATCH-FIX-OPENSUSE skip_json_example.patch fix compile error (https://github.com/rttrorg/rttr/issues/224)
Patch3:         skip_json_example.patch
# PATCH-FIX-OPENSUSE fix-include-permissions.patch fix wrong permissions of headers (https://github.com/rttrorg/rttr/issues/147)
Patch4:         fix-include-permissions.patch
# PATCH-FIX-UPSTREAM lp64.patch Support all LP64 architectures (https://github.com/rttrorg/rttr/pull/231)
Patch5:         lp64.patch
#PATCH-FIX-UPSTREAM remove_pessimizing_moves.patch remove pessimizing move calls (https://github.com/rttrorg/rttr/pull/243)
Patch6:         remove_pessimizing_moves.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%prep
%setup -q -n%{name}-%{version}
%if 0%{?suse_version} < 1500
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

#only apply move elision to gcc versions that support it
%if 0%{?suse_version} >= 1500
%patch6 -p1
%endif

%build
find . -type f -exec chmod a-x "{}" +
dos2unix README.md
%cmake -DBUILD_BENCHMARKS=OFF -DCMAKE_INSTALL_CMAKEDIR=cmake -DBUILD_UNIT_TESTS=OFF
#make unit tests pass
export LD_LIBRARY_PATH=%{_builddir}/rttr-%{version}/build/lib/
%make_jobs

%install
#make unit tests pass
export LD_LIBRARY_PATH=%{_builddir}/rttr-%{version}/build/lib/
%cmake_install rttr_core
rm -Rf %{buildroot}/%{_datadir}/rttr

%package -n lib%{name}_core0_9_6
Summary:        Run Time Type Reflection for C++
Group:          System/Libraries

%description -n lib%{name}_core0_9_6
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%post -n lib%{name}_core0_9_6 -p /sbin/ldconfig
%postun -n lib%{name}_core0_9_6 -p /sbin/ldconfig

%files -n lib%{name}_core0_9_6
%license LICENSE.txt
%{_libdir}/librttr_core.so.%{version}

%package  devel
Summary:        Header files for the C++ Run Time Type Reflection library
Group:          Development/Languages/C and C++
Requires:       librttr_core0_9_6 = %{version}

%description  devel
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%files devel
%{_includedir}/rttr/
%{_libdir}/librttr_core.so
%{_libdir}/cmake/rttr/

%package devel-doc
Summary:        Documentation for rttr
Group:          Documentation/Other

%description devel-doc
API Documentation for rttr

%files devel-doc
%doc README.md
%{_docdir}/rttr/

%changelog
