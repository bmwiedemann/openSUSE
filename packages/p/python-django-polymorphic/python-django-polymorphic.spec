#
# spec file for package python-django-polymorphic
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-django-polymorphic
Version:        4.11.7
Release:        0
Summary:        Polymorphic inheritance for Django models
License:        BSD-3-Clause
URL:            https://github.com/django-commons/django-polymorphic
Source:         https://github.com/django-commons/django-polymorphic/archive/v%{version}.tar.gz#/django-polymorphic-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-typing-extensions >= 4.12
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module django-test-migrations}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 4.12}
# /SECTION
%python_subpackages

%description
Seamless polymorphic inheritance for Django models.

%prep
%autosetup -p1 -n django-polymorphic-%{version}
# Remove after hatchling adds this classifier
sed -i '/Django :: 6.1/d' pyproject.toml
# No --headed option, added by pytest-playwright, not packaged
sed -i 's/not config.getoption("--headed")/True/' conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE="polymorphic.tests.debug"
export SQLITE_DATABASES="test1.db,test2.db"
# Requires pytest-playwright
ignore="--ignore src/polymorphic/tests/examples/integrations/extra_views/test.py "
ignore+="--ignore src/polymorphic/tests/examples/integrations/reversion/test.py "
ignore+="--ignore src/polymorphic/tests/examples/views/test.py "
ignore+="--ignore src/polymorphic/tests/test_admin.py "
ignore+="--ignore src/polymorphic/tests/test_migrations/test_on_delete.py "
ignore+="--ignore src/polymorphic/tests/test_serialization.py"
%pytest $ignore

%files %{python_files}
%doc README.md docs/*.rst
%license LICENSE
%{python_sitelib}/polymorphic
%{python_sitelib}/django_polymorphic-%{version}.dist-info

%changelog
