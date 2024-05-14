#
# spec file for package python-dfwinreg
#
# Copyright (c) 2024 SUSE LLC
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

%define timestamp 20240316
%define modname dfwinreg
Name:           python-dfwinreg
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Windows Registry
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/log2timeline/dfwinreg
Source:         https://github.com/log2timeline/%{modname}/releases/download/%{timestamp}/%{modname}-%{timestamp}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module dfdatetime}
BuildRequires:  %{python_module dtfabric}
BuildRequires:  %{python_module libcreg}
BuildRequires:  %{python_module libregf}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dfdatetime
Requires:       python-dtfabric
Requires:       python-libcreg >= 20210502
Requires:       python-libregf >= 20201002
BuildArch:      noarch
%python_subpackages

%description
%{modname}, or Digital Forensics Windows Registry, is a Python module that provides read-only access to Windows Registry objects.

%prep
%setup -q -n %{modname}-%{timestamp}
sed -i 's|/usr/bin/env python|/usr/bin/env python3|' run_tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# these are installed into the wrong place
rm -rf %{buildroot}%{_datadir}/doc/%{modname}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python ./run_tests.py
}

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%{python_sitelib}/%{modname}*

%changelog
