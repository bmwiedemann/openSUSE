#
# spec file for package python-statsd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-statsd
Version:        3.3.0
Release:        0
Summary:        A simple statsd client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jsocol/pystatsd
Source:         https://files.pythonhosted.org/packages/source/s/statsd/statsd-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
statsd is a front-end to Graphite. This is a Python client
for the statsd daemon.

%prep
%setup -q -n statsd-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.rst docs/_build/html
%{python_sitelib}/*

%changelog
