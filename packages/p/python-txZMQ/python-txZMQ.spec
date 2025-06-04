#
# spec file for package python-txZMQ
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-txZMQ
Version:        1.0.0
Release:        0
Summary:        Twisted bindings for ZeroMQ
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/smira/txZMQ
Source:         https://files.pythonhosted.org/packages/source/t/txZMQ/txZMQ-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 10.0
Requires:       python-pyzmq >= 13
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted >= 10.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 13}
# /SECTION
%python_subpackages

%description
txZMQ allows to integrate ZeroMQ sockets into Twisted event loop (reactor).
It supports both CPython and PyPy, and ZeroMQ library versions 2.2.x or 3.2.x.

%prep
%setup -q -n txZMQ-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt README.rst
%{python_sitelib}/tx[Zz][Mm][Qq]
%{python_sitelib}/tx[Zz][Mm][Qq]-%{version}.dist-info

%changelog
