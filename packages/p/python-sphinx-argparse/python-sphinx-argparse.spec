#
# spec file for package python-sphinx-argparse
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
%define skip_python2 1
Name:           python-sphinx-argparse
Version:        0.2.5
Release:        0
Summary:        Sphinx extension to document argparse commands and options
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ribozz/sphinx-argparse
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx-argparse-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/alex-rudakov/sphinx-argparse/%{version}/LICENSE#/LICENSE-sphinx-argparse
# PATCH-FIX-UPSTREAM prog-in-description.patch gh#alex-rudakov/sphinx-argparse#113 mcepl@suse.com
# Substitute %(prog)s in description and epilog
Patch0:         prog-in-description.patch
BuildRequires:  %{python_module CommonMark}
BuildRequires:  %{python_module Sphinx >= 1.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension that automatically documents argparse commands and options.

%prep
%setup -q -n sphinx-argparse-%{version}
%autopatch -p1

install -m0644 %{SOURCE1} LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# can't use %%pytest until gh#alex-rudakov/sphinx-argparse#121 is solved
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTEST_NAME="py.test-%{$python_bin_suffix}"
$PYTEST_NAME --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -vv
}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
