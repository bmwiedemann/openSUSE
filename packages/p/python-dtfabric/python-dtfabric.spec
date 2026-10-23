#
# spec file for package python-dtfabric
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
%define modname dtfabric
Name:           python-dtfabric
Version:        20260506
Release:        0
Summary:        Data type fabric (dtfabric)
License:        Apache-2.0
URL:            https://github.com/libyal/dtfabric
Source:         https://github.com/libyal/dtfabric/releases/download/%{version}/dtfabric-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
dtFabric, or data type fabric, is a project to manage data types and structures, as used in the libyal projects.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/validate_definitions
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative validate_definitions

%postun
%python_uninstall_alternative validate_definitions

%check
# Using pytest leads to some horribly-looking crashes, not sure what's
# going on.
%python_exec ./run_tests.py

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README.md
%python_alternative %{_bindir}/validate_definitions
%{python_sitelib}/dtfabric
%{python_sitelib}/dtfabric-%{version}.dist-info

%changelog
