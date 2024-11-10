#
# spec file for package python-certipy
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-certipy
Version:        0.2.1
Release:        0
Summary:        Create and sign CAs and certificates
License:        BSD-3-Clause
URL:            https://github.com/LLNL/certipy
Source:         https://files.pythonhosted.org/packages/source/c/certipy/certipy-%{version}.tar.gz
# MANIFEST.in was merged; check next release
Source1:        https://raw.githubusercontent.com/LLNL/certipy/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Create and sign CAs and certificates.

%prep
%setup -q -n certipy-%{version}
cp %{SOURCE1} .
mv certipy/test .
sed -i 's/\.\.certipy/certipy/' test/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/certipy

%check
mkdir tmp
export TMP=$(pwd)/tmp
%pytest test/

%post
%python_install_alternative certipy

%postun
%python_uninstall_alternative certipy

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/certipy
%{python_sitelib}/certipy
%{python_sitelib}/certipy-%{version}.dist-info

%changelog
