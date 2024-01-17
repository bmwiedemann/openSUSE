#
# spec file for package python-sphinx-theme-builder
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


Name:           python-sphinx-theme-builder
Version:        0.2.0b1
Release:        0
Summary:        A tool for authoring Sphinx themes with a simple (opinionated) workflow
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pradyunsg/sphinx-theme-builder
Source:         https://github.com/pradyunsg/sphinx-theme-builder/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-autobuild}
BuildRequires:  %{python_module tomli >= 1.0.0 if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-nodeenv
Requires:       python-packaging
Requires:       python-pyproject-metadata
Requires:       python-rich
Requires:       python-setuptools
Requires:       (python-tomli if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Streamline the Sphinx theme development workflow, by building upon
existing standardised tools.

 * simplified packaging experience
 * simplified JavaScript tooling setup
 * development server, with rebuild-on-save and automagical browser reloading
 * consistent repository structure across themes

%prep
%autosetup -p1 -n sphinx-theme-builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/stb
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative stb

%postun
%python_uninstall_alternative stb

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/stb
%{python_sitelib}/sphinx_theme_builder
%{python_sitelib}/sphinx_theme_builder-%{version}*-info

%changelog
