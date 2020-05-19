#
# spec file for package python-uniseg
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
Name:           python-uniseg
Version:        0.7.1
Release:        0
Summary:        Python module for determining Unicode text segmentations
License:        MIT
URL:            https://bitbucket.org/emptypage/uniseg-python
Source:         https://files.pythonhosted.org/packages/source/u/uniseg/uniseg-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A pure Python module to determine Unicode text segmentations.

%prep
%setup -q -n uniseg-%{version}
sed -i -e '/^#!\//, 1d' uniseg/*test.py uniseg/samples/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/uniseg-dbpath
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative uniseg-dbpath

%postun
%python_uninstall_alternative uniseg-dbpath

%files %{python_files}
%license LICENSE
%doc README
%python_alternative %{_bindir}/uniseg-dbpath
%{python_sitelib}/*

%changelog
