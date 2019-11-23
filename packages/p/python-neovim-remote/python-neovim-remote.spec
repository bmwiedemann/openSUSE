#
# spec file for package python-neovim-remote
#
# Copyright (c) 2019 SUSE LLC
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
%define skip_python2 1
%define modname neovim-remote
Name:           python-neovim-remote
Version:        2.3.2
Release:        0
Summary:        Neovim process control utility
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mhinz/neovim-remote
Source0:        https://files.pythonhosted.org/packages/source/n/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module neovim}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
BuildArch:      noarch

%python_subpackages

%description
This package provides an executable called "nvr" which solves these cases:

- Controlling nvim processes from the shell, e.g. opening files in another
  terminal window.
- Opening files from within `:terminal` without starting a nested nvim process.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '1{\@^#!\s*%{_bindir}/env python@d}' nvr/nvr.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Plain python tests/test_nvr.py would work as well, but it makes no
# diagnostic output.
%python_expand PYTHONPATH=. py.test-%{$python_bin_suffix} -v tests

%files %{python_files}
%{_bindir}/nvr
%{python_sitelib}/*

%changelog
