#
# spec file for package python-pip-requirements-parser
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

%{?sle15_python_module_pythons}
Name:           python-pip-requirements-parser
Version:        32.0.1
Release:        0
Summary:        Pip requirements parsing library
License:        MIT
URL:            https://github.com/nexB/pip-requirements-parser
Source:         https://files.pythonhosted.org/packages/source/p/pip-requirements-parser/pip-requirements-parser-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm >= 4}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
Requires:       python-pyparsing
BuildArch:      noarch
%python_subpackages

%description
A mostly correct pip requirements parsing library because it uses pip's own code.

%package -n %{name}-doc
Summary:        Documentation files for %name
BuildRequires:  %{python_module Sphinx >= 5.0.2}
BuildRequires:  %{python_module sphinx_rtd_theme}

%description -n %{name}-doc
Documentation files for %name

%prep
%autosetup -p1 -n pip-requirements-parser-%{version}

%build
%pyproject_wheel
pushd docs
make text

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -m 644 -D docs/build/text/skeleton-usage.txt %{buildroot}%{_docdir}/%{name}-doc/skeleton-usage.txt

%check
# skip tests because of wrong error message (https://github.com/aboutcode-org/pip-requirements-parser/issues/22)
skip="test_RequirementsFile_to_dict or test_RequirementsFile_dumps_unparse"
%pytest -k "not ($skip)"

%files %{python_files}
%license mit.LICENSE apache-2.0.LICENSE src/packaging_legacy_version.py.LICENSE.APACHE src/packaging_legacy_version.py.LICENSE.BSD
%{python_sitelib}/pip_requirements_parser.py
%pycache_only %{python_sitelib}/__pycache__/
%{python_sitelib}/pip_requirements_parser-%{version}.dist-info
%{python_sitelib}/packaging_legacy_version.py

%files -n %{name}-doc
%doc AUTHORS.txt CHANGELOG.rst README.rst src/packaging_legacy_version.py.ABOUT 
%{_docdir}/%{name}-doc/skeleton-usage.txt

%changelog
