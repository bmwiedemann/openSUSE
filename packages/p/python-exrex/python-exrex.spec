#
# spec file for package python-exrex
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
Name:           python-exrex
Version:        0.10.5
Release:        0
Summary:        Irregular methods for regular expressions
License:        AGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/asciimoo/exrex
Source:         https://files.pythonhosted.org/packages/source/e/exrex/exrex-%{version}.tar.gz
# PATCH-FIX-UPSTREAM add-license.patch
Patch0:         https://github.com/asciimoo/exrex/pull/32.patch#/add-license.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Exrex is a command line tool and python module that generates all or random matching strings to a given regular expression and more.

%prep
%setup -q -n exrex-%{version}
sed -i '1s/^#!.*//' exrex.py
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/exrex
rm %{buildroot}%{_bindir}/exrex.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%post
%python_install_alternative exrex

%postun
%python_uninstall_alternative exrex

%files %{python_files}
%{python_sitelib}/*
%license COPYING
%python_alternative %{_bindir}/exrex

%changelog
