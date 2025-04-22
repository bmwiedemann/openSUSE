#
# spec file for package python-django-pipeline
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


Name:           python-django-pipeline
Version:        4.0.0
Release:        0
Summary:        An asset packaging library for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-pipeline
Source:         https://files.pythonhosted.org/packages/source/d/django-pipeline/django_pipeline-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/jazzband/django-pipeline/pull/835 834 compatibility django52
Patch:          django52.patch
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module css-html-js-minify}
BuildRequires:  %{python_module jsmin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module slimit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Recommends:     python-Jinja2
BuildArch:      noarch
%python_subpackages

%package -n python-django-pipeline-doc
Summary:        Man files for python-django-pipeline
Group:          Documentation/Other
Requires:       python3-django-pipeline = %{version}

%description -n python-django-pipeline-doc
Documentation files for python-django-pipeline

%description
Pipeline is an asset packaging library for Django, providing both CSS and
JavaScript concatenation and compression, built-in JavaScript template support,
and optional data-URI image and font embedding.

%prep
%autosetup -p1 -n django_pipeline-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# fix installation errors
mkdir -p %{buildroot}%{_docdir}/python-django-pipeline/
mv %{buildroot}%{python3_sitelib}/docs/* %{buildroot}%{_docdir}/python-django-pipeline/
rm -r %{buildroot}%{_docdir}/python-django-pipeline/__pycache__
mv %{buildroot}%{python3_sitelib}/img %{buildroot}%{_docdir}/python-django-pipeline/
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests %{buildroot}%{$python_sitelib}/docs %{buildroot}%{$python_sitelib}/img

%check
# test_*_packages_with_pipeline_disabled - no media files in PyPI tarball
PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest -k "not packages_with_pipeline_disabled"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pipeline/
%{python_sitelib}/*django_pipeline*/

%files -n python-django-pipeline-doc
%{_docdir}/python-django-pipeline/

%changelog
