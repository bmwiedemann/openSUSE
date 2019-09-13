#
# spec file for package python-django-pipeline
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-pipeline
Version:        1.6.14
Release:        0
Summary:        An asset packaging library for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-pipeline
Source:         https://files.pythonhosted.org/packages/source/d/django-pipeline/django-pipeline-%{version}.tar.gz
Patch0:         django-pipeline-setpcfg.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module setuptools}
BuildRequires: sqlite3
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-futures
BuildRequires:  python2-mock
Requires:       python-Jinja2
Requires:       python-Django >= 1.11
BuildArch:      noarch
%ifpython2
Requires:       python2-futures
%endif
%python_subpackages

%description
Pipeline is an asset packaging library for Django, providing both CSS and
JavaScript concatenation and compression, built-in JavaScript template support,
and optional data-URI image and font embedding.

%prep
%setup -q -n django-pipeline-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The tests quite spectaculary fail on newer django releases, upstream must fix
#%check
#export DJANGO_SETTINGS_MODULE=tests.settings
#%%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
