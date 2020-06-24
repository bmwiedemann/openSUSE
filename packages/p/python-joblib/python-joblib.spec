#
# spec file for package python-joblib
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
Name:           python-joblib
Version:        0.15.1
Release:        0
Summary:        Module for using Python functions as pipeline jobs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/joblib/joblib
Source:         https://files.pythonhosted.org/packages/source/j/joblib/joblib-%{version}.tar.gz
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-threadpoolctl
Requires:       python-lz4
Recommends:     python-numpy
Recommends:     python-psutil
BuildArch:      noarch
%python_subpackages

%description
Joblib is a set of tools to provide lightweight pipelining in
Python. In particular, joblib offers:

  1. transparent disk-caching of the output values and lazy re-evaluation
     (memoize pattern)

  2. parallel computing

  3. logging and tracing of the execution

Joblib can handle large data and has specific optimizations for `numpy` arrays.

%prep
%setup -q -n joblib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/joblib-%{version}-py*.egg-info
%{python_sitelib}/joblib/

%changelog
