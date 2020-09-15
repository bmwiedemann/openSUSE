#
# spec file for package python-django-ipware
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
Name:           python-django-ipware
Version:        3.0.1
Release:        0
Summary:        Django utility application that returns client's real IP address
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/un33k/django-ipware
Source:         https://files.pythonhosted.org/packages/source/d/django-ipware/django-ipware-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A Django utility application that returns client's real IP address.

%prep
%setup -q -n django-ipware-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=ipware.tests.testsettings
%python_exec -m django test -v 2

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
