#
# spec file for package python-django-template-partials
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-django-template-partials
Version:        25.3
Release:        0
Summary:        Reusable named inline-partials for the Django Template Language
License:        MIT
URL:            https://github.com/carltongibson/django-template-partials/
Source:         https://files.pythonhosted.org/packages/source/d/django-template-partials/django_template_partials-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
BuildRequires:  just
# /SECTION
Requires:       python-Django
Provides:       python-django_template_partials = %{version}
Obsoletes:      python-django_template_partials < %{version}
Suggests:       python-Sphinx
Suggests:       python-coverage
Suggests:       python-django_coverage_plugin
BuildArch:      noarch
%python_subpackages

%description
Reusable named inline partials for the Django Template Language.
Template Partials were added to Django in version 6.0. You should use that in new projects: 

%prep
%autosetup -p1 -n django_template_partials-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#CHOOSE: %%pytest OR %%pyunittest -v OR CUSTOM
#%%pytest

%files %{python_files}
%{python_sitelib}/template_partials
%{python_sitelib}/django_template_partials-%{version}.dist-info

%changelog
