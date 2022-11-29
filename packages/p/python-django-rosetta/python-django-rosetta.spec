#
# spec file for package python-django-rosetta
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
Name:           python-django-rosetta
Version:        0.9.8
Release:        0
Summary:        Django application that eases the translation of Django projects
License:        MIT
URL:            https://github.com/mbi/django-rosetta
Source:         https://files.pythonhosted.org/packages/source/d/django-rosetta/django-rosetta-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-Django >= 1.11
Requires:       python-polib >= 1.1.0
Requires:       python-requests >= 2.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module polib >= 1.1.0}
BuildRequires:  %{python_module pymemcache}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module requests >= 2.1.0}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  memcached
# /SECTION
%python_subpackages

%description
Django application that eases the translation of Django projects.

%prep
%setup -q -n django-rosetta-%{version}
# Workaround https://github.com/mbi/django-rosetta/issues/233
sed -i 's/test_47_azure_ajax_translation/_test_47_azure_ajax_translation/' rosetta/tests/tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd testproject
%{_bindir}/memcached &
%python_exec -Wd manage.py test -v2 rosetta

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/rosetta
%{python_sitelib}/django_rosetta-%{version}*-info

%changelog
