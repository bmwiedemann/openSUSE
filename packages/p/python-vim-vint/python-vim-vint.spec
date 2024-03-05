#
# spec file for package python-vim-vint
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


Name:           python-vim-vint
Version:        0.3.21
Release:        0
Summary:        Lint tool for Vim script Language
License:        MIT
URL:            https://github.com/Kuniwak/vint
Source:         https://github.com/Kuniwak/vint/archive/v%{version}.tar.gz
Patch0:         test-sys-executable.patch
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module ansicolor >= 0.2.4}
BuildRequires:  %{python_module chardet >= 2.3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 2.6.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.11
Requires:       python-ansicolor >= 0.2.4
Requires:       python-chardet >= 2.3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A lint tool for the Vim script Language.

%prep
%autosetup -p1 -n vint-%{version}
sed -e 's/==/>=/g' \
    -e 's/\~=/>=/g' \
    -i setup.py \
    -i test-requirements.txt \
    -i requirements.txt
sed -i -e '/^#!\//, 1d' vint/_bundles/vimlparser.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# this test fails with 3.9 when building, but succedes on changeroot
# when run manually when run by python3.9 -m unittest discover -v
rm ./test/acceptance/test_cli.py
%pyunittest discover -v

%post
%python_install_alternative vint

%postun
%python_uninstall_alternative vint

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/vint
%{python_sitelib}/vint
%{python_sitelib}/vim_vint-%{version}.dist-info

%changelog
