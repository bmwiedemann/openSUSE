#
# spec file for package git-pw
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           git-pw
Version:        1.5.1
Release:        0
Summary:        A tool for integrating Git with Patchwork
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/getpatchwork/%{name}
Source:         https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-arrow
Requires:       python-click
Requires:       python-requests
Requires:       python-tabulate
%python_subpackages

%description
git-pw is a tool for integrating Git with Patchwork, the web-based patch
tracking system.

%prep
%setup -q

%build
%python_build

%install
%python_install

%check
export LC_ALL=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/git-pw
%{python_sitelib}/git_pw
%{python_sitelib}/git_pw-%{version}-py%{py_ver}.egg-info

%changelog
