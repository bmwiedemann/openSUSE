#
# spec file for package python-ufonormalizer
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-ufonormalizer
Version:        0.6.2
Release:        0
Summary:        Script to normalize the XML and other data inside of a UFO
License:        BSD-3-Clause
URL:            https://github.com/unified-font-object/ufoNormalizer
Source:         https://files.pythonhosted.org/packages/source/u/ufonormalizer/ufonormalizer-%{version}.zip
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Script to normalize the XML and other data inside of a UFO.

%prep
%autosetup -p1 -n ufonormalizer-%{version}
sed -i -e '1{\,^#! %{_bindir}/env python,d}' src/ufonormalizer/__init__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ufonormalizer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%post
%python_install_alternative ufonormalizer

%postun
%python_uninstall_alternative ufonormalizer

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/ufonormalizer
%{python_sitelib}/ufonormalizer
%{python_sitelib}/ufonormalizer-%{version}*-info

%changelog
