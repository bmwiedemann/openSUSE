#
# spec file for package python-django-babel
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-babel
Version:        0.6.2
Release:        0
Summary:        Utilities for using Babel in Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/graingert/django-babel/
Source:         https://files.pythonhosted.org/packages/source/d/django-babel/django-babel-%{version}.tar.gz
Patch0:         django21.patch
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 1.3
Requires:       python-Django >= 1.8
BuildArch:      noarch
%python_subpackages

%description
This package contains various utilities for integration of `Babel`_ into the
`Django`_ web framework:

 * A message extraction plugin for Django templates.
 * A middleware class that adds the Babel `Locale`_ object to requests.
 * A set of template tags for date and number formatting.

%prep
%setup -q -n django-babel-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license COPYING
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
