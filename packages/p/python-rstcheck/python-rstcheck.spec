#
# spec file for package python-rstcheck
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


Name:           python-rstcheck
Version:        6.2.1
Release:        0
Summary:        Python module to check syntax of reStructuredText
License:        MIT
URL:            https://github.com/myint/rstcheck
Source:         https://files.pythonhosted.org/packages/source/r/rstcheck/rstcheck-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rstcheck-core >= 1.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module typer >= 0.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  bash
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-rstcheck-core >= 1.2
Requires:       python-typer >= 0.4.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     bash
Recommends:     gcc
Recommends:     gcc-c++
Recommends:     python-Sphinx
Provides:       rstcheck = %{version}
Obsoletes:      rstcheck < %{version}
BuildArch:      noarch
%python_subpackages

%description
A Python module to check the syntax of reStructuredText and code
blocks nested within it.

%prep
%autosetup -p1 -n rstcheck-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rstcheck
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative rstcheck

%postun
%python_uninstall_alternative rstcheck

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%python_alternative %{_bindir}/rstcheck
%{python_sitelib}/rstcheck
%{python_sitelib}/rstcheck-%{version}.dist-info

%changelog
