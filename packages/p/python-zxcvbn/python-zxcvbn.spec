#
# spec file for package python-zxcvbn
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        4.5.0
Release:        0
Summary:        Python password strength estimator
License:        MIT
URL:            https://github.com/dwolfhub/zxcvbn-python
Source:         https://github.com/dwolfhub/zxcvbn-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python password strength estimator.

%prep
%setup -q -n %{modname}-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info
%python_alternative %{_bindir}/zxcvbn

%changelog
