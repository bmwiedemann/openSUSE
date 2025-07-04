#
# spec file for package python-django-coverage-plugin
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-django-coverage-plugin
Version:        3.1.0
Release:        0
Summary:        Django template coveragepy plugin
License:        Apache-2.0
URL:            https://github.com/nedbat/django_coverage_plugin
Source:         https://github.com/nedbat/django_coverage_plugin/archive/v%{version}.tar.gz#/django_coverage_plugin-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-coverage >= 4.0
Provides:       python-django_coverage_plugin = %{version}
Obsoletes:      python-django_coverage_plugin < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module unittest-mixins}
# /SECTION
%python_subpackages

%description
Django template coverage.py plugin

%prep
%autosetup -p1 -n django_coverage_plugin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/django_coverage_plugin
%{python_sitelib}/django_coverage_plugin-%{version}.dist-info

%changelog
