#
# spec file for package python-django-braces
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
Name:           python-django-braces
Version:        1.13.0
Release:        0
Summary:        Reusable, generic mixins for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/brack3t/django-braces/
Source:         https://files.pythonhosted.org/packages/source/d/django-braces/django-braces-%{version}.tar.gz
Source1:        form.html
Patch0:         dj21.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module Django}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-Django
%python_subpackages

%description
Reusable, generic mixins for Django.

%prep
%setup -q -n django-braces-%{version}
%patch0 -p1
# https://github.com/brack3t/django-braces/pull/249
mkdir tests/templates/
cp %{SOURCE1} tests/templates/
touch tests/templates/blank.html
echo '<h1>404!!!!</h1>' > tests/templates/404.html

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
%python_exec -m pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
