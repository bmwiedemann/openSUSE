#
# spec file for package python-pythran
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
%{?sle15_python_module_pythons}

%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%define psuffix -%{flavor}
%bcond_without test
%if "%{flavor}" != "test-py310"
%define skip_python310 1
%endif
%if "%{flavor}" != "test-py311"
%define skip_python311 1
%endif
%if "%{flavor}" != "test-py312"
%define skip_python312 1
%endif
# Skip empty buildsets, last one is for sle15_python_module_pythons
%if "%{shrink:%{pythons}}" == "" || ("%pythons" == "python311" && 0%{?skip_python311})
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%else
ExclusiveArch:  x86_64
%endif
%endif

Name:           python-pythran%{psuffix}
Version:        0.16.1
Release:        0
Summary:        Ahead of Time compiler for numeric kernels
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/pythran
# Tests are only availble from the github archive
Source0:        https://github.com/serge-sans-paille/pythran/archive/refs/tags/%{version}.tar.gz#/pythran-%{version}-gh.tar.gz
Source99:       python-pythran-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beniget >= 0.4.0
Requires:       python-numpy
Requires:       python-ply >= 3.4
Requires:       python-setuptools
Requires:       (python-gast >= 0.5.0 with python-gast < 0.6.0)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION This is a package that compiles code, the runtime requires devel packages
Requires:       boost-devel
Requires:       gcc-c++
Requires:       python-devel
Requires:       python-numpy-devel
Requires:       xsimd-devel >= 13.0.0
# /SECTION
%if %{with test}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pythran = %{version}}
BuildRequires:  %{python_module wheel}
%if 0%{?suse_version} > 1500
BuildRequires:  openblas-devel
%else
BuildRequires:  cblas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  unzip
%endif
BuildArch:      noarch
%python_subpackages

%description
Ahead of Time compiler for numeric kernels

%prep
%autosetup -p1 -n pythran-%{version}

find -name '*.hpp' -exec chmod -x {} +
sed -i '1{/env python/d}' pythran/run.py

# remove embedded VIM swap files
find -type f -name "*.swp" -delete

# Remove bundled header libs and use the ones from system
rm -r pythran/boost pythran/xsimd

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pythran
%python_clone -a %{buildroot}%{_bindir}/pythran-config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export CFLAGS="%{optflags}"
%if 0%{?suse_version} > 1500
# Force to link against openblas during tests because the update-alternatives setup
# for lapack/cblas/openblas might be inconsistent inside obs builds
cat > config.pythranrc <<EOF
[compiler]
blas=openblas
libs=openblas
EOF
export PYTHRANRC=$PWD/config.pythranrc
%endif
# pytest_extra_args is for debug builds with local defines on command line
%pytest %{?jobs:-n %jobs} %{?pytest_extra_args}
%endif

%if !%{with test}
%post
%python_install_alternative pythran pythran-config

%postun
%python_uninstall_alternative pythran

%files %{python_files}
%doc AUTHORS Changelog README.rst
%license LICENSE
%python_alternative %{_bindir}/pythran
%python_alternative %{_bindir}/pythran-config
%{python_sitelib}/pythran
%{python_sitelib}/omp
%{python_sitelib}/pythran-%{version}.dist-info
%endif

%changelog
