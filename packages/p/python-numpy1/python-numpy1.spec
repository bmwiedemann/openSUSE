#
# spec file for package python-numpy1
#
# Copyright (c) 2024 SUSE LLC
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
%define ver 1.26.4
%define _ver 1_26_4
%define plainpython python
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

%if %{without hpc}
%define pname python-numpy1
%else
%define pname python-numpy
%endif

%if 0%{?sle_version} == 120300
%{?with_openblas:ExclusiveArch:  do_not_build}
%endif
%{?with_hpc:%{hpc_requires}}
#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%bcond_without cblas
%else
%bcond_with libalternatives
%bcond_with cblas
%endif
#
%bcond_with ringdisabled
#
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
%{?sle15_python_module_pythons}
Name:           %{package_name}
# set %%ver and %%_ver instead above
Version:        %{ver}
Release:        0
Summary:        NumPy array processing for numbers, strings, records and objects
License:        BSD-3-Clause
URL:            http://www.numpy.org/
Source:         https://files.pythonhosted.org/packages/source/n/numpy/numpy-%{version}.tar.gz
Source99:       python-numpy1-rpmlintrc
# PATCH-FIX-OPENSUSE numpy-buildfix.patch -- openSUSE-specific build fixes
Patch0:         numpy-buildfix.patch
# PATCH-FIX-OPENSUSE numpy-1.9.0-remove-__declspec.patch -- fix for spurious compiler warnings that cause build failure
Patch1:         numpy-1.9.0-remove-__declspec.patch
# PATCH-FIX-UPSTREAM https://github.com/numpy/numpy/pull/26151
Patch2:         0001-BUG-Fix-test_impossible_feature_enable-failing-witho.patch
# PATCH-FIX-UPSTREAM https://github.com/numpy/meson/pull/12
Patch3:         0001-feature-module-Fix-handling-of-multiple-conflicts-pe.patch
# PATCH-FIX-UPSTREAM Based on gh#numpy/numpy#25839
Patch4:         fix-meson-multiple-python-versions.patch
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module meson-python >= 0.15}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata >= 0.7.1}
BuildRequires:  cmake
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  ninja >= 1.8.2
BuildRequires:  patchelf
BuildRequires:  python-rpm-macros >= 20210929
BuildConflicts: gcc11 < 11.2
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.4.0}
BuildRequires:  %{python_module hypothesis >= 6.75.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module typing-extensions >= 4.2.0}
# /SECTION
%if %{without hpc}
# Last version which packaged %%{_bindir}/f2py without update-alternatives
Conflicts:      %{plainpython}-numpy <= 1.12.0
Conflicts:      python-numpy >= 2
Provides:       python-numpy = %{version}-%{release}
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
%if %{with openblas}
BuildRequires:  openblas-devel > 0.3.20
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%if %{with cblas}
# openblas has significantly better performance for some operations
BuildRequires:  cblas-devel
Recommends:     libopenblas_pthreads0
%endif
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
%ifnarch %ix86 %arm
BuildRequires:  lua-lmod
%endif
BuildRequires:  suse-hpc
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
%endif
%python_subpackages

# Note: the hpc master package is provided by numpy 2 only

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

%package devel
Summary:        Development files for numpy applications
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       %plainpython(abi) = %{python_version}
%if %{without hpc}
Conflicts:      python-numpy-devel >= 2
Provides:       python-numpy-devel = %{version}-%{release}
%if %{with openblas}
Requires:       openblas-devel
%else
Requires:       blas-devel
%if %{with cblas}
Requires:       cblas-devel
%endif
Requires:       lapack-devel
%endif
%else
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
%{hpc_requires_devel}
%endif

%description devel
This package contains files for developing applications using numpy.

%prep
%autosetup -p1 -n numpy-%{version}
# Fix non-executable scripts
sed -i '1{/^#!/d}'\
  numpy/{distutils,f2py,ma,matrixlib,testing}/setup.py \
  numpy/distutils/{conv_template,cpuinfo,from_template,system_info}.py \
  numpy/f2py/{__init__,cfuncs,diagnose,crackfortran,f2py2e,rules}.py \
  numpy/random/_examples/cython/extending{,_distributions}.pyx \
  numpy/testing/print_coercion_tables.py
chmod -x \
  numpy/f2py/{crackfortran,f2py2e,rules}.py \
  numpy/testing/{print_coercion_tables,setup}.py

# force cythonization
rm -f PKG-INFO

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
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif

%pyproject_wheel

%install
%{?with_hpc:%hpc_setup}
%{?with_hpc:module load openblas}

%pyproject_install --prefix %{p_prefix} --root %{buildroot}

%if !%{with hpc}
%python_clone -a %{buildroot}%{_bindir}/f2py
%endif

%if 0%{?suse_version}
%fdupes %{buildroot}%{p_prefix}
%endif

%if %{with hpc}

%define hpc_module_pname ${python_flavor}-numpy
%{python_expand # Don't package testsuite
python_flavor=`cat _current_flavor`
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
# https://numpy.org/doc/stable/dev/development_environment.html#running-tests
%if %{without hpc}
export PATH="%{buildroot}%{_bindir}:$PATH"

mkdir -p testing
cp pytest.ini testing/
pushd testing

# flaky tests
test_failok+=" or test_structured_object_indexing"
test_failok+=" or test_structured_object_item_setting"
# flaky due to memory consumption
test_failok+=" or test_big_arrays"
# gh#numpy/numpy#22825
test_failok+=" or TestPrintOptions"
# gh#numpy/numpy#22835
test_failok+=" or test_keepdims_out"
# boo#1148173 gh#numpy/numpy#14438
%ifarch ppc64 ppc64le
test_failok+=" or test_generalized_sq"
# situation with IBM and double numbers is ... complicated
# gh#numpy/numpy#21094
test_failok+=" or test_ppc64_ibm_double_double128"
%endif
# these tests fail on big endian gh#numpy/numpy#11831
%ifarch s390x ppc ppc64
test_failok+=" or TestFReturnCharacter"
%endif
# missing instruction set
%ifarch s390x
test_failok+=" or test_truncate_f32"
%endif
%ifarch %{ix86}
# (arm 32-bit seems okay here)
# gh#numpy/numpy#18387
test_failok+=" or test_pareto"
# gh#numpy/numpy#18388
test_failok+=" or test_float_remainder_overflow"
%endif
%ifarch %{ix86} %{arm32}
# too much memory for 32bit
test_failok+=" or test_identityless_reduction_huge_array"
test_failok+=" or test_huge_vectordot"
# invalid int type for 32bit
test_failok+=" or (test_kind and test_quad_precision)"
test_failok+=" or (test_kind and test_int)"
test_failok+=" or (test_kind and test_real)"
test_failok+=" or (test_multinomial_pvals_float32)"
%endif
%ifarch %{arm}
# https://github.com/numpy/numpy/issues/24001
test_failok+=" or (test_cpu_features and test_features)"
test_failok+=" or (test_umath and test_unary_spurious_fpexception)"
%endif
%ifarch riscv64
# These tests fail due to non-portable assumptions about the signbit of NaN
# gh#numpy/numpy#8213
test_failok+=" or (test_umath and test_fpclass)"
test_failok+=" or (test_numeric and TestBoolCmp and test_float)"
test_failok+=" or (test_umath and test_fp_noncontiguous)"
%endif
# fail on Python 3.13 https://github.com/numpy/numpy/issues/27842
test_failok+=" or (test_nditer and test_iter_refcount) or (test_utils and (test_deprecate_help_indentation or test_deprecate_preserve_whitespace))"

echo "
import sys
import numpy
r = numpy.test(label='full', verbose=2,
               extra_argv=['-v', '-n', 'auto', '-k'] + sys.argv[1:])
sys.exit(0 if r else 1)
" > runobstest.py

%{python_expand # for all python3 flavors
export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
[ -n "$test_failok" ] && $python runobstest.py "${test_failok:4}" ||:
# test_new_policy: duplicates test runs and output and does not follow our deselection
$python runobstest.py "not (test_new_policy ${test_failok} or slow)"
}

popd
%endif

%if %{without hpc}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative f2py

%post
%python_install_alternative f2py

%postun
%python_uninstall_alternative f2py
%endif

%files %{python_files}
%doc README.md THANKS.txt
%license LICENSE.txt
%if %{without hpc}
%python_alternative %{_bindir}/f2py
%{python_sitearch}/numpy/
%{python_sitearch}/numpy-%{version}.dist-info
%exclude %{python_sitearch}/numpy/core/include/
%exclude %{python_sitearch}/numpy/distutils/mingw/*.c
%exclude %{python_sitearch}/numpy/distutils/checks/*.c
%exclude %{python_sitearch}/numpy/f2py/src/
%exclude %{python_sitearch}/numpy/core/lib/libnpymath.a
%exclude %{python_sitearch}/numpy/random/lib/libnpyrandom.a
%else
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
%{p_bindir}/f2py
%else
%exclude %{p_bindir}/f2py
%endif
%{p_python_sitearch}/numpy/
%{p_python_sitearch}/numpy-%{version}.dist-info
%exclude %{p_python_sitearch}/numpy/core/include/
%exclude %{p_python_sitearch}/numpy/core/lib/libnpymath.a
%exclude %{p_python_sitearch}/numpy/random/lib/libnpyrandom.a
%exclude %{p_python_sitearch}/numpy/distutils/mingw/*.c
%exclude %{p_python_sitearch}/numpy/distutils/checks/*.c
%exclude %{p_python_sitearch}/numpy/f2py/src/
%endif

%if %{with hpc}
%define hpc_module_pname %{python_flavor}-numpy
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
%if 0%{python_version_nodots} < 312
%{python_sitearch}/numpy/distutils/mingw/*.c
%{python_sitearch}/numpy/distutils/checks/*.c
%endif
%{python_sitearch}/numpy/f2py/src/
%{python_sitearch}/numpy/core/lib/libnpymath.a
%{python_sitearch}/numpy/random/lib/libnpyrandom.a
%else
%{p_python_sitearch}/numpy/core/include/
%{p_python_sitearch}/numpy/core/lib/libnpymath.a
%{p_python_sitearch}/numpy/random/lib/libnpyrandom.a
%if 0%{python_version_nodots} < 312
%{p_python_sitearch}/numpy/distutils/mingw/*.c
%{p_python_sitearch}/numpy/distutils/checks/*.c
%endif
%{p_python_sitearch}/numpy/f2py/src/
%endif

%changelog
