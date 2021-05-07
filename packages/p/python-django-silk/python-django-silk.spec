#
# spec file for package python-django-silk
#
# Copyright (c) 2020 SUSE LLC
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
# Python 3.9 is supported by next release
%define skip_python39 1
Name:           python-django-silk
Version:        4.1.0
Release:        0
Summary:        Profiling for the Django Framework
License:        MIT
URL:            https://github.com/jazzband/django-silk
Source:         django-silk-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module Jinja2 >= 2.8}
BuildRequires:  %{python_module Pillow >= 3.2}
BuildRequires:  %{python_module Pygments >= 2.0}
BuildRequires:  %{python_module autopep8 >= 1.2.1}
BuildRequires:  %{python_module gprof2dot >= 2017.09.19}
BuildRequires:  %{python_module python-dateutil >= 2.4}
BuildRequires:  %{python_module pytz > 2014.2}
BuildRequires:  %{python_module requests >= 2.10}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlparse >= 0.1.19}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-Jinja2 >= 2.8
Requires:       python-Pillow >= 3.2
Requires:       python-Pygments >= 2.0
Requires:       python-autopep8 >= 1.2.1
Requires:       python-gprof2dot >= 2017.09.19
Requires:       python-python-dateutil >= 2.4
Requires:       python-pytz > 2014.2
Requires:       python-requests >= 2.10
Requires:       python-sqlparse >= 0.1.19
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module contextlib2 >= 0.5.5}
BuildRequires:  %{python_module factory_boy >= 2.8.1}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module networkx >= 1.11}
BuildRequires:  %{python_module pydotplus >= 2.0.2}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module simplejson >= 3.13.2}
BuildRequires:  %{python_module six >= 1.11.0}
# /SECTION
%python_subpackages

%description
Profiling for the Django Framework.

%prep
%setup -q -n django-silk-%{version}
chmod a-x silk/static/silk/lib/*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd project
export DB=sqlite3 DB_NAME=db.sqlite3
%{python_expand rm -f db.sqlite3
$python manage.py migrate --noinput
$python manage.py test --noinput
}
# DB=mysql DB_NAME=mysql_db

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
