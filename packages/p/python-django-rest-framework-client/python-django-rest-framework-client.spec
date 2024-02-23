#
# spec file for package python-django-rest-framework-client
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


%define skip_python39 1
Name:           python-django-rest-framework-client
Version:        0.10.0
Release:        0
Summary:        Python client for a Django REST Framework based web site
License:        MIT
URL:            https://github.com/dkarchmer/django-rest-framework-client
Source:         https://github.com/dkarchmer/django-rest-framework-client/archive/v%{version}.tar.gz#/django-rest-framework-client-%{version}.tar.gz
Patch0:         python-django-rest-framework-client-no-mock.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Python client for a Django REST Framework based web site.

%prep
%autosetup -p1 -n django-rest-framework-client-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/drf_client
%{python_sitelib}/django_rest_framework_client-%{version}.dist-info

%changelog
