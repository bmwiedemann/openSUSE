#
# spec file for package python-sphinx-notfound-page
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
Name:           python-sphinx-notfound-page
Version:        1.0.4
Release:        0
Summary:        Sphinx extension to build a 404 page with absolute URLs
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-notfound-page/sphinx_notfound_page-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 5}
# /SECTION
%python_subpackages

%description
Create a custom 404 page with absolute URLs hardcoded.

Check out the full documentation at https://sphinx-notfound-page.readthedocs.io/

%prep
%autosetup -p1 -n sphinx_notfound_page-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/notfound
%{python_sitelib}/sphinx_notfound_page-%{version}.dist-info

%changelog
