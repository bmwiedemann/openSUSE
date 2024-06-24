#
# spec file for package python-proselint
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


%define modname proselint
Name:           python-proselint
Version:        0.14.0
Release:        0
Summary:        A linter for prose
License:        BSD-3-Clause
URL:            https://github.com/amperser/proselint
Source:         https://github.com/amperser/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-dbm
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
proselint is a linter for English prose. (A linter is a computer
program that, like a spell checker, scans through a document and
analyzes it.)

Proselint is a command-line utility that can be integrated into
existing tools.

%prep
%autosetup -p1 -n proselint-%{version}

sed -i -e '/^#!\//, 1d' proselint/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/proselint
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%post
%python_install_alternative proselint

%postun
%python_uninstall_alternative proselint

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/proselint
%{python_sitelib}/proselint/
%{python_sitelib}/proselint-%{version}.dist-info

%changelog
