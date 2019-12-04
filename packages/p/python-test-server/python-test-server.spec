#
# spec file for package python-test-server
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-test-server
Version:        0.0.31
Release:        0
Summary:        Server to test HTTP clients
License:        MIT
URL:            https://github.com/lorien/test_server
Source:         https://github.com/lorien/test_server/archive/v%{version}.tar.gz#/test-server-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebTest
Requires:       python-bottle >= 0.12.13
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module bottle >= 0.12.13}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Server to test HTTP clients.

%prep
%setup -q -n test_server-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_null_bytes failing on Python 2 only due to
# https://github.com/lorien/test_server/issues/13
%pytest -k 'not test_null_bytes'

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
