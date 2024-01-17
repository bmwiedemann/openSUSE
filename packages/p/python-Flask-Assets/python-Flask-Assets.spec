#
# spec file for package python-Flask-Assets
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without test
Name:           python-Flask-Assets
Version:        2.1.0
Release:        0
Summary:        Asset management for Flask, to compress and merge CSS and Javascript files
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/miracle2k/flask-assets
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Assets/Flask-Assets-%{version}.tar.gz
# PATCH-FIX-UPSTREAM denose.patch gh#miracle2k/flask-assets#169 mcepl@suse.com
# Clean up the remnants of nose tests.
Patch1:         denose.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module webassets}
BuildRequires:  fdupes
Requires:       python-Flask
Requires:       python-webassets
Recommends:     python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
Integrates the webassets library with Flask, adding support for
merging, minifying and compiling CSS and Javascript files.

%package -n %{name}-doc
Summary:        Documentation for Flask-Assets
Group:          Documentation/HTML
Provides:       %{python_module Flask-Assets-doc = %{version}}

%description -n %{name}-doc
This package contains documentation for the Flask-Assets module.

%prep
%setup -q -n Flask-Assets-%{version}
%autopatch -p1
# FIXME: theme not packaged by openSUSE
sed -i "s/html_theme = 'flask_small'//" docs/conf.py

%build
%python_build
cd docs
%make_build html
rm _build/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/flask_assets.py
%pycache_only %{python_sitelib}/__pycache__/flask_assets*.pyc
%{python_sitelib}/Flask_Assets-%{version}*-info

%files -n %{name}-doc
%doc CHANGES README.rst docs/_build/html

%changelog
