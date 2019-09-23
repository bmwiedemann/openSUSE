#
# spec file for package python-django-sekizai
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
Name:           python-django-sekizai
Version:        1.0.0
Release:        0
Summary:        Django Template Blocks with extra functionality
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ojii/django-sekizai
Source:         https://github.com/divio/django-sekizai/archive/%{version}.tar.gz
Patch0:         django-sekizai-pycodestyle.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-classy-tags >= 0.3.1}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-django-classy-tags >= 0.3.1
BuildArch:      noarch
%python_subpackages

%description
Django Template Blocks with extra functionality

%prep
%setup -q -n django-sekizai-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
