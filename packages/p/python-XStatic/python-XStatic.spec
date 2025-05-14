#
# spec file for package python-XStatic
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


Name:           python-XStatic
Version:        1.0.3
Release:        0
Summary:        XStatic base package with minimal support code
License:        MIT
URL:            https://github.com/xstatic-py/xstatic
Source:         https://files.pythonhosted.org/packages/source/X/XStatic/XStatic-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
XStatic is a packaging standard to package external (often 3rd party)
static files as a Python package.

%prep
%setup -q -n XStatic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/[Xx][Ss]tatic
%{python_sitelib}/[Xx][Ss]tatic-%{version}*-info
%{python_sitelib}/[Xx][Ss]tatic-%{version}*nspkg.pth

%changelog
