#
# spec file for package python-async_generator
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
%define skip_python2 1
Name:           python-async_generator
Version:        1.10
Release:        0
Summary:        Async generators and context managers for Python 3.5+
License:        MIT OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/async_generator
Source:         https://files.pythonhosted.org/packages/source/a/async_generator/async_generator-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python 3.6 added async generators. Python 3.7 adds some more
tools to make them usable, like contextlib.asynccontextmanager.

%prep
%setup -q -n async_generator-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.MIT
%license LICENSE.APACHE2
%{python_sitelib}/async_generator
%{python_sitelib}/async_generator-%{version}*-info

%changelog
