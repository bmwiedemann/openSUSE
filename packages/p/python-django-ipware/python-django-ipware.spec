#
# spec file for package python-django-ipware
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


%{?sle15_python_module_pythons}
Name:           python-django-ipware
Version:        5.0.2
Release:        0
Summary:        Django utility application that returns client's real IP address
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/un33k/django-ipware
Source:         https://github.com/un33k/django-ipware/archive/refs/tags/v%{version}.tar.gz#/django-ipware-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=ipware.tests.testsettings
%python_exec -m django test -v 2

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipware
%{python_sitelib}/django_ipware-%{version}.dist-info

%changelog
