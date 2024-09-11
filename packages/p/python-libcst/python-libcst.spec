#
# spec file for package python-libcst
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
# %%if "%%{flavor}" == "test"
# %%define psuffix -test
# %%bcond_without test
# %%else
%define psuffix %{nil}
%bcond_with test
# %%endif
%define modname libcst
%{?sle15_python_module_pythons}
Name:           python-libcst%{psuffix}
Version:        1.4.0
Release:        0
Summary:        Python 3.5+ concrete syntax tree with AST-like properties
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source0:        https://files.pythonhosted.org/packages/source/l/libcst/%{modname}-%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM pyo3-022.patch gh#Instagram/LibCST!1180 mcepl@suse.com
# updgrade pyo3 to 0.22 version
Patch0:         pyo3-022.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
Requires:       python-PyYAML >= 5.2
Requires:       python-typing-inspect >= 0.4.0
Requires:       python-typing_extensions >= 3.7.4.2
Requires:       (python-dataclasses if python-base < 3.7)
%if %{with test}
# black and isort needed for tests and the code regeneration
BuildRequires:  %{python_module PyYAML >= 5.2}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module hypothesis >= 4.36.0}
BuildRequires:  %{python_module hypothesmith >= 0.0.4}
BuildRequires:  %{python_module typing-inspect >= 0.4.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.2}
%endif
%python_subpackages

%description
A concrete syntax tree with AST-like properties for Python 3.5+ programs.

%prep
%autosetup -a1 -n libcst-%{version} -p1

# # Depends on optional pyre
# rm \
#   libcst/metadata/tests/test_type_inference_provider.py \
#   libcst/metadata/tests/test_full_repo_manager.py \
#   libcst/tests/test_pyre_integration.py

%build
export CARGO_NET_OFFLINE=true PROFILE=release
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true PROFILE=release
%pyproject_install
# gh#Instagram/LibCST#818
%{python_expand rm -rf %{buildroot}%{$python_sitearch}/libcst/tests
%fdupes %{buildroot}%{$python_sitearch}
}

%clean

%if %{with test}
%check
%python_expand find %{buildroot}%{$python_sitearch} -name \*.so\*
%pyunittest_arch discover -v libcst/tests
%endif

%if %{without test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/libcst
%{python_sitearch}/libcst-%{version}*-info
%endif

%changelog
