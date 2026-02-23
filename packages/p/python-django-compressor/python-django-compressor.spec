#
# spec file for package python-django-compressor
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define mod_name django_compressor
%define git_tarball_name django-compressor
%define git_tarball_internal_version 4.6
Name:           python-django-compressor
Version:        4.6.0
Release:        0
Summary:        Python module to compress linked/inline JavaScript/CSS to cached files
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://github.com/django-compressor/django-compressor
Source:         https://github.com/django-compressor/django-compressor/archive/refs/tags/%{git_tarball_internal_version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module Brotli >= 1.0.6}
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module calmjs.parse}
BuildRequires:  %{python_module csscompressor}
BuildRequires:  %{python_module django-appconf >= 1.0.3}
BuildRequires:  %{python_module django-sekizai >= 2.0.0}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module lxml >= 4.9.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module rcssmin >= 1.2.1}
BuildRequires:  %{python_module rjsmin >= 1.2.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-beautifulsoup4
Requires:       python-csscompressor
Requires:       python-django-appconf >= 1.0.3
Requires:       python-rcssmin >= 1.2.1
Requires:       python-rjsmin >= 1.2.4
Recommends:     python-Brotli >= 1.0.6
Recommends:     python-Jinja2
Recommends:     python-calmjs
Suggests:       python-django-sekizai >= 2.0.0
Provides:       python-django_compressor = %{version}
Obsoletes:      python-django_compressor < %{version}
BuildArch:      noarch
%python_subpackages

%description
Django Compressor combines and compresses linked and inline Javascript or CSS
in a Django templates into cacheable static files by using the "compress"
template tag.

%prep
%setup -q -n %{git_tarball_name}-%{git_tarball_internal_version}
# No patches available atm
# %%autopatch -p1
sed -i '1{/env python/d}' compressor/tests/precompiler.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_expand $python -m django test --settings=compressor.test_settings compressor --pythonpath=`pwd` -v2

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/compressor
%{python_sitelib}/django_compressor-%{version}*-info

%changelog
