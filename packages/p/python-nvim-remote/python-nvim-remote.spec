#
# spec file for package python-nvim-remote
#
# Copyright (c) 2024 SUSE LLC
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


%define modname nvim_remote
Name:           python-nvim-remote
Version:        4.2.0
Release:        0
Summary:        Neovim process control utility
License:        MIT
URL:            https://github.com/1995parham/nvim-remote
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module neovim}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-neovim
Requires:       python-psutil
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This package provides an executable called "nvr" which solves these cases:

- Controlling nvim processes from the shell, e.g. opening files in another
  terminal window.
- Opening files from within `:terminal` without starting a nested nvim process.

%prep
%autosetup -n nvim-remote-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nvr
%python_expand %fdupes %{buildroot}%{python_sitelib}

#fixes
%python_expand chmod +x %{buildroot}%{python_sitelib}/%{modname}/nvr.py
%python_expand sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|g' %{buildroot}%{python_sitelib}/%{modname}/nvr.py

%check
%pytest

%post
%python_install_alternative nvr

%postun
%python_uninstall_alternative nvr

%files %{python_files}
%python_alternative %{_bindir}/nvr
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-4.0.0.dist-info
%pycache_only %{python_sitelib}/%{modname}/__pycache__

%changelog
