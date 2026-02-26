#
# spec file for package python-numpy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define plainpython python

#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%bcond_without cblas
%else
%bcond_with libalternatives
%bcond_with cblas
%endif
#
%{?sle15_python_module_pythons}

Name:           python-numpy
Version:        2.4.2
Release:        0
Summary:        NumPy array processing for numbers, strings, records and objects
License:        BSD-3-Clause
URL:            http://www.numpy.org/
Source:         https://files.pythonhosted.org/packages/source/n/numpy/numpy-%{version}.tar.gz
Source99:       python-numpy-rpmlintrc
# PATCH-FIX-OPENSUSE numpy-buildfix.patch -- openSUSE-specific build fixes
Patch0:         numpy-buildfix.patch
BuildRequires:  %{python_module Cython >= 3.0.6}
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module meson-python >= 0.18.0}
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
# Last version which packaged %%{_bindir}/f2py without update-alternatives
Conflicts:      %{plainpython}-numpy <= 1.12.0
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%if %{with cblas}
# openblas has significantly better performance for some operations
BuildRequires:  cblas-devel
Recommends:     libopenblas_pthreads0
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
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

%package devel
Summary:        Development files for numpy applications
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       python-devel
Requires:       %plainpython(abi) = %{python_version}
%if %{with cblas}
Requires:       cblas-devel
%endif
Requires:       lapack-devel

%description devel
This package contains files for developing applications using numpy.

%prep
%autosetup -p1 -n numpy-%{version}
# Fix non-executable scripts
sed -i '1{/^#!/d}'\
  numpy/distutils/{conv_template,cpuinfo,from_template,system_info}.py \
  numpy/f2py/{__init__,cfuncs,diagnose,crackfortran,f2py2e,rules}.py \
  numpy/random/_examples/cython/extending{,_distributions}.pyx \
  numpy/testing/print_coercion_tables.py
chmod -x \
  numpy/f2py/{crackfortran,f2py2e,rules}.py \
  numpy/testing/print_coercion_tables.py

# force cythonization
rm -f PKG-INFO

%build
export PYTHONDONTWRITEBYTECODE=1
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif

%pyproject_wheel

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/f2py
%python_clone -a %{buildroot}%{_bindir}/numpy-config

%if 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

%check
# https://numpy.org/doc/stable/dev/development_environment.html#running-tests

mkdir -p testing
cp pytest.ini testing/
pushd testing
%python_flavored_alternatives
%if %{with libalternatives}
%{python_expand #
for b in f2py numpy-config; do
  ln -s %{buildroot}%{_bindir}/$b-%{$python_bin_suffix} build/flavorbin/$b
done
}

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
# The meson command is always on the primary python and wants to import numpy from there
test_failok+=" or test_limited_api"
# gh#numpy/numpy#27531
test_failok+=" or test_api_importable"

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

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative f2py

%post
%python_install_alternative f2py numpy-config

%postun
%python_uninstall_alternative f2py

%files %{python_files}
%doc README.md THANKS.txt
%license LICENSE.txt
%python_alternative %{_bindir}/f2py
%python_alternative %{_bindir}/numpy-config
%{python_sitearch}/numpy/
%{python_sitearch}/numpy-%{version}.dist-info
%exclude %{python_sitearch}/numpy/_core/include
%exclude %{python_sitearch}/numpy/_core/lib/libnpymath.a
%exclude %{python_sitearch}/numpy/_core/lib/pkgconfig/numpy.pc
%exclude %{python_sitearch}/numpy/distutils/mingw/*.c
%exclude %{python_sitearch}/numpy/distutils/checks/*.c
%exclude %{python_sitearch}/numpy/f2py/src/
%exclude %{python_sitearch}/numpy/random/lib/libnpyrandom.a

%files %{python_files devel}
%license LICENSE.txt
%{python_sitearch}/numpy/_core/include/
%if 0%{python_version_nodots} < 312
%{python_sitearch}/numpy/distutils/mingw/*.c
%{python_sitearch}/numpy/distutils/checks/*.c
%endif
%{python_sitearch}/numpy/f2py/src/
%{python_sitearch}/numpy/_core/lib/libnpymath.a
%{python_sitearch}/numpy/_core/lib/pkgconfig/numpy.pc
%{python_sitearch}/numpy/random/lib/libnpyrandom.a

%changelog
