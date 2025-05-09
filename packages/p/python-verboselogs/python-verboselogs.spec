#
# spec file for package python-verboselogs
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


%{?sle15_python_module_pythons}
Name:           python-verboselogs
Version:        1.7
Release:        0
Summary:        Verbose logging level for Python's logging module
License:        MIT
URL:            https://github.com/xolox/python-verboselogs
Source:         https://files.pythonhosted.org/packages/source/v/verboselogs/verboselogs-%{version}.tar.gz
Patch0:         verboselogs-pylint2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-pylint
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest >= 2.6.1}
BuildRequires:  %{python_module pytest-cov >= 2.2.1}
# /SECTION
%python_subpackages

%description
The verboselogs_ package extends Python's logging_ module to add the log levels
VERBOSE_, NOTICE_, and SPAM_:

- The VERBOSE level sits between the predefined INFO and DEBUG levels.
- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.

It is currently tested on Python 2.6, 2.7, 3.4, 3.5 and PyPy.

%prep
%autosetup -p1 -n verboselogs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/xolox/python-verboselogs/issues/12
sed -i 's:import mock:from unittest import mock:' verboselogs/tests.py
%pytest verboselogs/tests.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/verboselogs
%{python_sitelib}/verboselogs-%{version}.dist-info

%changelog
