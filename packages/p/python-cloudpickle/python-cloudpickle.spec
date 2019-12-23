#
# spec file for package python-cloudpickle
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-cloudpickle
Version:        1.2.2
Release:        0
Summary:        Extended pickling support for Python objects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cloudpipe/cloudpickle
Source:         https://files.pythonhosted.org/packages/source/c/cloudpickle/cloudpickle-%{version}.tar.gz
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy >= 1.8.2}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
Requires:       python-curses
Requires:       python-numpy >= 1.8.2
Requires:       python-scipy
Requires:       python-tornado
BuildArch:      noarch
%python_subpackages

%description
The cloudpickle package makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library.

cloudpickle is especially useful for cluster computing where Python
expressions are shipped over the network to execute on remote hosts,
possibly close to the data.

Among other things, cloudpickle supports pickling for lambda expressions,
functions and classes defined interactively in the __main__ module.

%prep
%setup -q -n cloudpickle-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH='.:tests'
# Because of gh#cloudpipe/cloudpickle#316
%pytest -s -k 'not (test_dynamic_module or test_load_dynamic_module_in_grandchild_process)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
