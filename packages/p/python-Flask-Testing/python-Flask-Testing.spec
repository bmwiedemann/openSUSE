#
# spec file for package python-Flask-Testing
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Testing
Version:        0.7.1
Release:        0
License:        BSD-3-Clause
Summary:        Unit testing for Flask
Url:            https://github.com/jarus/flask-testing
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Testing/Flask-Testing-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module blinker}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Flask
BuildArch:      noarch

%python_subpackages

%description
Unit testing for Flask.

%prep
%setup -q -n Flask-Testing-%{version}
# Remove Python 2-only unmaintained test dependency twill
# which includes a lot of outdated vendored packages
sed -i "s/twill[^']*/setuptools/" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
