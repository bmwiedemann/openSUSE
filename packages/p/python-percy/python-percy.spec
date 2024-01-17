#
# spec file for package python-percy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-percy
Version:        2.0.2
Release:        0
Summary:        Visual regression testing library
License:        MIT
URL:            https://github.com/percy/python-percy-client
Source:         https://files.pythonhosted.org/packages/source/p/percy/percy-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.14.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.14.0
BuildArch:      noarch
%python_subpackages

%description
Python client library for visual regression testing with Percy.

%prep
%setup -q -n percy-%{version}
# support urllib3 v2
sed -i 's/method_whitelist/allowed_methods/g' percy/connection.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_commit_live - needs initialized git repo
%pytest -k 'not test_commit_live'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
