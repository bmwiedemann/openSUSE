#
# spec file for package python-htmlmin
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
Name:           python-htmlmin
Version:        0.1.12
Release:        0
Summary:        An HTML Minifier
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://htmlmin.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/h/htmlmin/htmlmin-%{version}.tar.gz
# https://github.com/mankyd/htmlmin/issues/51
Source1:        tests.tar.bz2
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A configurable HTML Minifier with safety features.

%prep
%setup -q -n htmlmin-%{version} -a1
# command.py is installed without exec permissions (and they're actually not needed) so
# we remove the shebang
sed -ie "s,#!%{_bindir}/env python,##!%{_bindir}/python3," htmlmin/command.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/htmlmin
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative htmlmin

%postun
%python_uninstall_alternative htmlmin

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/htmlmin
%{python_sitelib}/*

%changelog
