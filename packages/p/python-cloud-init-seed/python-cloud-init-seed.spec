#
# spec file for package python-cloud-init-seed
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define skip_python2 1
Name:           python-cloud-init-seed
Version:        0.3.0
Release:        0
Summary:        Create cloud-init compatible image seeds
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/toabctl/cloud-init-seed
Source:         https://files.pythonhosted.org/packages/source/c/cloud-init-seed/cloud-init-seed-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       mkisofs
BuildArch:      noarch

%python_subpackages

%description
Create cloud-init compatible image seeds

%prep
%setup -q -n cloud-init-seed-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python3_only %{_bindir}/cloud-init-seed
%{python_sitelib}/*

%changelog
