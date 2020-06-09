#
# spec file for package python-behave
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
Name:           python-behave
Version:        1.2.6
Release:        0
Summary:        Behaviour-driven development, Python style
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/behave/behave
Source:         https://files.pythonhosted.org/packages/source/b/behave/behave-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-parse >= 1.8.2
Requires:       python-parse_type >= 0.4.2
Requires:       python-six >= 1.11
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-argparse
Suggests:       python-coverage
Suggests:       python-enum34
Suggests:       python-importlib
Suggests:       python-invoke >= 0.21.0
Suggests:       python-modernize >= 0.5
Suggests:       python-ordereddict
Suggests:       python-path.py >= 8.1.2
Suggests:       python-pathlib
Suggests:       python-pycmd
Suggests:       python-pylint
Suggests:       python-pytest >= 3.0
Suggests:       python-pytest-cov
Suggests:       python-sphinx >= 1.6
Suggests:       python-sphinx_bootstrap_theme >= 0.6
Suggests:       python-tox
Suggests:       python-traceback2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyHamcrest >= 1.8}
BuildRequires:  %{python_module mock >= 1.1}
BuildRequires:  %{python_module nose >= 1.3}
BuildRequires:  %{python_module parse >= 1.8.2}
BuildRequires:  %{python_module parse_type >= 0.4.2}
BuildRequires:  %{python_module path.py >= 10.1}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module six >= 1.11}
# /SECTION
%python_subpackages

%description
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

*behave* uses tests written in a natural language style, backed up by Python
code.

%prep
%setup -q -n behave-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/behave
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

%post
%python_install_alternative behave

%postun
%python_uninstall_alternative behave

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/behave
%{python_sitelib}/*

%changelog
