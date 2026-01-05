#
# spec file for package python-django-attachments
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-django-attachments
Version:        1.12
Release:        0
Summary:        Attach files to any Django model
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bartTC/django-attachments
Source:         https://files.pythonhosted.org/packages/source/d/django_attachments/django_attachments-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django >= 1.11
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module django >= 1.11}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
django-attachments is generic Django application to attach Files (Attachments) to any model.

%prep
%setup -q -n django_attachments-%{version}
sed -i '/mock/d;/-cov/d;/flakes/d' setup.cfg
sed -i 's/import mock/from unittest import mock/' attachments/tests/test_views.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/attachments/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export DJANGO_SETTINGS_MODULE=attachments.tests.testapp.settings
PYTHONPATH=.
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/attachments
%{python_sitelib}/django_attachments-%{version}.dist-info

%changelog
