#
# spec file for package python-certipy
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
%define skip_python2 1
Name:           python-certipy
Version:        0.1.3
Release:        0
Summary:        Create and sign CAs and certificates
License:        BSD-3-Clause
URL:            https://github.com/LLNL/certipy
Source:         https://files.pythonhosted.org/packages/source/c/certipy/certipy-%{version}.tar.gz
# MANIFEST.in was merged; check next release
Source1:        https://raw.githubusercontent.com/LLNL/certipy/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Create and sign CAs and certificates.

%prep
%setup -q -n certipy-%{version}
cp %{SOURCE1} .
mv certipy/test .
sed -i 's/\.\.certipy/certipy/' test/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir tmp
export TMP=$(pwd)/tmp
%pytest test/

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/certipy
%{python_sitelib}/*

%changelog
