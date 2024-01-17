#
# spec file for package python-cl
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-cl
Version:        0.0.3
Release:        0
Summary:        Kombu actor framework
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ask/cl/
Source:         https://files.pythonhosted.org/packages/source/c/cl/cl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM port-2to3.patch bsc#[0-9]+ mcepl@suse.com
# Remove use_2to3 in setup.py
Patch0:         port-2to3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kombu
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Actor framework for Kombu

%prep
%autosetup -p1 -n cl-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cl
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative cl

%postun
%python_uninstall_alternative cl

%files %{python_files}
%license LICENSE
%doc AUTHORS README examples
%python_alternative %{_bindir}/cl
%{python_sitelib}/*

%changelog
