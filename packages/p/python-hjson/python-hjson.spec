#
# spec file for package python-hjson
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define mod_name hjson-py
%define upversion 3.1.0
Name:           python-hjson
Version:        3.1.0+git.1762077481.9351a27
Release:        0
Summary:        Hjson, a user interface for JSON
License:        MIT
URL:            http://github.com/hjson/hjson-py
# Source0:        https://files.pythonhosted.org/packages/source/h/hjson/hjson-%%{version}.tar.gz
Source0:        %{mod_name}-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Hjson, a user interface for JSON.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hjson
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v hjson/tests

%post
%python_install_alternative hjson

%postun
%python_uninstall_alternative hjson

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/hjson
%{python_sitelib}/hjson
%{python_sitelib}/hjson-%{upversion}.dist-info

%changelog
