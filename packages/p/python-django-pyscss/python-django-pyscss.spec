#
# spec file for package python-django-pyscss
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
Name:           python-django-pyscss
Version:        2.0.2
Release:        0
Summary:        A collection of tools to use pyScss within Django
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/fusionbox/django-pyscss
Source:         https://files.pythonhosted.org/packages/source/d/django-pyscss/django-pyscss-%{version}.tar.gz
Patch0:         no-discover-runner.patch
Patch1:         django10.patch
Patch2:         fix-testproject-settings.py.patch
Patch3:         django-1.10-urls.patterns-removed.patch
Patch4:         FTBFS-fix-unit-tests.patch
Patch5:         django-2.0.patch
Patch6:         crashing_templates.patch
BuildRequires:  %{python_module Django >= 1.10}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyScss >= 1.2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module django_compressor >= 1.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-pathlib
Requires:       python-Django >= 1.10
Requires:       python-pyScss >= 1.3.4
Requires:       python2-pathlib
%python_subpackages

%description
This app smooths over a lot of things when dealing with pyScss in Django. It

- Overwrites the import system to use Django's staticfiles app. This way, one
  can import SCSS files from any app (or any file that's findable by the
  STATICFILES_FINDERS).

- Configures pyScss to work with the staticfiles app for its image functions
  (e.g. inline-image and sprite-map).

- It provides a django-compressor precompile filter class so that the developer
  can use pyScss with django-compressor without having to bust out to the
  shell.  This has the added benefit of removing the need to configure pyScss
  through its command-line arguments, AND makes it possible for the exceptions
  and warnings that pyScss emits to bubble up to the process so that the user
  actually knows what's going on.

%prep
%setup -q -n django-pyscss-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# %%check
# Tests crash python interpreter gh#Kronuz/pyScss#378
# %%python_exec setup.py test -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/django_pyscss
%{python_sitelib}/django_pyscss-%{version}-py*.egg-info

%{python_sitelib}/*

%changelog
