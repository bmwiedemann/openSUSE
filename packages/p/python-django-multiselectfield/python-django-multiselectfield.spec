#
# spec file for package python-django-multiselectfield
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-multiselectfield
Version:        0.1.12
Release:        0
Summary:        Django multiple select field
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/goinnn/django-multiselectfield
Source:         https://github.com/goinnn/django-multiselectfield/archive/v%{version}.tar.gz#/django-multiselectfield-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.4}
# /SECTION
%python_subpackages

%description
Django multiple select field.

%prep
%setup -q -n django-multiselectfield-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
%python_exec example/run_tests.py

%files %{python_files}
%doc CHANGES.rst README.rst
%license COPYING.LGPLv3
%{python_sitelib}/*

%changelog
