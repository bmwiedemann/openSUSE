#
# spec file for package tbb
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


%define so_ver 2

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with python2
%bcond_without python3
%if ! %{with python2}
%define skip_python2 1
%endif
Name:           tbb
Version:        2020.3
Release:        0
Summary:        Threading Building Blocks (TBB)
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.threadingbuildingblocks.org/
Source0:        https://github.com/oneapi-src/oneTBB/archive/v%{version}.tar.gz#/tbb-%{version}.tar.gz
# PATCH-FIX-OPENSUSE optflags.patch -- Use rpm optflags
Patch1:         optflags.patch
# PATCH-FIX-OPENSUSE reproducible.patch -- Do not compile build hostname+kernel into binary
Patch2:         reproducible.patch
# PATCH-FIX-OPENSUSE disable-irml.patch -- Don't try to link to irml
Patch3:         disable-irml.patch
Patch4:         cmake-remove-include-path.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  swig >= 3.0.6
%if 0%{?python38_version_nodots}
# if python multiflavor is in place yet, use it to generate subpackages
%define python_subpackage_only 1
%python_subpackages
%else
# unified defaults for the package file list
%define pycache_only %{nil}
%define python_sitearch %{python3_sitearch}
%define python_files() -n python3-%{**}
%endif

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

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Summary:        Python %{python_version} support for Threading Building Blocks (TBB)
Group:          Development/Languages/Python

%description -n python-%{name}
This package contains python %{python_version} bindings for Threading Building Blocks
(TBB).

%else
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
This package contains python 3 bindings for Threading Building Blocks
(TBB).
%endif

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
%setup -q -n oneTBB-%{version}
%autopatch -p1

sed -i 's/version\s*="0.1"/version = "%{version}"/' python/setup.py
sed -i '1{/^#!.*env python/ d}' python/TBB.py python/tbb/*.py

%build
make OPTFLAGS="%{optflags}" %{?_smp_mflags} tbb_build_prefix=obj

mkdir lib; pushd lib
ln -s ../build/obj_release/*.so* .
popd

export TBBROOT=$PWD
. build/obj_release/tbbvars.sh
%if %{with python2} || %{with python3}
pushd python
%python_build
# only needed for testing? Linking is patched out, not installing.
pushd rml
make
popd
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

export TBBROOT=$PWD
. build/obj_release/tbbvars.sh
%if %{with python2} || %{with python3}
pushd python
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
popd
%endif

%if %{with python2} || %{with python3}
%check
# avoid shuffling the existing build dir
mkdir python-test
pushd python-test
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}:../python/rml"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m tbb test -v
popd
%endif

%post -n libtbb%{so_ver} -p /sbin/ldconfig
%postun -n libtbb%{so_ver} -p /sbin/ldconfig
%post -n libtbbmalloc%{so_ver} -p /sbin/ldconfig
%postun -n libtbbmalloc%{so_ver} -p /sbin/ldconfig

%files -n libtbb%{so_ver}
%{_libdir}/libtbb.so.%{so_ver}*

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-%{name}
%{python2_sitearch}/tbb
%{python2_sitearch}/TBB.py*
%{python2_sitearch}/TBB-%{version}*-info
%endif

%if %{with python3} || ( %{with python2} && 0%{?python_subpackage_only} )
%files %{python_files %{name}}
%{python_sitearch}/tbb
%{python_sitearch}/TBB.py*
%{python_sitearch}/TBB-%{version}*-info
%pycache_only %{python_sitearch}/__pycache__/TBB*
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
