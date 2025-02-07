#
# spec file for package python-git-pw
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


%define modname git_pw
%{?sle15_python_module_pythons}
Name:           python-git-pw
Version:        2.7.1
Release:        0
Summary:        A tool for integrating Git with Patchwork
License:        MIT
URL:            https://github.com/getpatchwork/git-pw
Source:         https://files.pythonhosted.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module arrow >= 0.10}
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyaml >= 5.1}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module requests > 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate >= 0.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-arrow >= 0.10
Requires:       python-click >= 6.0
Requires:       python-pyaml >= 5.1
Requires:       python-requests > 2.0
Requires:       python-tabulate >= 0.8
Provides:       git-pw = %{version}
Obsoletes:      git-pw < %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
git-pw is a tool for integrating Git with Patchwork, the web-based patch
tracking system.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/git-pw
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
%pytest

%post
%python_install_alternative git-pw

%postun
%python_uninstall_alternative git-pw

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/git-pw
%{python_sitelib}/git_pw
%{python_sitelib}/git_pw-%{version}.dist-info

%changelog
