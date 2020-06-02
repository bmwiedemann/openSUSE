#
# spec file for package python-django-rest-framework-client
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
%bcond_without  python2
Name:           python-django-rest-framework-client
Version:        0.1.1
Release:        0
Summary:        Python client for a Django REST Framework based web site
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dkarchmer/django-rest-framework-client
Source:         https://github.com/dkarchmer/django-rest-framework-client/archive/v%{version}.tar.gz#/django-rest-framework-client-%{version}.tar.gz
# fake dependency, https://github.com/dkarchmer/django-rest-framework-client/pull/2
Patch0:         python-django-rest-framework-client-no-unittest2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
%if %{with python2}
BuildRequires:  python-unittest2
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django
Requires:       python-requests
BuildArch:      noarch

%python_subpackages

%description
Python client for a Django REST Framework based web site.

%prep
%setup -q -n django-rest-framework-client-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
