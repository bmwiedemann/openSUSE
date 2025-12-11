#
# spec file for package python-msoffcrypto-tool
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


%{?sle15_python_module_pythons}
Name:           python-msoffcrypto-tool
Version:        5.4.2
Release:        0
Summary:        Library for decrypting MS Office files
License:        MIT
URL:            https://github.com/nolze/msoffcrypto-tool
Source:         https://github.com/nolze/msoffcrypto-tool/archive/v%{version}.tar.gz#/msoffcrypto_tool-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 39.0
Requires:       python-olefile >= 0.46
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 39.0}
BuildRequires:  %{python_module olefile >= 0.46}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python tool and library for decrypting MS Office
files with passwords or other keys.

%prep
%autosetup -p1 -n msoffcrypto-tool-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/msoffcrypto-tool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# pytest creates an illegitimate doctest case for __main__ which then fails
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
sed -i "s/python\([0-9]\.[0-9]*\)\?/python%{$python_bin_suffix}/" tests/test_cli.sh
$python -m pytest --doctest-modules -k 'not __main__'
}

%post
%python_install_alternative msoffcrypto-tool

%postun
%python_uninstall_alternative msoffcrypto-tool

%files %{python_files}
%doc README.md
%doc %{python_sitelib}/NOTICE.txt
%license LICENSE.txt
%python_alternative %{_bindir}/msoffcrypto-tool
%{python_sitelib}/msoffcrypto
%{python_sitelib}/msoffcrypto_tool-%{version}.dist-info

%changelog
