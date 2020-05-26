#
# spec file for package python-hetzner
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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
Name:           python-hetzner
Version:        0.8.2
Release:        0
Summary:        High level access to the Hetzner robot
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aszlig/hetzner
Source:         https://github.com/aszlig/hetzner/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A high-level Python API for accessing the Hetzner robot.

%prep
%setup -q -n hetzner-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/hetznerctl
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative hetznerctl

%postun
%python_uninstall_alternative hetznerctl

%files %{python_files}
%doc README.md
%license COPYING
%python_alternative %{_bindir}/hetznerctl
%{python_sitelib}/*

%changelog
