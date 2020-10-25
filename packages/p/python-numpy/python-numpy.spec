#
# spec file for package python-numpy
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


%global flavor @BUILD_FLAVOR@%{nil}
%define ver 1.19.2
%define _ver 1_19_2
%define pname python-numpy
%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')
%if "%{flavor}" == ""
 %bcond_with hpc
 %bcond_with openblas
%endif
%if "%{flavor}" == "gnu-hpc"
 %bcond_without hpc
%endif
%if "%{flavor}" == "gnu7-hpc"
 %define c_f_ver 7
 %bcond_without hpc
%endif
%if %{with hpc}
 %bcond_without openblas
%endif
%if 0%{?sle_version} == 120300
%{?with_openblas:ExclusiveArch:  do_not_build}
%endif
%ifarch s390 s390x
%{?with_openblas:ExclusiveArch:  do_not_build}
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%{?with_hpc:%{hpc_requires}}
%bcond_with ringdisabled
%if %{without hpc}
%define package_name %{pname}
%define p_python_sitearch %{python_sitearch}
%define p_prefix %{_prefix}
%define p_bindir %{_bindir}
%else
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?mpi_ver:-V %{mpi_ver}}}
%define package_name %{hpc_package_name %{_ver}}
%define p_python_sitearch %{hpc_python_sitearch}
%define p_prefix %{hpc_prefix}
%define p_bindir %{hpc_bindir}
# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%endif
Name:           %{package_name}
# set %%ver and %%_ver instead above
Version:        %ver
Release:        0
Summary:        NumPy array processing for numbers, strings, records and objects
License:        BSD-3-Clause
URL:            http://www.numpy.org/
Source:         https://files.pythonhosted.org/packages/source/n/numpy/numpy-%{version}.zip
Source99:       python-numpy-rpmlintrc
# PATCH-FIX-OPENSUSE numpy-buildfix.patch -- openSUSE-specific build fixes
Patch0:         numpy-buildfix.patch
# PATCH-FIX-OPENSUSE numpy-1.9.0-remove-__declspec.patch -- fix for spurious compiler warnings that cause build failure
Patch1:         numpy-1.9.0-remove-__declspec.patch
# # PATCH-FIX-SLE fix-py34-tests.patch -- python 3.4 support
Patch3:         fix-py34-tests.patch
Patch4:         s390x.patch
BuildRequires:  %{python_module Cython >= 0.29.21}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis >= 5.12.0}
BuildRequires:  %{python_module pytest >= 5.4.2}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if %{without hpc}
 %if 0%{?suse_version}
BuildRequires:  gcc-fortran
 %else
BuildRequires:  gcc-gfortran
 %endif
 %if %{with openblas}
BuildRequires:  openblas-devel > 0.3.4
 %else
BuildRequires:  blas-devel
BuildRequires:  cblas-devel
BuildRequires:  lapack-devel
# openblas has significantly better performance for some operations
Recommends:     libopenblas_pthreads0
 %endif
# Last version which packaged %%{_bindir}/f2py without update-alternatives
# Protect it from substitution
%define oldpy_numpy python-numpy
Conflicts:      %{oldpy_numpy} <= 1.12.0
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type which also makes NumPy suitable for
interfacing with general-purpose data-base applications.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation.

%{?with_hpc:%{hpc_python_master_package -L -a }}

%package devel
Summary:        Development files for numpy applications
Requires:       %{name} = %{version}
Requires:       python-devel
%if %{without hpc}
%if %{with openblas}
Requires:       openblas-devel
%else
Requires:       blas-devel
Requires:       cblas-devel
Requires:       lapack-devel
%endif
%else
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
%{hpc_requires_devel}
%endif

%description devel
This package contains files for developing applications using numpy.

%{?with_hpc:%{hpc_python_master_package devel -a }}

%prep
%setup -q -n numpy-%{version}
%patch0 -p1
%patch1 -p1
%patch3 -p1
%ifarch s390x ppc ppc64
# TestF{77,90}ReturnCharacter are broken on all big-endian architectures (#11831)
%patch4 -p1
%endif
# Fix non-executable scripts
sed -i '1s/^#!.*$//' numpy/{compat/setup,random/_examples/cython/setup,distutils/{conv_template,cpuinfo,exec_command,from_template,setup,system_info},f2py/{__init__,auxfuncs,capi_maps,cb_rules,cfuncs,common_rules,crackfortran,diagnose,f2py2e,f90mod_rules,func2subr,rules,setup,use_rules},ma/{setup,bench},matrixlib/setup,setup,testing/{print_coercion_tables,setup}}.py
sed -i '1s/^#!.*$//' numpy/random/_examples/cython/*.pyx

# force cythonization
rm PKG-INFO

%build
%define _lto_cflags %{nil}
%if %{with hpc}
%hpc_setup
module load openblas
export CFLAGS="$(pkg-config --cflags openblas) %{optflags} -fno-strict-aliasing" LIBS="$(pkg-config --libs openblas)"
cat > site.cfg <<EOF
[openblas]
libraries = openblas
library_dirs = $OPENBLAS_LIB
include_dirs = $OPENBLAS_INC
EOF
%else
export CFLAGS="%{optflags} -fno-strict-aliasing"
%endif

%python_build

%install
%{?with_hpc:%hpc_setup}
%{?with_hpc:module load openblas}

%python_exec setup.py install --prefix=%{p_prefix} --root=%{buildroot}

%if !%{with hpc}
%python_clone -a %{buildroot}%{_bindir}/f2py
%endif

%if 0%{?suse_version}
%fdupes %{buildroot}%{p_prefix}
%endif

%if %{with hpc}

%define hpc_module_pname python${py_ver/.*/}-numpy
%{python_expand # Don't package testsuite
py_ver=%{$python_version}
sitesearch_path=`$python -c "import sysconfig as s; print(s.get_paths(vars={'platbase':'%{hpc_prefix}','base':'%{hpc_prefix}'}).get('platlib'))"`
rm -rf %{buildroot}${sitesearch_path}/numpy/{,core,distutils,f2py,fft,lib,linalg,ma,matrixlib,oldnumeric,polynomial,random,testing}/tests
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler"
puts stderr "toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler"
module-whatis "Version: %{version}"
module-whatis "Category: python module"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL %{url}"

set     version             %{version}

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
  if { ![is-loaded intel] && ![is-loaded openblas] } {
      module load openblas
    }
}

prepend-path    PATH                %{hpc_bindir}
prepend-path    PYTHONPATH          ${sitesearch_path}

setenv          %{hpc_upcase_trans_hyph %{pname}}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase_trans_hyph %{pname}}_BIN        %{hpc_bindir}

family "NumPy"
EOF
}

%endif

%check
%if %{without hpc}
export PATH="%{buildroot}%{_bindir}:$PATH"
mkdir testing
pushd testing
# boo#1148173 gh#numpy/numpy#14438
%ifarch ppc64 ppc64le
%define skiptest -k "not test_generalized_sq"
%pytest_arch -n auto --pyargs numpy %{buildroot}%{python_sitearch}/numpy -k "test_generalized_sq" || true
%endif
%pytest_arch -n auto --pyargs numpy %{buildroot}%{python_sitearch}/numpy %{?skiptest}
popd
rm -Rf %{buildroot}%{python_sitearch}/numpy/.pytest_cache
%endif

%if %{without hpc}
%post
%python_install_alternative f2py

%postun
%python_uninstall_alternative f2py
%endif

%files %{python_files}
%doc README.md THANKS.txt
%if %{without hpc}
%python_alternative %{_bindir}/f2py
%python3_only %{_bindir}/f2py3*
%{python_sitearch}/numpy/
%{python_sitearch}/numpy-%{version}-py*.egg-info
%license %{python_sitearch}/numpy/LICENSE.txt
%exclude %{python_sitearch}/numpy/core/include/
%exclude %{python_sitearch}/numpy/distutils/mingw/gfortran_vs2003_hack.c
%exclude %{python_sitearch}/numpy/f2py/src/
%exclude %{python_sitearch}/numpy/core/lib/libnpymath.a
%else
%python3_only %{p_bindir}/f2py*
%{p_python_sitearch}/numpy/
%{p_python_sitearch}/numpy-%{version}-py*.egg-info
%license %{p_python_sitearch}/numpy/LICENSE.txt
%exclude %{p_python_sitearch}/numpy/core/include/
%exclude %{p_python_sitearch}/numpy/core/lib/libnpymath.a
%exclude %{p_python_sitearch}/numpy/distutils/mingw/gfortran_vs2003_hack.c
%exclude %{p_python_sitearch}/numpy/f2py/src/
%endif

%if %{with hpc}
%define hpc_module_pname python%(a=%{hpc_python_version}; echo -n ${a/.*/})-numpy
%{hpc_modules_files}
%{hpc_dirs}
%dir %{hpc_bindir}
%dir %{hpc_libdir}/python%{hpc_python_version}
%dir %{p_python_sitearch}
%endif

%files %{python_files devel}
%license LICENSE.txt
%if %{without hpc}
%{python_sitearch}/numpy/core/include/
%{python_sitearch}/numpy/distutils/mingw/gfortran_vs2003_hack.c
%{python_sitearch}/numpy/f2py/src/
%{python_sitearch}/numpy/core/lib/libnpymath.a
%else
%{p_python_sitearch}/numpy/core/include/
%{p_python_sitearch}/numpy/core/lib/libnpymath.a
%{p_python_sitearch}/numpy/distutils/mingw/gfortran_vs2003_hack.c
%{p_python_sitearch}/numpy/f2py/src/
%endif

%changelog
