#
# spec file for package python-pytest-console-scripts
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pytest-console-scripts
Version:        1.4.1
Release:        0
Summary:        Pytest plugin for testing console scripts
License:        MIT
URL:            https://github.com/kvas-it/pytest-console-scripts
Source:         https://files.pythonhosted.org/packages/source/p/pytest-console-scripts/pytest-console-scripts-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module virtualenv >= 20}
# /SECTION
%python_subpackages

%description
Pytest-console-scripts is a `Pytest`_ plugin for testing python scripts
installed via ``console_scripts`` entry point of ``setup.py``. It can run the
scripts under test in a separate process or using the interpreter that's
running the test suite.  The former mode ensures that the script will run in an
environment that is identical to normal execution whereas the latter one allows
much quicker test runs during development while simulating the real runs as
much as possible.

%prep
%autosetup -n pytest-console-scripts-%{version} -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i 's:env python:env python3:' tests/test_run_scripts.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
