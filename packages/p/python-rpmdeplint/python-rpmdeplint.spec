#
# spec file for package python-rpmdeplint
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
Name:           python-rpmdeplint
Version:        1.4
Release:        0
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://pagure.io/rpmdeplint
Source:         https://files.pythonhosted.org/packages/source/r/rpmdeplint/rpmdeplint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hawkey
Requires:       python-rpm
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hawkey}
BuildRequires:  %{python_module librepo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rpmfluff}
BuildRequires:  %{python_module rpm}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Tool to find errors in RPM packages in the context of their dependency graph.

%prep
%setup -q -n rpmdeplint-%{version}
# Remove cmdclass entry
sed -i "/'build': build/d" setup.py
mv rpmdeplint/tests/ .
sed -i '/tests/d' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rpmdeplint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative rpmdeplint

%postun
%python_uninstall_alternative rpmdeplint

%check
%pytest tests/ -k 'not TestDependencyAnalyzer'

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/rpmdeplint
%{python_sitelib}/*

%changelog
