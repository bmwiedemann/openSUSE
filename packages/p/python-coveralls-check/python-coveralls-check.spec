#
# spec file for package python-coveralls-check
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


%{?sle15_python_module_pythons}
Name:           python-coveralls-check
Version:        1.2.1
Release:        0
Summary:        Coverage checking using https://coveralls.io/
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cjw296/coverage-check
Source:         https://files.pythonhosted.org/packages/source/c/coveralls-check/coveralls-check-%{version}.tar.gz
# https://github.com/cjw296/coveralls-check/issues/3
Patch0:         python-coveralls-check-no-mock.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backoff
Requires:       python-requests
Requires:       python-setuptools
Requires(post): alts
Requires(postun): alts
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module backoff}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module testfixtures}
# /SECTION
%python_subpackages

%description
A helper to check https://coveralls.io for a given commit hash.

%prep
%setup -q -n coveralls-check-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/coveralls-check
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%post
%python_install_alternative coveralls-check

%postun
%python_uninstall_alternative coveralls-check

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/coveralls-check
%{python_sitelib}/coveralls[-_]check.py
%{python_sitelib}/coveralls[-_]check-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/coveralls[-_]check*

%changelog
