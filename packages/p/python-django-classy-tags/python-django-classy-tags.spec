#
# spec file for package python-django-classy-tags
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-django-classy-tags
Version:        2.0.0
Release:        0
Summary:        Class based template tags for Django
License:        MIT
URL:            https://github.com/ojii/django-classy-tags
Source:         https://github.com/divio/django-classy-tags/archive/%{version}.tar.gz
# https://github.com/django-cms/django-classy-tags/pull/66
Patch0:         dj40.patch
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
This project creates an altnerate way of writing Django template tags
which is fully compatible with the current Django templating infrastructure.

%prep
%setup -q -n django-classy-tags-%{version}
%patch0 -p1
sed -i 's/verbosity=1/verbosity=2/' tests/settings.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests

%check
export PYTHONPATH='.'
%python_exec tests/settings.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/classytags/
%{python_sitelib}/django_classy_tags*egg-info/

%changelog
