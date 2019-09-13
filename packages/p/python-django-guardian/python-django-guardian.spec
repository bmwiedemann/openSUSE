#
# spec file for package python-django-guardian
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


%define pypi_package_name django-guardian
Name:           python-%{pypi_package_name}
Version:        1.5.1
Release:        0
Url:            http://github.com/lukaszb/django-guardian
Summary:        Implementation of per object permissions for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/d/django-guardian/django-guardian-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module django-environ}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
BuildArch:      noarch
%python_subpackages

%description
django-guardian is implementation of per object permissions as
authorization backend.

%prep
%setup -q -n django-guardian-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/guardian/testapp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# mv's avoid pytest's compiled file conflict detection.
rm -rf build/ _build*/
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python setup.py test

%files %{python_files}
%doc CHANGES README.rst
%{python_sitelib}/*

%changelog
