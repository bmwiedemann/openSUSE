#
# spec file for package python-docrepr
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-docrepr
Version:        0.1.1
Release:        0
Summary:        Python module to render docstrings as HTML
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/docrepr
Source:         https://github.com/spyder-ide/docrepr/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Sphinx
Requires:       python-docutils
BuildArch:      noarch
%python_subpackages

%description
The docrepr package renders Python docstrings as HTML. It is based on
the sphinxify module developed by Tim Dumol for the Sage Notebook and
the utils.inspector module developed for the Spyder IDE.

%prep
%setup -q -n docrepr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no upstream tests

%files %{python_files}
%doc README.md RELEASE.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/*

%changelog
