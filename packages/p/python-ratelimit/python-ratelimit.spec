#
# spec file for package python-ratelimit
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


%{?sle15_python_module_pythons}
Name:           python-ratelimit
Version:        2.2.1
Release:        0
Summary:        API rate limit decorator
License:        MIT
URL:            https://github.com/tomasbasham/ratelimit
# PyPI sdist lacks tests, use the GitHub tarball
Source:         %{url}/archive/v%{version}/ratelimit-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Function decorator that limits how often a function can be called
within a time period, for example to stay under the rate limit of a
remote API.

%prep
%autosetup -p1 -n ratelimit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# pytest.ini adds coverage options, pytest-cov is not needed
%pytest -o addopts="" tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/ratelimit
%{python_sitelib}/ratelimit-%{version}.dist-info

%changelog
