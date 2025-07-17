#
# spec file for package python-nodeenv
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


%bcond_without libalternatives
%{?sle15allpythons}
Name:           python-nodeenv
Version:        1.9.1
Release:        0
Summary:        Nodejs virtual environment builder
License:        BSD-3-Clause
URL:            https://github.com/ekalinin/nodeenv
Source:         https://github.com/ekalinin/nodeenv/archive/%{version}.tar.gz#/nodeenv-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Node.js virtual environment builder.

%prep
%autosetup -p1 -n nodeenv-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nodeenv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_smoke is an integration test requiring network access.
%pytest -k 'not test_smoke'

%pre
%python_libalternatives_reset_alternative nodeenv

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%python_alternative %{_bindir}/nodeenv
%{python_sitelib}/nodeenv.py
%pycache_only %{python_sitelib}/__pycache__/nodeenv.*.pyc
%{python_sitelib}/nodeenv-%{version}.dist-info

%changelog
