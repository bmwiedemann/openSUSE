#
# spec file for package python-django-classy-tags
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-django-classy-tags
Version:        4.1.0
Release:        0
Summary:        Class based template tags for Django
License:        MIT
URL:            https://github.com/ojii/django-classy-tags
Source:         https://github.com/divio/django-classy-tags/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
BuildArch:      noarch
%python_subpackages

%description
This project creates an altnerate way of writing Django template tags
which is fully compatible with the current Django templating infrastructure.

%prep
%autosetup -p1 -n django-classy-tags-%{version}
sed -i 's/verbosity=1/verbosity=2/' tests/settings.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH='.'
%python_exec tests/settings.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/classytags
%{python_sitelib}/django_classy_tags-%{version}.dist-info

%changelog
