#
# spec file for package python-pybars3
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


%define base_name pybars3

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{base_name}
Version:        0.9.7
Release:        0
Summary:        Handlebarsjs templating for Python 3 and 2
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/wbond/%{base_name}
Source:         https://github.com/wbond/%{base_name}/archive/%{version}.tar.gz
BuildRequires:  %{python_module PyMeta3 >= 0.5.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyMeta3 >= 0.5.1
BuildArch:      noarch

%python_subpackages

%description
Pybars3 provides a template system for Python which is compatible with
Handlebars.js.  It is a fork of the pybars project that adds Python 3
compatibility and numerous features from Handlebars.js 2.0.

%prep
%setup -q -n pybars3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec tests.py

%files %{python_files}
%license LICENSE
%doc readme.md changelog.md
%{python_sitelib}/*

%changelog
