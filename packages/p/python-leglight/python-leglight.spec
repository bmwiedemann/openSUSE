#
# spec file for package python-leglight
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


Name:           python-leglight
Version:        0.2.0
Release:        0
Summary:        A Python module designed to control the Elgato brand Lights
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.org/project/leglight/
Source:         https://files.pythonhosted.org/packages/source/l/leglight/leglight-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.22.0
Requires:       python-zeroconf >= 0.24.3
%python_subpackages

%description
A Python module designed to control the Elgato brand Lights. For use in
automation or in lieu of their Control Center app (when on a non-supported
platform).

%prep
%setup -q -n leglight-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.md
%{python_sitelib}/leglight
%{python_sitelib}/leglight-%{version}*-info

%changelog
