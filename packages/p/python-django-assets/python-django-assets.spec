#
# spec file for package python-django-assets
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


Name:           python-django-assets
Version:        2.0
Release:        0
Summary:        Django asset management to compress and merge CSS and Javascript files
License:        BSD-2-Clause
URL:            https://github.com/miracle2k/django-assets
Source:         https://files.pythonhosted.org/packages/source/d/django-assets/django-assets-%{version}.tar.gz
Patch0:         remove-nose.patch
# PATCH-FIX-UPSTREAM gh#miracle2k/django-assets#104
Patch1:         support-python-311.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.7
Requires:       python-webassets >= 2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module webassets >= 2.0}
# /SECTION
%python_subpackages

%description
Asset management for Django, to compress and merge CSS and Javascript files.

%prep
%autosetup -p1 -n django-assets-%{version}
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/miracle2k/django-assets/issues/101
%pytest -k 'not TestLoader'

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/django_assets*

%changelog
