#
# spec file for package python-omemo-dr
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


%define _name   omemo-dr
%{?sle15_python_module_pythons}
Name:           python-omemo-dr
Version:        1.2.0
Release:        0
Summary:        OMEMO Encryption Library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://dev.gajim.org/gajim/omemo-dr
Source:         %{url}/-/archive/v%{version}/%{_name}-v%{version}.tar.bz2
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
# For testing
BuildRequires:  %{python_module protobuf >= 4.21.0}
BuildRequires:  %{python_module setuptools >= 65.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators >= 20220912
BuildRequires:  python-rpm-macros >= 20220912
Requires:       python-cryptography
Requires:       python-protobuf >= 4.21.0
%{?python_enable_dependency_generator}

%python_subpackages

%description
Python library for handling OMEMO encryption.

%prep
%autosetup -n %{_name}-v%{version} -p1

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%check
%pyunittest_arch discover -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/omemo_dr/
%{python_sitearch}/omemo_dr-*

%changelog
