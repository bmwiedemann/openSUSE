#
# spec file for package python-mobi
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
Name:           python-mobi
Version:        0.3.3
Release:        0
Summary:        Library for unpacking unencrypted mobi files
License:        GPL-3.0-only
URL:            https://github.com/iscc/mobi
Source:         https://files.pythonhosted.org/packages/source/m/mobi/mobi-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-loguru >= 0.4
BuildArch:      noarch
%python_subpackages

%description
Python library for unpacking unencrypted mobi files (forked from KindleUnpack)

%prep
%setup -q -n mobi-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mobiunpack
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test files are not installable

%post
%python_install_alternative mobiunpack

%postun
%python_uninstall_alternative mobiunpack

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mobiunpack
%{python_sitelib}/*

%changelog
