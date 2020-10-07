#
# spec file for package python-distributed
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Test requires network connection
%bcond_with     test
Name:           python-distributed
Version:        2.29.0
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/d/distributed/distributed-%{version}.tar.gz
Source99:       python-distributed-rpmlintrc
BuildRequires:  %{python_module joblib >= 0.10.2}
BuildRequires:  %{python_module scikit-learn >= 0.17.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 6.6
Requires:       python-cloudpickle >= 1.3.0
Requires:       python-contextvars
Requires:       python-dask >= 2.7.0
Requires:       python-joblib >= 0.10.2
Requires:       python-msgpack
Requires:       python-psutil >= 5.0
Requires:       python-scikit-learn >= 0.17.1
Requires:       python-sortedcontainers
Requires:       python-tblib
Requires:       python-toolz >= 0.7.4
Requires:       python-tornado >= 5
Requires:       python-zict >= 0.1.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module click >= 6.6}
BuildRequires:  %{python_module cloudpickle >= 1.3.0}
BuildRequires:  %{python_module dask >= 0.18.0}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module tblib}
BuildRequires:  %{python_module toolz >= 0.7.4}
BuildRequires:  %{python_module tornado >= 4.5.1}
BuildRequires:  %{python_module zict >= 0.1.3}
%endif
%python_subpackages

%description
Dask.distributed is a library for distributed computing in Python. It
extends both the concurrent.futures and dask APIs to moderate sized
clusters.

%prep
%setup -q -n distributed-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/distributed/tests/
# Deduplicating files can generate a RPMLINT warning for pyc mtime
%fdupes %{buildroot}%{$python_sitelib}
}

%if %{with test}
%check
%pytest distributed/tests/
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/dask-ssh
%{_bindir}/dask-scheduler
%{_bindir}/dask-worker
%{python_sitelib}/distributed*

%changelog
