#
# spec file for package python-dfwinreg
#
# Copyright (c) 2020 SUSE LLC
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
%define timestamp 20190714
%define modname dfwinreg
Name:           python-dfwinreg
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Windows Registry
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/log2timeline/dfwinreg
Source:         https://github.com/log2timeline/%{modname}/releases/download/%{timestamp}/%{modname}-%{timestamp}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
%{modname}, or Digital Forensics Windows Registry, is a Python module that provides read-only access to Windows Registry objects.

%prep
%setup -q -n %{modname}-%{timestamp}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# these are installed into the wrong place
rm -rf %{buildroot}%{_datadir}/doc/%{modname}

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%{python_sitelib}/%{modname}*

%changelog
