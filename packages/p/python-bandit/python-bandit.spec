#
# spec file for package python-bandit
#
# Copyright (c) 2025 SUSE LLC
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
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# CLI tool, no module
%define pythons python3
%bcond_without  builddocs
%{?sle15_python_module_pythons}
Name:           python-bandit
Version:        1.8.3
Release:        0
Summary:        Security oriented static analyser for Python code
License:        Apache-2.0
URL:            https://github.com/PyCQA/bandit
Source:         https://files.pythonhosted.org/packages/source/b/bandit/bandit-%{version}.tar.gz
Patch0:         remove-non-test-deps.patch
BuildRequires:  %{python_module pbr >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-GitPython
Requires:       python-GitPython >= 1.0.1
Requires:       python-PyYAML
Requires:       python-PyYAML >= 5.3.1
Requires:       python-jschema-to-python >= 1.2.3
Requires:       python-rich
Requires:       python-sarif-om
Requires:       python-stestr >= 1.0.0
Requires:       python-stevedore >= 1.20.0
Requires:       (python-tomli >= 1.2.3 if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{python_version_nodots} < 311
Requires:       python-tomli
%endif
%if %{with test}
BuildRequires:  %{python_module GitPython >= 1.0.1}
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module bandit == %{version}}
BuildRequires:  %{python_module beautifulsoup4 >= 4.8.0}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module jschema-to-python >= 1.2.3}
BuildRequires:  %{python_module python-subunit >= 0.0.18}
BuildRequires:  %{python_module sarif-om}
BuildRequires:  %{python_module stestr >= 2.5.0}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testscenarios >= 0.5.0}
BuildRequires:  %{python_module testtools >= 2.3.0}
%endif
# doc requirements
%if %{with builddocs}
BuildRequires:  %{python_module Sphinx >= 1.2.1}
BuildRequires:  %{python_module reno >= 1.8.0}
%endif
%python_subpackages

%description
Bandit is a tool designed to find common security issues in Python code. To do
this Bandit processes each file, builds an AST from it, and runs appropriate
plugins against the AST nodes. Once Bandit has finished scanning all the files
it generates a report.

%prep
%autosetup -p1 -n bandit-%{version}
sed -i '/^#!/d' bandit/__main__.py

%if !%{with test}
%build
%pyproject_wheel
%endif

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/bandit
%python_clone -a %{buildroot}%{_bindir}/bandit-config-generator
%python_clone -a %{buildroot}%{_bindir}/bandit-baseline
%endif

%if %{with test}
%check
%pyunittest discover -v
%endif

%if !%{with test}
%post
%{python_install_alternative bandit bandit-config-generator bandit-baseline }
%endif

%if !%{with test}
%postun
%python_uninstall_alternative bandit
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%python_alternative %{_bindir}/bandit
%python_alternative %{_bindir}/bandit-config-generator
%python_alternative %{_bindir}/bandit-baseline
%{python_sitelib}/bandit
%{python_sitelib}/bandit-%{version}*-info
%endif

%changelog
