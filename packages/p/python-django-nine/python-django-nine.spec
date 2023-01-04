#
# spec file for package python-django-nine
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
%define skip_python36 1
Name:           python-django-nine
Version:        0.2.7
Release:        0
Summary:        Compatibility library for Django
License:        GPL-2.0-only OR LGPL-2.1-or-later
URL:            https://github.com/barseghyanartur/django-nine/
Source:         https://files.pythonhosted.org/packages/source/d/django-nine/django-nine-%{version}.tar.gz
# https://github.com/barseghyanartur/django-nine/issues/8
Patch0:         python-django-nine-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
BuildArch:      noarch

%python_subpackages

%description
Version checking library for Django.

%prep
%autosetup -p1 -n django-nine-%{version}
chmod a-x LICENSE_* CHANGELOG.rst README.rst

# Remove backwards compatibility layer
rm src/nine/__init__.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/django_nine/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest src/django_nine/tests/

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt
%{python_sitelib}/*

%changelog
