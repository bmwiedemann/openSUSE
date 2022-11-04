#
# spec file for package python-django-oscar
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
Name:           python-django-oscar
Version:        3.1
Release:        0
Summary:        Django domain-driven e-commerce framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-oscar/django-oscar
Source:         https://github.com/django-oscar/django-oscar/archive/%{version}.tar.gz#/django-oscar-%{version}.tar.gz
# PATCH-FIX-OPENSUSE django-41-compat.patch to fix tests with django-4.1
# gh#django-oscar/django-oscar#3908
Patch:          django-41-compat.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 1.0
Requires:       python-Django >= 1.11
Requires:       python-Pillow >= 4.0
Requires:       python-django-extra-views >= 0.11
Requires:       python-django-haystack >= 2.5.0
Requires:       python-django-phonenumber-field >= 2.0
Requires:       python-django-tables2 >= 1.19
Requires:       python-django-treebeard >= 4.3.0
Requires:       python-django-widget-tweaks >= 1.4.1
Requires:       python-phonenumbers
Requires:       python-purl >= 0.7
Suggests:       python-easy-thumbnails >= 2.5
Suggests:       python-factory_boy >= 2.4.1
Suggests:       python-sorl-thumbnail >= 12.4.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Babel >= 1.0}
BuildRequires:  %{python_module Pillow >= 4.0}
BuildRequires:  %{python_module WebTest >= 2.0}
BuildRequires:  %{python_module django >= 1.11}
BuildRequires:  %{python_module django-extra-views >= 0.11}
BuildRequires:  %{python_module django-haystack >= 2.5.0}
BuildRequires:  %{python_module django-phonenumber-field >= 2.0}
BuildRequires:  %{python_module django-tables2 >= 1.19}
BuildRequires:  %{python_module django-treebeard >= 4.3.0}
BuildRequires:  %{python_module django-webtest >= 1.9}
BuildRequires:  %{python_module django-widget-tweaks >= 1.4.1}
BuildRequires:  %{python_module easy-thumbnails >= 2.5}
BuildRequires:  %{python_module factory_boy >= 2.4.1}
BuildRequires:  %{python_module freezegun >= 1.1}
BuildRequires:  %{python_module phonenumbers}
BuildRequires:  %{python_module psycopg2 >= 2.8}
BuildRequires:  %{python_module purl >= 0.7}
BuildRequires:  %{python_module pytest-django >= 3.7}
BuildRequires:  %{python_module sorl-thumbnail >= 12.4.1}
# /SECTION
%python_subpackages

%description
A domain-driven e-commerce framework for Django.

%prep
%autosetup -p1 -n django-oscar-%{version}
sed -i "s/,<[0-9.]*'/'/" setup.py

sed -i 's/^import factory/import factory, factory.django/;s/factory.DjangoModelFactory/factory.django.DjangoModelFactory/' src/oscar/test/factories/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#django-oscar/django-oscar#3659
dont_test='test_updating_subtree_slugs_when_moving_category_to_new_parent or test_updating_subtree_when_moving_category_to_new_sibling '
dont_test+='or TestConcurrentOrderPlacement or test_raises_exception_if_app_has_already_been_forked'
# gh#django-oscar/django-oscar#3883
dont_test+=' or test_delete_object or test_delete_popup_object or test_check_verification_hash_valid'
dont_test+=' or test_redirects_to_parent_list_after_creating_child_category or test_verification_hash_generation or test_voucher_delete_view_for_voucher_in_set'
%pytest --sqlite -k "not (${dont_test})"

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/oscar
%{python_sitelib}/django_oscar-%{version}*-info

%changelog
