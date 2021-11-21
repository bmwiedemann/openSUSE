#
# spec file for package python-mkdocs-bootstrap
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mkdocs-bootstrap
Version:        1.1
Release:        0
Summary:        Bootstrap theme for MkDocs
License:        BSD-2-Clause
URL:            https://mkdocs.github.io/mkdocs-bootstrap/
Source:         https://files.pythonhosted.org/packages/source/m/mkdocs-bootstrap/mkdocs-bootstrap-%{version}.tar.gz
BuildRequires:  %{python_module mkdocs >= 1.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mkdocs >= 1.1
BuildArch:      noarch
%python_subpackages

%description
Bootstrap theme for MkDocs

%prep
%setup -q -n mkdocs-bootstrap-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mkdocs_bootstrap*

%changelog
