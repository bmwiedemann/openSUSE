#
# spec file for package python-django-pandas
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
Name:           python-django-pandas
Version:        0.6.6
Release:        0
Summary:        Tools for working with pandas in Django projects
License:        BSD-3-Clause
URL:            https://github.com/chrisdev/django-pandas/
Source:         https://files.pythonhosted.org/packages/source/d/django-pandas/django-pandas-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-pandas >= 0.14.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pandas >= 0.20.1}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module semver >= 2.10.1}
# /SECTION
%python_subpackages

%description
Tools for working with pandas in Django projects.

%prep
%setup -q -n django-pandas-%{version}

sed -i 's/==/>=/;/coverage/d' setup.py
# Remove python-six deps from tests
sed -i '/python_2_unicode_compatible/, 1d' django_pandas/tests/models.py
# Remove python-six deps from requires
sed -i '/six/, 1d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Do not distribute tests with package
%python_expand rm -rf %{buildroot}%{$python_sitelib}/django_pandas/tests

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python runtests.py

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/django_pandas
%{python_sitelib}/django_pandas-%{version}*-info

%changelog
