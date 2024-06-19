#
# spec file for package python-django-bootstrap4
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


%{?sle15_python_module_pythons}
Name:           python-django-bootstrap4
Version:        24.3
Release:        0
Summary:        Bootstrap support for Django projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/zostera/django-bootstrap4
Source:         https://github.com/zostera/django-bootstrap4/archive/v%{version}.tar.gz#/django-bootstrap4-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-beautifulsoup4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  gdal-devel
# /SECTION
%python_subpackages

%description
Bootstrap support for Django projects.

%prep
%autosetup -p1 -n django-bootstrap4-%{version}

# Remove need to install gis, as the tests do not exercise this yet
sed -i '/django.contrib.gis/d' tests/app/settings.py
sed -Ei '/(gisform|polygon)/d' tests/forms.py

# gh#zostera/django-bootstrap4#662
# Upstream uses setuptools_scm that adds everything in the git
# repository so we need to do the same here manually to do not depend
# on git.
cat << EOF > MANIFEST.in
recursive-include src/bootstrap4/templates/bootstrap4 *.html
EOF

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python manage.py test -v2 --noinput

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE
%{python_sitelib}/bootstrap4
%{python_sitelib}/django_bootstrap4-%{version}*-info

%changelog
