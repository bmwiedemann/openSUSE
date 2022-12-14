#
# spec file for package python-git-pw
#
# Copyright (c) 2022 SUSE LLC
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


%define modname git-pw
%define skip_python2 1
Name:           python-git-pw
Version:        2.4.0
Release:        0
Summary:        A tool for integrating Git with Patchwork
License:        MIT
URL:            https://github.com/getpatchwork/git-pw
Source:         https://files.pythonhosted.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module arrow >= 0.10}
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pyaml >= 5.1}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module requests > 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.12}
BuildRequires:  %{python_module tabulate >= 0.8}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-arrow >= 0.10
Requires:       python-click >= 6.0
Requires:       python-pyaml >= 5.1
Requires:       python-requests > 2.0
Requires:       python-six >= 1.12
Requires:       python-tabulate >= 0.8
Provides:       %{modname} = %{version}
Obsoletes:      %{modname} < %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
git-pw is a tool for integrating Git with Patchwork, the web-based patch
tracking system.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
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
%{python_sitelib}/git_pw-%{version}-py%{python_version}.egg-info

%changelog
