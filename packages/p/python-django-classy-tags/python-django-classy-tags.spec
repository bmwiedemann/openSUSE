#
# spec file for package python-django-classy-tags
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
Name:           python-django-classy-tags
Version:        0.9.0
Release:        0
Summary:        Class based template tags for Django
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/ojii/django-classy-tags
Source:         https://github.com/divio/django-classy-tags/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
%python_subpackages

%description
This project creates an altnerate way of writing Django template tags
which is fully compatible with the current Django templating infrastructure.

%prep
%setup -q -n django-classy-tags-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
