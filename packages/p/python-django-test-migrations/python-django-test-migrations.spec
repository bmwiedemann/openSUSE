#
# spec file for package python-django-test-migrations
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

%define short_name django-test-migrations
%define package_name django_test_migrations
Name:           python-django-test-migrations
Version:        1.5.0
Release:        0
Summary:        Test django schema and data migrations
License:        MIT
URL:            https://github.com/wemake-services/django-test-migrations
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros 
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 8.2}
BuildRequires:  %{python_module django >= 4.2}
BuildRequires:  %{python_module pytest-django >= 4.8}
BuildRequires:  %{python_module pytest-mock > 3.14}
BuildRequires:  %{python_module pytest-cov >= 6.0}
BuildRequires:  fdupes
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Features:
* Allows to test django schema and data migrations
* Allows to test both forward and rollback migrations
* Allows to test the migrations order
* Allows to test migration names
* Allows to test database configuration
* Fully typed with annotations and checked with mypy, PEP561 compatible
* Easy to start: has lots of docs, tests, and tutorials

%prep
%autosetup -p1 -n %{short_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{package_name}

%check
export DJANGO_DATABASE_NAME=db
%pytest --import-mode=importlib --no-cov -k 'not (test_managepy_check or test_call_pytest_setup_plan or test_pytest_markers)'

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/%{package_name}
%exclude %{python_sitelib}/%{package_name}/__pycache__
%{python_sitelib}/%{package_name}-%{version}.*-info
%pycache_only %{python_sitelib}/%{package_name}/__pycache__

%changelog

