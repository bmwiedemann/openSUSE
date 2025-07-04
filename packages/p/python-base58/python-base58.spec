#
# spec file for package python-base58
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-base58
Version:        2.1.1
Release:        0
Summary:        Base58 and Base58Check implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/keis/base58
Source:         https://files.pythonhosted.org/packages/source/b/base58/base58-%{version}.tar.gz
BuildRequires:  %{python_module PyHamcrest >= 2.0.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Base58 and Base58Check implementation compatible with what is used by the bitcoin network.

%prep
%setup -q -n base58-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/base58
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative base58

%files %{python_files}
%doc README.md
%license COPYING
%python_alternative %{_bindir}/base58
%{python_sitelib}/base58
%{python_sitelib}/base58-%{version}*-info

%changelog
