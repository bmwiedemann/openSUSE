#
# spec file for package python-django-coverage-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django_coverage_plugin
Version:        1.6.0
Release:        0
Summary:        Django template coveragepy plugin
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nedbat/django_coverage_plugin
Source:         https://github.com/nedbat/django_coverage_plugin/archive/v1.6.0.tar.gz#/django_coverage_plugin-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-coverage >= 4.0
Requires:       python-six >= 1.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module unittest-mixins}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module six >= 1.4.0}
# /SECTION
%python_subpackages

%description
Django template coverage.py plugin

%prep
%setup -q -n django_coverage_plugin-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc HISTORY.rst README.rst
%{python_sitelib}/*

%changelog
