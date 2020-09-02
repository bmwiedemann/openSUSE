#
# spec file for package python-django-jsonfield
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
%define skip_python2 1
Name:           python-django-jsonfield
Version:        3.1.0
Release:        0
Summary:        A reusable Django field to store validated JSON
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dmkoch/django-jsonfield/
Source:         https://files.pythonhosted.org/packages/source/j/jsonfield/jsonfield-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
Django-jsonfield is a reusable Django field that allows you to
store validated JSON in your model.

%prep
%setup -q -n jsonfield-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=.
export DJANGO_SETTINGS_MODULE="tests.settings"
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
