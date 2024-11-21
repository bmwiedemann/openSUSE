#
# spec file for package python-sphinx-autobuild
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
Name:           python-sphinx-autobuild
Version:        2024.10.3
Release:        0
Summary:        Rebuild Sphinx documentation on changes, with live-reload in the browser
License:        MIT
URL:            https://github.com/executablebooks/sphinx-autobuild
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-autobuild/sphinx_autobuild-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module watchfiles}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx
Requires:       python-colorama
Requires:       python-watchfiles
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%prep
%setup -q -n sphinx_autobuild-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sphinx-autobuild
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_application'

%post
%python_install_alternative sphinx-autobuild

%postun
%python_uninstall_alternative sphinx-autobuild

%files %{python_files}
%doc AUTHORS.rst NEWS.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/sphinx-autobuild
%{python_sitelib}/sphinx_autobuild
%{python_sitelib}/sphinx_autobuild-%{version}.dist-info

%changelog
