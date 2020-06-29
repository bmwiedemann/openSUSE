#
# spec file for package python-django-widget-tweaks
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-widget-tweaks
Version:        1.4.8
Release:        0
Summary:        Django form field rendering in templates
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-widget-tweaks
Source:         https://files.pythonhosted.org/packages/source/d/django-widget-tweaks/django-widget-tweaks-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jazzband/django-widget-tweaks/master/runtests.py
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Tweak the form field rendering in templates, not in python-level form definitions.

%prep
%setup -q -n django-widget-tweaks-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
