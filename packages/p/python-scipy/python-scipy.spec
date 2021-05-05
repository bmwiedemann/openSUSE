#
# spec file for package python-scipy
#
# Copyright (c) 2021 SUSE LLC
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
%define _ver 1_6_0
%define shortname scipy
%define pname python-%{shortname}
%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if "%{flavor}" == "standard"
 %bcond_with hpc
 %ifarch armv6l s390 s390x m68k riscv64
  %bcond_with openblas
 %else
    %if 0%{?sle_version} == 120200
      %ifarch i586
        %bcond_with openblas
      %else
        %bcond_without openblas
      %endif
    %else
      %bcond_without openblas
    %endif
  %endif
%endif
%if "%{flavor}" == "gnu-hpc"
 %define compiler_family gnu
 %bcond_without hpc
 %undefine c_f_ver
%endif
%if "%{flavor}" == "gnu7-hpc"
 %define compiler_family gnu
 %define c_f_ver 7
 %bcond_without hpc
%endif
%define         skip_python2 1
# https://numpy.org/neps/nep-0029-deprecation_policy.html
%define         skip_python36 1
%{?with_hpc:%{hpc_requires}}
%bcond_with ringdisabled
%if %{without hpc}
%define package_name %{pname}
%define p_python_sitearch %{python_sitearch}
%define p_prefix %{_prefix}
%define p_bindir %{_bindir}
%else
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %{_ver}}
%define p_python_sitearch %{hpc_python_sitearch}
%define p_prefix %{hpc_prefix}
%define p_bindir %{hpc_bindir}
# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
 %ifarch armv6l s390 s390x m68k riscv64 i586
ExclusiveArch:  do_not_build
 %endif
%{hpc_modules_init openblas}
%endif
Name:           %{package_name}
Version:        1.6.3
Release:        0
Summary:        Scientific Tools for Python
License:        BSD-3-Clause AND LGPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://www.scipy.org
Source0:        https://files.pythonhosted.org/packages/source/s/scipy/scipy-%{version}.tar.gz
Source100:      python-scipy-rpmlintrc
BuildRequires:  %{python_module Cython >= 0.29.18}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pybind11 >= 2.4.3}
BuildRequires:  %{python_module pybind11-devel >= 2.4.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if %{without hpc}
BuildRequires:  %{python_module numpy-devel >= 1.16.5}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
Requires:       python-numpy >= 1.16.5
Requires:       python-pybind11 >= 2.4.3
 %if %{with openblas}
BuildRequires:  openblas-devel
 %else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
 %endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel >= 1.3
BuildRequires:  %{python_module numpy%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel}
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc >= 0.3
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
Requires:       python-numpy%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc >= 1.16.5
%endif
%python_subpackages

%description
Scipy is open-source software for mathematics, science, and
engineering. The core library is NumPy which provides convenient and
fast N-dimensional array manipulation. The SciPy library is built to
work with NumPy arrays, and provides many numerical routines such as
for numerical integration and optimization.

%{?with_hpc:%{hpc_python_master_package -L -a }}

%prep
%setup -q -n scipy-%{version}
find . -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python||" {} \;

%build
%{python_expand #
%if %{with hpc}
py_ver=%{$python_version}
%hpc_setup
module load $python-numpy
export CFLAGS="$(pkg-config --cflags openblas) %{optflags} -fno-strict-aliasing" LIBS="$(pkg-config --libs openblas)"
export OPENBLAS=$OPENBLAS_LIB
%else
export CFLAGS="%{optflags} -fno-strict-aliasing"
export BLAS=%{_libdir}
export LAPACK=%{_libdir}
 %if %{with openblas}
export OPENBLAS=%{_libdir}
 %endif
%endif
$python setup.py config_fc --fcompiler=gnu95 --noarch build
}

%install
%{python_expand #
%if %{with hpc}
%hpc_setup
module load $python-numpy
%endif
$python setup.py install --prefix=%{p_prefix} --root=%{buildroot}
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with hpc}
%define hpc_module_pname ${python_flavor}-%{shortname}
%{python_expand #
python_flavor=$(cat _current_flavor)
sitesearch_path=`$python -c "import sysconfig as s; print(s.get_paths(vars={'platbase':'%{hpc_prefix}','base':'%{hpc_prefix}'}).get('platlib'))"`
rm -rf %{buildroot}${sitesearch_path}/scipy/{,core,distutils,f2py,fft,lib,linalg,ma,matrixlib,oldnumeric,polynomial,random,testing}/tests
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler "
puts stderr "toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain."
module-whatis "Version: %{version}"
module-whatis "Category: python module"
module-whatis "Description: %{SUMMARY}"
module-whatis "URL %{url}"

set     version             %{version}

depends-on $python-numpy

prepend-path    PYTHONPATH          ${sitesearch_path}

setenv          %{hpc_upcase_trans_hyph %{pname}}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase_trans_hyph %{pname}}_BIN        %{hpc_bindir}

family %{shortname}
EOF
}
%endif

%if %{with hpc}
%post
%{hpc_module_delete_if_default}
%endif

%files %{python_files}
%license LICENSE.txt
%{p_python_sitearch}/scipy/
%{p_python_sitearch}/scipy-*-py*.egg-info

%if %{with hpc}
%define hpc_module_pname %{python_flavor}-scipy
%{hpc_modules_files}
%{hpc_dirs}
%dir %{hpc_libdir}/python%{hpc_python_version}
%dir %{p_python_sitearch}
%endif

%changelog
