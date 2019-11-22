#
# spec file for package caffe
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname caffe
%define ver 1.0
%define _ver 1_0

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
 %define package_name %pname
%endif

%if "%flavor" == "serial"
%define so_name 1_0_0
%{bcond_with hpc}
%endif

%if "%flavor" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if %{without hpc}
%define package_name  %{pname}
%define p_prefix %_prefix
%define p_includedir %_includedir/%pname
%define p_bindir %_bindir
%define p_datadir %_datadir
%define p_libdir %_libdir
%define p_cmakedir %{p_libdir}/cmake/%{pname}
%else
%define package_name %{hpc_package_name %_ver}
%define p_prefix %hpc_prefix
%define p_includedir %hpc_includedir
%define p_bindir %hpc_bindir
%define p_datadir %hpc_datadir
%define p_libdir %hpc_libdir
%define p_cmakedir %{hpc_libdir}/cmake

%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%{hpc_modules_init openblas hdf5 python3-numpy}
%endif

Name:           %package_name
Version:        %ver
Release:        0
Summary:        A framework for deep learning
License:        BSD-2-Clause
Group:          Development/Libraries/Other
Url:            http://caffe.berkeleyvision.org/
Source0:        https://github.com/BVLC/caffe/archive/1.0.tar.gz#/%{pname}-%{version}.tar.gz
%if 0%{?suse_version} < 1330
BuildRequires:  boost-devel >= 1.55
%else
BuildRequires:  libboost_filesystem-devel >= 1.55
BuildRequires:  libboost_system-devel >= 1.55
BuildRequires:  libboost_thread-devel >= 1.55
%endif
BuildRequires:  cmake >= 2.8.7
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glog-devel
BuildRequires:  leveldb-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  lmdb-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(protobuf)
%if %{without hpc}
BuildRequires:  hdf5-devel
BuildRequires:  openblas-devel
BuildRequires:  python3-numpy-devel
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  hdf5-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  libopenblas-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  python3-numpy-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  suse-hpc >= 0.4
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deep learning framework made with expression, speed, and modularity
in mind.

%{?with_hpc:%{hpc_master_package}}

%package -n lib%{name}%{?so_name}
Summary:        Shared libraries for Caffe
Group:          System/Libraries
%if %{with hpc}
Requires:       libhdf5%{hpc_package_name_tail}
Requires:       libopenblas%{hpc_package_name_tail}
Requires:       lua-lmod
%endif

%description -n lib%{name}%{?so_name}
Deep learning framework made with expression, speed, and modularity
in mind.

%{?with_hpc:%{hpc_master_package -l -L}}

%package devel
Summary:        Development headers and libraries for Caffe
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the development libraries and headers for Caffe.

%{?with_hpc:%{hpc_master_package devel}}

%package -n python3-%name
Summary:        Python bindings to Caffe
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python3-protobuf
Requires:       python3-scikit-image

%description -n python3-%name
This package contains Python binding for Caffe.

%{?with_hpc:%{hpc_master_package -N python3-%pname}}

%package examples
Summary:        Examples for learning and testing with Caffe
Group:          Documentation/Howto
Requires:       %{name} = %{version}
Requires:       python3-caffe

%description examples
Examples which were bundeled with the sources, containing, for example,
sample programs to run in minst data.

%{?with_hpc:%{hpc_master_package examples}}

%prep
%setup -q -n %{pname}-%{version}

%build
%{?with_hpc:%hpc_setup}
export CMAKE_LIBRARY_PATH=$OPENBLAS_LIB

%define __builder ninja
# Use python3, not 2
sed -i 's/set(python_version "2"/set(python_version "3"/' CMakeLists.txt
export CFLAGS="%{optflags} -fPIE"
%if %{with hpc}
%hpc_cmake \
%else
%cmake \
%endif
       -DCPU_ONLY=ON \
       -DCMAKE_BUILD_TYPE=Release \
       -DBLAS=Open \
       -DBUILD_python=ON \
       -DBUILD_python_layer=ON \
       -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=true \
       -DCMAKE_EXE_LINKER_FLAGS="-pie"
%cmake_build

%install
%{?with_hpc:%hpc_setup}
%cmake_install

# Add caffe.pb.cc as required by some packages (e.g. armnn)
cp build/include/caffe/proto/caffe.pb.cc \
%if %{without hpc}
%{buildroot}%{p_includedir}/proto/caffe.pb.cc
%else
%{buildroot}%{p_includedir}/caffe/proto/caffe.pb.cc
%endif

# copy the examples
mkdir -p %{buildroot}%{_docdir}/%{name} 
# Contains URLs to possibly copyrighted material
rm -rf examples/finetune_flickr_style
cp -r examples %{buildroot}%{_docdir}/%{name}
cp -r data %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/examples/CMakeLists.txt
# Move python to the right folders
mkdir -p %{buildroot}%{python3_sitelib}/
mv %{buildroot}%{p_prefix}/python/caffe/ %{buildroot}%{python3_sitelib}/caffe/
mv %{buildroot}%{p_prefix}/python/*.py %{buildroot}%{p_bindir}
rm  %{buildroot}%{p_prefix}/python/requirements.txt
rmdir %{buildroot}%{p_prefix}/python/
# Remove static lib
rm -rf %{buildroot}%{p_libdir}/libproto.a
# Ugly fix to add right shebang line
for file in $(find %{buildroot}%{_docdir}/%{name}/ -name \*.sh); do grep '#!/usr/bin/sh' $file || sed -i '1s,#!/usr/bin/env sh,#!/usr/bin/sh,' $file ;done
# Add executeable bits to python bins
find %{buildroot}%{p_bindir} -name \*py -exec chmod 755 {} +
%if %{without hpc}
for file in $(find %{buildroot} -name \*.py); do grep '#!/usr/bin/python' $file || sed -i '1s,#!/usr/bin/env python,#!/usr/bin/python3,' $file ;done
for file in $(find %{buildroot}%{python3_sitelib}/caffe/ -name *py); do grep '#!/usr/bin/python' $file && chmod 755 $file; done
%else
%hpc_shebang_sanitize_scripts %{buildroot}/%{hpc_bindir}
for subdir in "" proto imagenet; do
  for file in %{buildroot}/%python3_sitelib/%{pname}/${subdir}/*.*; do
    %{hpc_python_mv_to_sitearch ${file##%{buildroot}} $subdir};
  done
done
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set     version                     %{version}

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
    if {  ![is-loaded openblas]  } {
        module load openblas
    }
    if { ![is-loaded hdf5]  } {
        module load hdf5
    }
    if { ![is-loaded python3-numpy]  } {
        module load python3-numpy
    }
}
prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
if {[file isdirectory  %{hpc_python_sitearch_no_singlespec}]} {
prepend-path    PYTHONPATH          %{hpc_python_sitearch_no_singlespec}
}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}/%{pname}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
}

family "%pname"
EOF
%endif
%fdupes %{buildroot}/%{_docdir}

%check
cd build
export LD_LIBRARY_PATH="%{buildroot}%{p_libdir}"
%{?with_hpc:%hpc_setup}
%cmake_build runtest

%if %{without hpc}
%post -n lib%{name}%{?so_name} -p /sbin/ldconfig

%postun -n lib%{name}%{?so_name} -p /sbin/ldconfig
%else
%postun -n lib%{name}
%{hpc_module_delete_if_default}
%endif

%files
%doc README.md
%license LICENSE
%{?with_hpc:%dir %{p_bindir}}
%{p_bindir}/caffe
%{p_bindir}/classification
%{p_bindir}/compute_image_mean
%{p_bindir}/convert_cifar_data
%{p_bindir}/convert_imageset
%{p_bindir}/convert_mnist_data
%{p_bindir}/convert_mnist_siamese_data
%{p_bindir}/device_query
%{p_bindir}/extract_features
%{p_bindir}/finetune_net
%{p_bindir}/net_speed_benchmark
%{p_bindir}/test_net
%{p_bindir}/train_net
%{p_bindir}/upgrade_net_proto_binary
%{p_bindir}/upgrade_net_proto_text
%{p_bindir}/upgrade_solver_proto_text

%files -n lib%{name}%{?so_name}
%{?hpc_modules_files}
%{?hpc_dirs}
%{p_libdir}/lib%{pname}.so.*

%files devel
%defattr(-,root,root)
%{p_includedir}
%{?with_hpc:%dir %p_datadir}
%{p_datadir}/Caffe
%{p_libdir}/lib%{pname}.so

%files -n python3-%{name}
%{p_bindir}/*.py
%if %{without hpc}
%dir %{python3_sitelib}/caffe
%{python3_sitelib}/caffe/*
%else
%{dirname:%{hpc_python_sitearch_no_singlespec}}
%endif

%files examples
%doc %{_docdir}/%{name}/examples
%doc %{_docdir}/%{name}/data

%changelog
