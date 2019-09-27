#
# spec file for package python-toro
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
Name:           python-toro
Version:        1.0.1
Release:        0
Summary:        Synchronization primitives for Tornado coroutines
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ajdavis/toro/
Source:         https://files.pythonhosted.org/packages/source/t/toro/toro-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado < 5.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tornado < 5.0
BuildArch:      noarch
%python_subpackages

%description
A set of locking and synchronizing primitives analogous to those in Python's
`threading module`_ or Gevent's `coros`_, for use with Tornado's `gen.engine`_.

%prep
%setup -q -n toro-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
