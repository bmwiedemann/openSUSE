#
# spec file for package python-Pallets-Sphinx-Themes
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Pallets-Sphinx-Themes
Version:        2.0.3
Release:        0
Summary:        Themes for the Pallets projects.
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source:         https://files.pythonhosted.org/packages/source/P/Pallets-Sphinx-Themes/Pallets-Sphinx-Themes-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Sphinx
Requires:       python-packaging
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Themes for the Pallets projects. If you’re writing an extension, use
the appropriate theme to make your documentation look consistent.
Available themes: flask, jinja, werkzeug, click

%prep
%setup -q -n Pallets-Sphinx-Themes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst CHANGES.rst
%license LICENSE.rst
%{python_sitelib}/pallets_sphinx_themes/
%{python_sitelib}/Pallets_Sphinx_Themes-%{version}-py*.egg-info

%changelog
