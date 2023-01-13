#
# spec file for package python-django-ckeditor
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
Name:           python-django-ckeditor
Version:        6.5.1
Release:        0
Summary:        Django admin CKEditor integration
License:        BSD-3-Clause
URL:            https://github.com/django-ckeditor/django-ckeditor
Source:         https://files.pythonhosted.org/packages/source/d/django-ckeditor/django-ckeditor-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-django-js-asset
BuildArch:      noarch
%python_subpackages

%description
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing
support included.

%prep
%setup -q -n django-ckeditor-%{version}

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
%{python_sitelib}/*

%changelog
