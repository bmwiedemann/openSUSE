#
# spec file for package python-py-vapid
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
Name:           python-py-vapid
Version:        1.7.0
Release:        0
Summary:        VAPID header generation library
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla-services/vapid
Source:         https://files.pythonhosted.org/packages/source/p/py-vapid/py-vapid-%{version}.tar.gz
Patch0:         skip-test_sign_01.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
VAPID header generation library.

%prep
%setup -q -n py-vapid-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vapid
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%post
%python_install_alternative vapid

%postun
%python_uninstall_alternative vapid

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%python_alternative %{_bindir}/vapid
%{python_sitelib}/*

%changelog
