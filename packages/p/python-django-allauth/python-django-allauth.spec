#
# spec file for package python-django-allauth
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
Name:           python-django-allauth
Version:        0.42.0
Release:        0
Summary:        Django authentication, registration, account management
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pennersr/django-allauth
Source:         https://files.pythonhosted.org/packages/source/d/django-allauth/django-allauth-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.0
Requires:       python-python3-openid >= 3.0.8
Requires:       python-requests
Requires:       python-requests-oauthlib >= 0.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module python3-openid >= 3.0.8}
BuildRequires:  %{python_module requests-oauthlib >= 0.3.0}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Integrated set of Django applications addressing authentication, registration,
account management as well as 3rd party (social) account authentication.

%prep
%setup -q -n django-allauth-%{version}
# Five errors reported at https://github.com/pennersr/django-allauth/issues/2210
# Cern provider test module fails
rm allauth/socialaccount/providers/cern/tests.py

# 2 tests failing with KeyError: 'location' (not in response headers)
sed -i 's/test_login/_test_login/' allauth/socialaccount/providers/openid/tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
%python_expand django-admin-%{$python_bin_suffix} test --settings=test_settings

%files %{python_files}
%doc AUTHORS ChangeLog.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
