#
# spec file for package python-PyJWT
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-PyJWT
Version:        1.7.1
Release:        0
Summary:        JSON Web Token implementation in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/progrium/pyjwt
Source:         https://files.pythonhosted.org/packages/source/P/PyJWT/PyJWT-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/jpadilla/pyjwt/pull/448.patch
Patch0:         0001-Catch-BadSignatureError-raised-by-ecdsa-0.13.3.patch
BuildRequires:  %{python_module cryptography >= 1.4}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.4
Requires:       python-ecdsa
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of JSON Web Token draft 01.

%prep
%setup -q -n PyJWT-%{version}
%patch0 -p1

%build
%python_build
#remove shebang from all non executable files
find ./ -type f -name "*.py" -perm 644 -exec sed -i -e '1{\@^#!%{_bindir}/env python@d}' {} \;

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyjwt

%post
%python_install_alternative pyjwt

%postun
%python_uninstall_alternative pyjwt

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -o addopts="" -k "not test_verify_false_deprecated"

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGELOG.md README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/pyjwt

%changelog
