#
# spec file for package python-ddgs
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-ddgs
Version:        9.14.4
Release:        0
Summary:        Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services
License:        MIT
URL:            https://github.com/deedy5/ddgs
Source:         https://files.pythonhosted.org/packages/source/d/ddgs/ddgs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.1.8}
BuildRequires:  %{python_module lxml >= 4.9.4}
BuildRequires:  %{python_module primp}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.1.8
Requires:       python-lxml >= 4.9.4
Requires:       python-primp
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services.

%prep
%autosetup -p1 -n ddgs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ddgs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative ddgs

%post
%python_install_alternative ddgs

%postun
%python_uninstall_alternative ddgs

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/ddgs
%{python_sitelib}/ddgs
%{python_sitelib}/ddgs-%{version}.dist-info

%changelog
