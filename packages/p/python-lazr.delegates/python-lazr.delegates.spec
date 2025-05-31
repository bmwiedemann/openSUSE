#
# spec file for package python-lazr.delegates
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


%{?sle15_python_module_pythons}
Name:           python-lazr.delegates
Version:        2.1.0
Release:        0
Summary:        Easily write objects that delegate behavior
License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.delegates
Source:         https://files.pythonhosted.org/packages/source/l/lazr.delegates/lazr.delegates-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
Easily write objects that delegate behavior

%prep
%setup -q -n lazr.delegates-%{version}

%build
sed -i "/'nose'/d" setup.py
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%dir %{python_sitelib}/lazr
%{python_sitelib}/lazr/delegates
%{python_sitelib}/lazr[._]delegates-%{version}*-info
%{python_sitelib}/lazr[._]delegates-%{version}*nspkg.pth

%changelog
