#
# spec file for package python-copr-cli
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-copr-cli
Version:        1.90
Release:        0
Summary:        Copr cli
License:        GPL-2.0+
URL:            https://pagure.io/copr/copr
Source:         https://files.pythonhosted.org/packages/source/c/copr-cli/copr-cli-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module copr}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-copr
Requires:       python-humanize
Requires:       python-Jinja2
Requires:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
CLI tool to run copr.

%prep
%setup -q -n copr-cli-%{version}
sed -i '1{/#!/d}' copr_cli/package_build_order.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/copr-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative copr-cli

%postun
%python_uninstall_alternative copr-cli

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/copr-cli
%{python_sitelib}/*

%changelog
