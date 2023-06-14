#
# spec file for package python-pip-api
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
Name:           python-pip-api
Version:        0.0.30
Release:        0
Summary:        The official unofficial pip API
License:        Apache-2.0
URL:            https://github.com/di/pip-api
Source0:        https://github.com/di/pip-api/releases/download/%{version}/pip-api-%{version}.tar.gz
Source1:        test-data.tar.gz
# PATCH-FIX-OPENSUSE We do not want a vendored packaging.
Patch0:         unvendor.patch
# PATCH-FIX-OPENSUSE Remove a test parameter that is broken with our shipped
# packaging.
Patch1:         support-packaging-changes.patch
BuildRequires:  %{python_module packaging >= 21.0}
BuildRequires:  %{python_module pip >= 22.1}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyparsing >= 2.4.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pip
BuildArch:      noarch
%python_subpackages

%description
The official unofficial pip API.

%prep
%autosetup -p1 -a 1 -n pip-api-%{version}
rm -Rf ./pip_api/_vendor

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken with current packaging ; requires network
%pytest -k 'not (test_installed_distributions_legacy_version)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pip_api
%{python_sitelib}/pip_api*info

%changelog
