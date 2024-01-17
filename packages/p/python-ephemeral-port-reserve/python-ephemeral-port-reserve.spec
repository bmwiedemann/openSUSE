#
# spec file for package python-ephemeral-port-reserve
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname ephemeral-port-reserve
%{?sle15_python_module_pythons}
Name:           python-ephemeral-port-reserve
Version:        1.1.4
Release:        0
Summary:        Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it
License:        MIT
URL:            https://github.com/Yelp/ephemeral-port-reserve/
# GH URL is necessary because of missing tests, gh#Yelp/ephemeral-port-reserve#16
Source:         https://github.com/Yelp/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -i -e '1{/env python/d}' ephemeral_port_reserve.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ephemeral-port-reserve
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative ephemeral-port-reserve

%postun
%python_uninstall_alternative ephemeral-port-reserve

%files %{python_files}
%python_alternative %{_bindir}/ephemeral-port-reserve

%{python_sitelib}/__pycache__
%{python_sitelib}/ephemeral_port_reserve-%{version}*-info
%{python_sitelib}/ephemeral_port_reserve.py

%changelog
