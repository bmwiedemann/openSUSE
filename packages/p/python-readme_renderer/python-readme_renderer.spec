#
# spec file for package python-readme_renderer
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


%{?sle15_python_module_pythons}
Name:           python-readme_renderer
Version:        44.0
Release:        0
Summary:        A library for rendering "readme" descriptions
License:        Apache-2.0
URL:            https://github.com/pypa/readme_renderer
Source:         https://files.pythonhosted.org/packages/source/r/readme_renderer/readme_renderer-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pypa/readme_renderer/pull/325 fix: update test outputs to fix tests fail
Patch:          pygments.patch
BuildRequires:  %{python_module Pygments >= 2.5.1}
BuildRequires:  %{python_module cmarkgfm >= 0.7.0}
BuildRequires:  %{python_module docutils >= 0.13.1}
BuildRequires:  %{python_module nh3 >= 0.2.14}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 2.5.1
Requires:       python-docutils >= 0.13.1
Requires:       python-nh3 >= 0.2.14
Recommends:     python-cmarkgfm >= 0.7.0
BuildArch:      noarch
%python_subpackages

%description
Readme Renderer is a library that will safely render arbitrary ``README`` files
into HTML. It is designed to be used in Warehouse to render the
long_description for packages.

%prep
%autosetup -p1 -n readme_renderer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/readme_renderer
%{python_sitelib}/readme_renderer-%{version}.dist-info

%changelog
