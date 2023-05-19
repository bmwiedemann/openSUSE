#
# spec file for package python-responses
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-responses
Version:        0.23.1
Release:        0
Summary:        A utility library for mocking out the `requests` Python library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/responses
Source:         https://files.pythonhosted.org/packages/source/r/responses/responses-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 636-urllib3-2-compat.patch gh#getsentry/responses!636 mcepl@suse.com
# Make the package compatible with urllib3 >= 2.0
Patch0:         636-urllib3-2-compat.patch
# PATCH-FIX-UPSTREAM unbundle-urllib3.patch gh#getsentry/responses#635, mcepl@suse.com
# Don't use urllib3 bundled in requests.
Patch1:         unbundle-urllib3.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cookies}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.22 with %python-requests < 3}
BuildRequires:  %{python_module tomli-w}
BuildRequires:  %{python_module urllib3 >= 2}
# /SECTION
Requires:       python-PyYAML
Requires:       python-urllib3 >= 2
Requires:       (python-requests >= 2.22.0 with python-requests < 3)
BuildArch:      noarch
%python_subpackages

%description
A utility library for mocking out the requests Python library.
Check https://github.com/getsentry/responses for more information
about the library.

%prep
%autosetup -p1 -n responses-%{version}

# Remove typing stub requirements
sed -i /types-/d setup.py

%build
export LANG="en_US.UTF8"
export PYTHONIOENCODING="utf_8"
%pyproject_wheel

%install
export LANG="en_US.UTF8"
export PYTHONIOENCODING="utf_8"
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/responses
%{python_sitelib}/responses-%{version}*-info

%changelog
