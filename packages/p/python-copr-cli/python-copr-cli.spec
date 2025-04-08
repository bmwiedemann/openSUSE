#
# spec file for package python-copr-cli
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


Name:           python-copr-cli
Version:        2.1
Release:        0
Summary:        Copr cli
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/copr
Source:         https://files.pythonhosted.org/packages/source/c/copr-cli/copr-cli-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-copr >= 1.116
Requires:       python-humanize
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module copr >= 1.116}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
CLI tool to run copr.

%prep
%autosetup -p1 -n copr-cli-%{version}

sed -i '1{/#!/d}' copr_cli/package_build_order.py

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/copr_cli
%{python_sitelib}/copr_cli-%{version}.dist-info

%changelog
