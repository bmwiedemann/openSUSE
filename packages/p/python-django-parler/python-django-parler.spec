#
# spec file for package python-django-parler
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
Name:           python-django-parler
Version:        2.3
Release:        0
Summary:        Simple Django model translations
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/edoburu/django-parler
Source:         https://github.com/django-parler/django-parler/archive/v%{version}.tar.gz#/django-parler-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module django-polymorphic}
# /SECTION
%python_subpackages

%description
Simple Django model translations without nasty hacks, including admin integration.

%prep
%setup -q -n django-parler-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py -v 2

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst docs/*.rst docs/*/*.rst
%license LICENSE
%{python_sitelib}/parler
%{python_sitelib}/django_parler-%{version}*-info

%changelog
