#
# spec file for package python-django-reversion
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
Name:           python-django-reversion
Version:        3.0.4
Release:        0
Summary:        A Django extension that provides version control for model instances
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/etianen/django-reversion
Source:         https://files.pythonhosted.org/packages/source/d/django-reversion/django-reversion-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Obsoletes:      python-django-reversion-doc
Obsoletes:      python-django-reversion-lang
BuildArch:      noarch
%python_subpackages

%description
Django-reversion is an extension to the Django web framework that provides
version control for model instances.

-  Roll back to any point in a model instance's history.
-  Recover deleted model instances.
-  Simple admin integration.

%prep
%setup -q -n django-reversion-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE
%{python_sitelib}/*

%changelog
