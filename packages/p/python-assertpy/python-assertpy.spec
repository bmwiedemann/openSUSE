#
# spec file for package python-assertpy
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-assertpy
Version:        1.1
Release:        0
Summary:        Simple assertion library for unit testing in python with a fluent API
License:        BSD-3-Clause
URL:            https://github.com/assertpy/assertpy
Source:         https://github.com/assertpy/assertpy/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildArch:      noarch
%python_subpackages

%description
Simple assertion library for unit testing in python with a fluent API

%prep
%autosetup -p1 -n assertpy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/assertpy
%{python_sitelib}/assertpy-%{version}.dist-info

%changelog
