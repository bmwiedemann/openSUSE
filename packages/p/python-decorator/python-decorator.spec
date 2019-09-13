#
# spec file for package python-decorator
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-decorator
Version:        4.4.0
Release:        0
Summary:        Non-nested signature-retaining Python decorators
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/micheles/decorator
Source:         https://files.pythonhosted.org/packages/source/d/decorator/decorator-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Typical implementations of Python decorators involve nested
functions, and do not preserve the signature of decorated functions,
thus can be confusing to both developers and documentation tools.

This module changes the usage of decorators for the average
programmer so as to make decorators such as memoize, tracing,
redirecting_stdout, locked, etc. more accessible.

%prep
%setup -q -n decorator-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python src/tests/test.py -v

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.md README.md
%{python_sitelib}/decorator.py*
%pycache_only %{python_sitelib}/__pycache__/decorator.*.py*
%{python_sitelib}/decorator-%{version}-py*.egg-info

%changelog
