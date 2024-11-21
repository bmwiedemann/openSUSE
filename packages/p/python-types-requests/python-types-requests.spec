#
# spec file for package python-types-requests
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-types-requests
Version:        2.32.0.20241016
Release:        0
Summary:        Typing stubs for requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python/typeshed
Source:         https://files.pythonhosted.org/packages/source/t/types-requests/types-requests-%{version}.tar.gz
Source99:       python-types-requests.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module urllib3 >= 2}
BuildRequires:  %{python_module mypy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-urllib3 >= 2
BuildArch:      noarch
%python_subpackages

%description
Typing stubs for requests
This is a PEP 561 type stub package for the requests package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
requests. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/requests. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.

%prep
%autosetup -p1 -n types-requests-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m mypy -p requests-stubs

%files %{python_files}
%doc CHANGELOG.md
%{python_sitelib}/requests-stubs
%{python_sitelib}/types_requests-%{version}.dist-info

%changelog
