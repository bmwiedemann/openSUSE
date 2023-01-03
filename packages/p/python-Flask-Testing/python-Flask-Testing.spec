#
# spec file for package python-Flask-Testing
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


Name:           python-Flask-Testing
Version:        0.8.1
Release:        0
Summary:        Unit testing for Flask
License:        BSD-3-Clause
URL:            https://github.com/jarus/flask-testing
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Testing/Flask-Testing-%{version}.tar.gz
Patch0:         skip-broken-tests.patch
# PATCH-FIX-OPENSUSE fix-utils.patch gh#jarus/flask-testing#157
Patch1:         fix-utils.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module importlib_metadata}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requre}
# /SECTION
%python_subpackages

%description
Unit testing for Flask.

%prep
%autosetup -p1 -n Flask-Testing-%{version}
# Remove Python 2-only unmaintained test dependency twill
# which includes a lot of outdated vendored packages
sed -i "s/twill[^']*/setuptools/" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest tests.suite

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/flask_testing
%{python_sitelib}/Flask_Testing-%{version}-py*.egg-info

%changelog
