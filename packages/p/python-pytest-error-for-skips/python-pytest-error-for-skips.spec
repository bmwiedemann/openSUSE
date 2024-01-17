#
# spec file for package python-pytest-error-for-skips
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
Name:           python-pytest-error-for-skips
Version:        2.0.2
Release:        0
Summary:        Pytest plugin to treat skipped tests a test failure
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jankatins/pytest-error-for-skips
Source:         https://github.com/jankatins/pytest-error-for-skips/archive/%{version}.tar.gz#/pytest-error-for-skips-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.6}
# /SECTION
%python_subpackages

%description
Pytest plugin to treat skipped tests a test failures.

This is nice if you want to ensure that your CI tests
really run all tests and don't skip tests because of
missing dependencies.

%prep
%setup -q -n pytest-error-for-skips-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
