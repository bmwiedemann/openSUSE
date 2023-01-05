#
# spec file for package python-dtfabric
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname dtfabric
%define skip_python2 1
Name:           python-dtfabric
Version:        20221218
Release:        0
Summary:        Data type fabric (dtfabric)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/libyal/dtfabric
Source:         https://github.com/libyal/dtfabric/releases/download/%{version}/dtfabric-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
dtFabric, or data type fabric, is a project to manage data types and structures, as used in the libyal projects.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/validate-definitions.py
# setup.py install helpfully installs files where it shouldn’t
rm -rv %{buildroot}%{_datadir}/doc/%{modname}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative validate-definitions.py

%postun
%python_uninstall_alternative validate-definitions.py

%check
# Using pytest leads to some horribly-looking crashes, not sure what's
# going on.
%python_exec ./run_tests.py

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%python_alternative %{_bindir}/validate-definitions.py
%{python_sitelib}/*

%changelog
