#
# spec file for package python-django-extra-views
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
Name:           python-django-extra-views
Version:        0.14.0
Release:        0
Summary:        Extra class-based views for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AndrewIngram/django-extra-views
Source:         https://github.com/AndrewIngram/django-extra-views/archive/%{version}.tar.gz#/django-extra-views-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/AndrewIngram/django-extra-views/pull/233.patch#/merged_pr_233.patch
Patch1:         merged_10881330.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module pytest-django}
# /SECTION
%python_subpackages

%description
Extra class-based views for Django.

%prep
%autosetup -p1 -n django-extra-views-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=extra_views_tests.settings
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*extra[-_]views*/

%changelog
