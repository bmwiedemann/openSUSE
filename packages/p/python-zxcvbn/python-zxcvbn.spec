#
# spec file for package python-zxcvbn
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


%global modname zxcvbn
Name:           python-%{modname}
Version:        4.4.28
Release:        0
Summary:        Python password strength estimator
License:        MIT
URL:            https://github.com/dwolfhub/zxcvbn-python
Source:         https://github.com/dwolfhub/zxcvbn-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python password strength estimator.

%prep
%setup -q -n %{modname}-python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/zxcvbn

%post
%python_install_alternative zxcvbn

%postun
%python_uninstall_alternative zxcvbn

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*
%python_alternative %{_bindir}/zxcvbn

%changelog
