#
# spec file for package python-framework16_inputmodule
#
# Copyright (c) 2024 Nico Krapp
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


%define stable_version 0.1.1
%define reponame inputmodule-rs
%{?sle15_python_module_python}
Name:           python-framework16_inputmodule
Version:        20241125.d9f18af
Release:        0
Summary:        A library to control input modules on the Framework 16 Laptop
License:        MIT
URL:            https://github.com/FrameworkComputer/inputmodule-rs
Source:         %{reponame}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyserial}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       framework-inputmodule-control
Requires:       python-Pillow
Requires:       python-base >= 3.7
Requires:       python-getkey
Requires:       python-pyserial
Requires:       python-pygame
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A library to control input modules on the Framework 16 Laptop

%prep
%autosetup -p1 -n %{reponame}-%{version}
cd python/
sed -E -i "1{s|^#\!\s*/usr/bin/env python3$|#\!%{_bindir}/python3|}" inputmodule/cli.py
sed -E -i "1{s|^#\!\s*/usr/bin/env python3$|#\!%{_bindir}/python3|}" inputmodule/uf2conv.py

%build
cd python/
%pyproject_wheel

%install
cd python/
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ledmatrixctl
%python_clone -a %{buildroot}%{_bindir}/ledmatrixgui
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ledmatrixctl ledmatrixgui

%postun
%python_uninstall_alternative ledmatrixctl ledmatrixgui

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/inputmodule
%attr(755, -, -) %{python_sitelib}/inputmodule/uf2conv.py
%{python_sitelib}/inputmodule-%{stable_version}.dist-info
%python_alternative %{_bindir}/ledmatrixctl
%python_alternative %{_bindir}/ledmatrixgui

%changelog
