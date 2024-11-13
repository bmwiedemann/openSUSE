#
# spec file for package python-django-silk
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-django-silk
Version:        5.3.1
Release:        0
Summary:        Profiling for the Django Framework
License:        MIT
URL:            https://github.com/jazzband/django-silk
Source:         https://files.pythonhosted.org/packages/source/d/django-silk/django_silk-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-autopep8 >= 1.2.1
Requires:       python-gprof2dot >= 2017.09.19
Requires:       python-sqlparse >= 0.1.19
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module autopep8 >= 1.2.1}
BuildRequires:  %{python_module factory_boy >= 3.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module gprof2dot >= 2017.09.19}
BuildRequires:  %{python_module networkx >= 2.6}
BuildRequires:  %{python_module pydot >= 1.4}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sqlparse >= 0.1.19}
# /SECTION
%python_subpackages

%description
Profiling for the Django Framework.

%prep
%setup -n django_silk-%{version}
chmod a-x silk/static/silk/lib/*.css
chmod a-x silk/static/silk/lib/*.js

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd project
export DB_ENGINE=sqlite3 DB_NAME=":memory:"
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/silk
%{python_sitelib}/django_silk-%{version}.dist-info

%changelog
