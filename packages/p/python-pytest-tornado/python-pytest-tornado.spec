#
# spec file for package python-pytest-tornado
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
Name:           python-pytest-tornado
Version:        0.8.0
Release:        0
Summary:        A py.test plugin for tornado applications
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/eugeniy/pytest-tornado
Source:         https://files.pythonhosted.org/packages/source/p/pytest-tornado/pytest-tornado-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-pytest
Requires:       python-tornado >= 4.1
BuildArch:      noarch
%python_subpackages

%description
A py.test_ plugin providing fixtures and markers to simplify testing
of asynchronous tornado applications.

%prep
%setup -q -n pytest-tornado-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
