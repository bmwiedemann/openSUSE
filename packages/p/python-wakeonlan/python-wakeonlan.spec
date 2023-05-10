#
# spec file for package python-wakeonlan
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-wakeonlan
Version:        3.0.0
Release:        0
Summary:        A small python module for wake on lan
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/remcohaszing/pywakeonlan
Source:         https://github.com/remcohaszing/pywakeonlan/archive/refs/tags/%{version}.tar.gz#/wakeonlan-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A small python module for wake on lan.

%prep
%setup -q -n pywakeonlan-%{version}
sed -i '1{/env python/d}' wakeonlan/__init__.py
chmod -x wakeonlan/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wakeonlan
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative wakeonlan

%postun
%python_uninstall_alternative wakeonlan

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/wakeonlan
%{python_sitelib}/wakeonlan
%{python_sitelib}/wakeonlan-%{version}.dist-info

%changelog
