#
# spec file for package python-django-cors-headers
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-django-cors-headers
Version:        4.4.0
Release:        0
Summary:        A Django App that adds CORS headers to responses
License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source:         https://github.com/adamchainz/django-cors-headers/archive/refs/tags/%{version}.tar.gz#/django-cors-headers-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A Django App that adds CORS (Cross-Origin Resource Sharing) headers to
responses.

%prep
%setup -q -n django-cors-headers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$PWD
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/corsheaders/
%{python_sitelib}/django[-_]cors[-_]headers*/

%changelog
