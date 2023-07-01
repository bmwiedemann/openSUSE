#
# spec file for package python-django-mailman3
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


%{?sle15_python_module_pythons}
%define modname django_mailman3
Name:           python-django-mailman3
Version:        1.3.9
Release:        0
Summary:        Django library to help interaction with Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/django-mailman3
Source:         https://files.pythonhosted.org/packages/04/b0/34331deb242988466cd34ffaa04c316c5eaf40760998d9ff2055142e2c6a/django-mailman3-1.3.9.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-django-allauth
Requires:       python-django-gravatar2 >= 1.0.6
Requires:       python-mailmanclient
Requires:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-allauth}
BuildRequires:  %{python_module django-gravatar2 >= 1.0.6}
BuildRequires:  %{python_module mailmanclient}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
Django library to help interaction with Mailman.

%prep
%autosetup -p1 -n django-mailman3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="$(pwd)"
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/%{modname}-%{version}*-info
%{python_sitelib}/%{modname}

%changelog
