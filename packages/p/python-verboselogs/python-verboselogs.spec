#
# spec file for package python-verboselogs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-verboselogs
Version:        1.7
Release:        0
Summary:        Verbose logging level for Python's logging module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xolox/python-verboselogs
Source:         https://files.pythonhosted.org/packages/source/v/verboselogs/verboselogs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Patch0:         verboselogs-pylint2.patch
Recommends:     python-pylint
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock >= 1.0.1}
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
%setup -q -n verboselogs-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand py.test-%{$python_bin_suffix} verboselogs/tests.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/verboselogs
%{python_sitelib}/verboselogs-%{version}-py*.egg-info

%changelog
