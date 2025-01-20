#
# spec file for package python-sphinxygen
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


Name:           python-sphinxygen
Version:        1.0.10
Release:        0
Summary:        A script to generate Sphinx ReST from Doxygen XML
License:        ISC
URL:            https://gitlab.com/drobilla/sphinxygen
Source:         https://files.pythonhosted.org/packages/source/s/sphinxygen/sphinxygen-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires(post): update-alternatives
Suggests:       python-html5lib
BuildArch:      noarch
%python_subpackages

%description
Sphinxygen is a Python module/script that generates Sphinx markup to describe a C API, from an XML description extracted by Doxygen.

%prep
%autosetup -p1 -n sphinxygen-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sphinxygen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
 
%post
%python_install_alternative sphinxygen

%postun
%python_uninstall_alternative sphinxygen

%files %{python_files}
%doc NEWS README.md
%license LICENSE LICENSES LICENSES/0BSD.txt LICENSES/ISC.txt
%python_alternative %{_bindir}/sphinxygen
%{python_sitelib}/sphinxygen
%{python_sitelib}/sphinxygen-%{version}.dist-info

%changelog
