#
# spec file for package python-pytimeparse2
#
# Copyright (c) 2023 SUSE LLC
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
%define short_name pytimeparse2
Name:           python-%{short_name}
Version:        1.7.1
Release:        0
Summary:        A small Python module to parse various kinds of time expressions
License:        MIT
URL:            https://github.com/onegreyonewhite/pytimeparse2 
Source:         %{short_name}-%{version}.tar.gz 
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module python-dateutil}
Requires:       python3-base
Recommends:     python3-python-dateutil
BuildArch:      noarch 
%python_subpackages

%description
A small Python module to parse various kinds of time expressions. Developed separately from the original.

%prep
%autosetup -n %{short_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand sed -i '1d' %{buildroot}/%{$python_sitelib}/%{short_name}.py

%check
%pyunittest -v

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/%{short_name}.py
%{python_sitelib}/%{short_name}-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog

