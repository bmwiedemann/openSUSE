#
# spec file for package python-django-geoposition
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


Name:           python-django-geoposition
Version:        0.3.0
Release:        0
Summary:        Django model field that can hold a geoposition
License:        MIT
URL:            https://github.com/philippbosch/django-geoposition
Source:         https://files.pythonhosted.org/packages/source/d/django-geoposition/django-geoposition-%{version}.tar.gz
Patch0:         pr_110.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module django-codemod}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Django model field that can hold a geoposition, and corresponding admin widget.

%prep
%autosetup -p1 -n django-geoposition-%{version}
djcodemod run --removed-in 4.0 geoposition/fields.py geoposition/forms.py geoposition/widgets.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/example/ %{buildroot}%{$python_sitelib}/geoposition/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export DJANGO_SETTINGS_MODULE=geoposition.tests.settings
%python_exec -m django test -v2 geoposition

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/geoposition
%{python_sitelib}/django_geoposition-%{version}.dist-info

%changelog
