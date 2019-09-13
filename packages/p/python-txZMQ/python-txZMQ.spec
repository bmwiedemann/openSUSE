#
# spec file for package python-txZMQ
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
%bcond_with test
Name:           python-txZMQ
Version:        0.8.0
Release:        0
Summary:        Twisted bindings for ZeroMQ
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/smira/txZMQ
Source:         https://files.pythonhosted.org/packages/source/t/txZMQ/txZMQ-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
txZMQ allows to integrate ZeroMQ sockets into Twisted event loop (reactor).
It supports both CPython and PyPy, and ZeroMQ library versions 2.2.x or 3.2.x.

%prep
%setup -q -n txZMQ-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt README.rst
%{python_sitelib}/*

%changelog
