#
# spec file for package python-libcst
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-libcst%{psuffix}
Version:        0.3.10
Release:        0
Summary:        Python 3.5+ concrete syntax tree with AST-like properties
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source:         https://files.pythonhosted.org/packages/source/l/libcst/libcst-%{version}.tar.gz
# isort needed for the code regeneration, code mod also on non test flavor
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.2
Requires:       python-typing-inspect >= 0.4.0
Requires:       python-typing_extensions >= 3.7.4.2
BuildArch:      noarch
%if %{python_version_nodots} < 37
Requires:       python-dataclasses
%endif
%if %{with test}
%if %{python_version_nodots} < 37
BuildRequires:  %{python_module dataclasses}
%endif
BuildRequires:  %{python_module PyYAML >= 5.2}
# black needed for tests and the code regeneration
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hypothesis >= 4.36.0}
BuildRequires:  %{python_module hypothesmith >= 0.0.4}
BuildRequires:  %{python_module typing-inspect >= 0.4.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.2}
%endif
%python_subpackages

%description
A concrete syntax tree with AST-like properties for Python 3.5+ programs.

%prep
%setup -q -n libcst-%{version}
# fix executable
sed -i 's/"python"/"python3"/' libcst/codemod/tests/test_codemod_cli.py
# https://github.com/Instagram/LibCST/issues/331
isort --version | grep "VERSION 4" || sed -i 's/"isort", "-y"/"isort"/' libcst/codegen/generate.py

# Depends on optional pyre
rm \
  libcst/metadata/tests/test_type_inference_provider.py \
  libcst/metadata/tests/test_full_repo_manager.py \
  libcst/tests/test_pyre_integration.py

# Test result depends on pyre
sed -i 's/"error: .* stack:",/"Transformed 1 files successfully.",/' libcst/codemod/tests/test_codemod_cli.py

%if !%{with test}
%build
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand # https://github.com/Instagram/LibCST/issues/331
$python -m libcst.codegen.generate visitors
$python -m libcst.codegen.generate return_types
$python -m libcst.codegen.generate matchers
}
%pyunittest -v
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/libcst
%{python_sitelib}/libcst-%{version}-py*.egg-info
%endif

%changelog
