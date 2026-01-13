#
# spec file for package python-nmcli
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


%{?sle15_python_module_pythons}
Name:           python-nmcli
Version:        1.7.0
Release:        0
Summary:        A python wrapper library for the network-manager cli client
License:        MIT
URL:            https://github.com/ushiboy/nmcli
Source:         https://github.com/ushiboy/nmcli/archive/refs/tags/v%{version}.tar.gz#/nmcli-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

Requires:       NetworkManager
%python_subpackages

%description

nmcli is a python wrapper library for the network-manager cli client.

%prep
%autosetup -p1 -n nmcli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/nmcli
%{python_sitelib}/nmcli-%{version}.dist-info

%changelog
