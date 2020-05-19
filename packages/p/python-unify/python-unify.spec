#
# spec file for package python-unify
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
Name:           python-unify
Version:        0.5
Release:        0
Summary:        Tool to modify strings to use the same quotes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/myint/unify
Source:         https://github.com/myint/unify/archive/v%{version}.tar.gz
Source9:        README.suse
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-untokenize
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module untokenize}
# /SECTION
%python_subpackages

%description
Modifies strings to all use the same (single/double) quote where possible.

Note that the "unify" executable has been renamed to "unify_quotes" to
avoid conflicts with the wdiff package.

%prep
%setup -q -n unify-%{version}
sed -i -e '/^#!\//, 1d' unify.py
cp %{SOURCE9} .

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/unify %{buildroot}%{_bindir}/unify_quotes
%python_clone -a %{buildroot}%{_bindir}/unify_quotes

%post
%python_install_alternative unify_quotes

%postun
%python_uninstall_alternative unify_quotes

%files %{python_files}
%license LICENSE
%doc README.rst README.suse
%python_alternative %{_bindir}/unify_quotes
%{python_sitelib}/*

%changelog
