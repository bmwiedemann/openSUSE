#
# spec file for package python-django-invitations
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-invitations
Version:        1.9.2
Release:        0
Summary:        Generic invitations app with support for Django-allauth
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/bee-keeper/django-invitations
Source:         https://github.com/bee-keeper/django-invitations/archive/%{version}.tar.gz
Patch0:         django20.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-allauth}
BuildRequires:  %{python_module freezegun >= 0.3.5}
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-django >= 3.1.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Recommends:     python-django-allauth
BuildArch:      noarch
%python_subpackages

%description
Generic invitations app with support for Django-allauth.

%prep
%setup -q -n django-invitations-%{version}
%patch0 -p1
rm tox.ini

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v tests/basic/tests.py --ds=test_settings
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v tests/allauth/test_allauth.py --ds=test_allauth_settings

%files %{python_files}
%license LICENSE
%{python_sitelib}/invitations/
%{python_sitelib}/django_invitations-*.egg-info/

%changelog
