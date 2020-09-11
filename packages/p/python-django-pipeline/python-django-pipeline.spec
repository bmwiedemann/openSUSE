#
# spec file for package python-django-pipeline
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
%define skip_python2 1
Name:           python-django-pipeline
Version:        2.0.5
Release:        0
Summary:        An asset packaging library for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-pipeline
Source:         https://files.pythonhosted.org/packages/source/d/django-pipeline/django-pipeline-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module jsmin}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module slimit}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-Jinja2
BuildArch:      noarch
%python_subpackages

%description
Pipeline is an asset packaging library for Django, providing both CSS and
JavaScript concatenation and compression, built-in JavaScript template support,
and optional data-URI image and font embedding.

%prep
%setup -q -n django-pipeline-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we do not have python-css-html-js-minify, because it is nearly unpackageable (missing licenses, no tags on GitHub)
PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest -k "not test_csshtmljsminify"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
