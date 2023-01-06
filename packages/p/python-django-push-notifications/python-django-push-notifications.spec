#
# spec file for package python-django-push-notifications
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-push-notifications
Version:        3.0.0
Release:        0
Summary:        Django package to send push notifications to mobile devices
License:        MIT
URL:            https://github.com/jazzband/django-push-notifications
Source:         https://github.com/jazzband/django-push-notifications/archive/%{version}.tar.gz#/django-push-notifications-%{version}.tar.gz
Patch0:         support-new-apns2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-pywebpush >= 1.3.0
Suggests:       python-apns2 >= 0.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module apns2}
BuildRequires:  %{python_module django-codemod}
BuildRequires:  %{python_module djangorestframework >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pywebpush >= 1.3.0}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Send push notifications to mobile devices through GCM, APNS or WNS and
to WebPush (Chrome, Firefox and Opera) in Django.

%prep
%autosetup -p1 -n django-push-notifications-%{version}
djcodemod run --removed-in 4.0 push_notifications/{admin,fields,models}.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH="$(pwd)"
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
