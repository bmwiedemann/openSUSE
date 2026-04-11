#
# spec file for package python-Pallets-Sphinx-Themes
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
Name:           python-Pallets-Sphinx-Themes
Version:        2.5.0
Release:        0
Summary:        Themes for the Pallets projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source:         https://files.pythonhosted.org/packages/source/P/Pallets-Sphinx-Themes/pallets_sphinx_themes-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 7.3}
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module sphinx-notfound-page}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 7.3
Requires:       python-packaging
Requires:       python-sphinx-notfound-page
BuildArch:      noarch
%python_subpackages

%description
Themes for the Pallets projects. If you’re writing an extension, use
the appropriate theme to make your documentation look consistent.
Available themes: flask, jinja, werkzeug, click

%prep
%setup -q -n pallets_sphinx_themes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.md CHANGES.md
%{python_sitelib}/pallets_sphinx_themes/
%{python_sitelib}/pallets_sphinx_themes-%{version}.dist-info

%changelog
