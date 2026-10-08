#
# spec file for package python-XStatic
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# PATCH-FIX-OPENSUSE Drop pkg_resources usage, can be dropped when 2.0.0 is released
Patch0:         no-more-pkg-resources.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
XStatic is a packaging standard to package external (often 3rd party)
static files as a Python package.

%prep
%autosetup -p1 -n XStatic-%{version}
# Also needs to be removed due to no-more-pkg-resources.patch
rm -r xstatic/pkg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/[Xx][Ss]tatic
%{python_sitelib}/[Xx][Ss]tatic-%{version}.dist-info

%changelog
