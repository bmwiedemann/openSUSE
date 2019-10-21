#
# spec file for package tbb
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


%define rel_ver 2019_U9
%define so_ver 2

%bcond_with python2
%bcond_without python3

Name:           tbb
Version:        2019_20190605
Release:        0
Summary:        Threading Building Blocks (TBB)
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://www.threadingbuildingblocks.org/
Source0:        https://github.com/01org/tbb/archive/%{rel_ver}.tar.gz
# PATCH-FIX-OPENSUSE optflags.patch -- Use rpm optflags
Patch1:         optflags.patch
# PATCH-FIX-OPENSUSE reproducible.patch -- Do not compile build hostname+kernel into binary
Patch2:         reproducible.patch
# PATCH-FIX-OPENSUSE disable-irml.patch -- Don't try to link to irml
Patch3:         disable-irml.patch
Patch4:         cmake-remove-include-path.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with python2}
BuildRequires:  python2-devel
%endif
%if %{with python3}
BuildRequires:  python3-devel
%endif
BuildRequires:  swig >= 3.0.6

%description
Threading Building Blocks (TBB) offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you take
advantage of multi-core processor performance without having to be a threading
expert. Threading Building Blocks is not just a threads-replacement library. It
represents a higher-level, task-based parallelism that abstracts platform
details and threading mechanism for performance and scalability.

%package -n libtbb%{so_ver}
Summary:        Threading Building Blocks (TBB)
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libtbb%{so_ver}
Threading Building Blocks (TBB) offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you take
advantage of multi-core processor performance without having to be a threading
expert. Threading Building Blocks is not just a threads-replacement library. It
represents a higher-level, task-based parallelism that abstracts platform
details and threading mechanism for performance and scalability.

%package -n libtbbmalloc%{so_ver}
Summary:        Threading Building Blocks (TBB)
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libtbbmalloc%{so_ver}
This subpackage contains the two TBB memory allocator templates that
are similar to the STL template class std::allocator. These two
templates, scalable_allocator<T> and cache_aligned_allocator<T>,
address critical issues in parallel programming: scalability and
false sharing.

%package -n python2-%{name}
Summary:        Python 2 support for Threading Building Blocks (TBB)
Group:          Development/Languages/Python

%description -n python2-%{name}
This package contains python 2 bindings for Threading Building Blocks
(TBB).

%package -n python3-%{name}
Summary:        Python 3 support for Threading Building Blocks (TBB)
Group:          Development/Languages/Python

%description -n python3-%{name}
This package contains python 2 bindings for Threading Building Blocks
(TBB).

%package devel
Summary:        Development Files for Threading Building Blocks (TBB)
Group:          Development/Libraries/C and C++
Requires:       c++_compiler
Requires:       libtbb%{so_ver} = %{version}
Requires:       libtbbmalloc%{so_ver} = %{version}

%description devel
Threading Building Blocks (TBB) offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you take
advantage of multi-core processor performance without having to be a threading
expert. Threading Building Blocks is not just a threads-replacement library. It
represents a higher-level, task-based parallelism that abstracts platform
details and threading mechanism for performance and scalability.

This package contains the header files needed for development with tbb.

%prep
%setup -q -n %{name}-%{rel_ver}
%autopatch -p1

%build
make OPTFLAGS="%{optflags}" %{?_smp_mflags} tbb_build_prefix=obj

mkdir lib; pushd lib
ln -s ../build/obj_release/*.so* .
popd

cp -r python python3

export TBBROOT=$PWD
. build/obj_release/tbbvars.sh
%if %{with python2}
pushd python
%python2_build
popd
%endif

%if %{with python3}
pushd python3
%python3_build
popd
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}

pushd include
    find tbb -type f -exec \
        install -Dpm 644 {} %{buildroot}%{_includedir}/{} \
    \;
popd

pushd build/obj_release
    for file in libtbb{,malloc{,_proxy}}; do
        install -Dpm 0755 ${file}.so.%{so_ver} %{buildroot}%{_libdir}
        ln -s $file.so.%{so_ver} %{buildroot}%{_libdir}/$file.so
    done
popd

mkdir -p %{buildroot}%{_libdir}/cmake/TBB
# Build cmake config files
cmake -DINSTALL_DIR=%{buildroot}%{_libdir}/cmake/TBB \
      -DSYSTEM_NAME=Linux \
      -DTBB_VERSION_FILE=%{buildroot}%{_includedir}/tbb/tbb_stddef.h \
      -DLIB_REL_PATH="../../" \
      -P cmake/tbb_config_installer.cmake

%if %{with python2}
pushd python
%python2_install
popd
%endif

%if %{with python3}
pushd python3
%python3_install
popd
%endif

%post -n libtbb%{so_ver} -p /sbin/ldconfig
%postun -n libtbb%{so_ver} -p /sbin/ldconfig
%post -n libtbbmalloc%{so_ver} -p /sbin/ldconfig
%postun -n libtbbmalloc%{so_ver} -p /sbin/ldconfig

%files -n libtbb%{so_ver}
%{_libdir}/libtbb.so.%{so_ver}*

%if %{with python2}
%files -n python2-%{name}
%{python_sitearch}/*
%endif

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/*
%endif

%files -n libtbbmalloc%{so_ver}
%{_libdir}/libtbbmalloc.so.%{so_ver}*
%{_libdir}/libtbbmalloc_proxy.so.%{so_ver}*

%files devel
%license LICENSE
%doc CHANGES doc/Release_Notes.txt
%{_includedir}/tbb/
%{_libdir}/cmake/TBB
%{_libdir}/libtbb.so
%{_libdir}/libtbbmalloc.so
%{_libdir}/libtbbmalloc_proxy.so

%changelog
