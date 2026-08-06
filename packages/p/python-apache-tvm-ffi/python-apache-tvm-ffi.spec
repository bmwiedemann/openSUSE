#
# spec file for package python-apache-tvm-ffi
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-apache-tvm-ffi
Version:        0.1.13.post2
Release:        0
Summary:        Minimal FFI runtime and ABI for machine learning systems
License:        Apache-2.0
URL:            https://github.com/apache/tvm-ffi
Source:         https://files.pythonhosted.org/packages/source/a/apache_tvm_ffi/apache_tvm_ffi-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module Cython >= 3.2.8}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build-core >= 0.10.0}
BuildRequires:  %{python_module setuptools-scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 4.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake >= 3.26
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja >= 1.11
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 4.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
apache-tvm-ffi (tvm_ffi) provides a minimal, dependency-free foreign
function interface runtime and ABI used to exchange functions, tensors
and errors between compiled machine learning kernels and Python. It
ships a compiled runtime shared library together with the C++ headers
and CMake package configuration so that native projects can link against
it via find_package(tvm_ffi).

%prep
%autosetup -p1 -n apache_tvm_ffi-%{version}

%build
export CMAKE_GENERATOR=Ninja
# The sdist ships PKG-INFO but no .git, so pin the version for setuptools-scm.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
# Drop the stray upstream .gitignore shipped inside the package tree.
%python_expand rm -f %{buildroot}%{$python_sitearch}/tvm_ffi/.gitignore
# Register the console entry points through the singlespec alternatives.
%python_clone -a %{buildroot}%{_bindir}/tvm-ffi-config
%python_clone -a %{buildroot}%{_bindir}/tvm-ffi-stubgen
%python_expand %fdupes %{buildroot}%{$python_sitearch}/tvm_ffi

%check
# The upstream pytest suite pulls the whole torch stack into the build root
# (its "test" dependency group includes torch, numpy and ml_dtypes) and
# JIT-compiles and loads native modules while the tests run, so it is not
# practical here. Fall back to an import smoke test that loads the compiled
# Cython core extension and the bundled runtime shared library.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -Bc "import tvm_ffi; print(tvm_ffi.__version__)"

%post
%python_install_alternative tvm-ffi-config
%python_install_alternative tvm-ffi-stubgen

%postun
%python_uninstall_alternative tvm-ffi-config
%python_uninstall_alternative tvm-ffi-stubgen

%files %{python_files}
%license LICENSE NOTICE
%doc README.md
%python_alternative %{_bindir}/tvm-ffi-config
%python_alternative %{_bindir}/tvm-ffi-stubgen
# The whole tvm_ffi tree is shipped intact: besides the Python package and the
# compiled core extension it carries lib/libtvm_ffi*.so, the C++ headers under
# include/, the JIT sources under src/ and the CMake package config under
# share/cmake/tvm_ffi/ that downstream consumers (e.g. xgrammar) discover via
# find_package(tvm_ffi CONFIG). Keeping the headers/CMake config in the Python
# package is intentional (no separate -devel subpackage) so that discovery
# works from the installed sitearch path.
%{python_sitearch}/tvm_ffi
%{python_sitearch}/apache_tvm_ffi-%{version}.dist-info

%changelog
