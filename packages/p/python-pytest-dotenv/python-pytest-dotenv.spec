#
# spec file for package python-pytest-dotenv
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


Name:           python-pytest-dotenv
Version:        0.5.2
Release:        0
Summary:        A pytest plugin that parses environment files
License:        MIT
URL:            https://github.com/quiqua/pytest-dotenv
Source:         https://github.com/quiqua/pytest-dotenv/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module python-dotenv >= 0.9.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 5.0
Requires:       python-python-dotenv >= 0.9.1
BuildArch:      noarch
%python_subpackages

%description
A py.test plugin that parses environment files before running tests.

%prep
%setup -q -n pytest-dotenv-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytest_dotenv
%{python_sitelib}/pytest_dotenv-%{version}.dist-info

%changelog
