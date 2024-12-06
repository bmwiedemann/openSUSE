#
# spec file for package python-django-ckeditor
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


%{?sle15_python_module_pythons}
Name:           python-django-ckeditor
Version:        6.7.2
Release:        0
Summary:        Django admin CKEditor integration
License:        BSD-3-Clause
URL:            https://github.com/django-ckeditor/django-ckeditor
Source:         https://files.pythonhosted.org/packages/source/d/django_ckeditor/django_ckeditor-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/ckeditor/ckeditor4/commit/8ed1a3c93d0ae5f49f4ecff5738ab8a2972194cb https://github.com/ckeditor/ckeditor4/security/advisories/GHSA-fq6h-4g8v-qqvm
Patch:          CVE-2024-24815.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-django-js-asset >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing
support included.

%prep
%autosetup -p1 -n django_ckeditor-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests need to be online and require web browser

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/ckeditor*
%{python_sitelib}/django_ckeditor-%{version}*info

%changelog
