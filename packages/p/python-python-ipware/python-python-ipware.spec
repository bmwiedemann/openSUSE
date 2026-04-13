#
# spec file for package python-python-ipware
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-python-ipware
Version:        3.0.0
Release:        0
Summary:        A Python package to retrieve user's IP address
License:        MIT
URL:            https://github.com/un33k/python-ipware
Source:         https://files.pythonhosted.org/packages/source/p/python-ipware/python_ipware-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-coveralls >= 3.3
Suggests:       python-coverage
BuildArch:      noarch
%python_subpackages

%description
A Python package to retrieve user's IP address

%prep
%autosetup -p1 -n python_ipware-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests/test*.py

%files %{python_files}
%{python_sitelib}/python_ipware
%{python_sitelib}/python_ipware-%{version}.dist-info

%changelog
