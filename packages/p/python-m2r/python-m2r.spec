#
# spec file for package python-m2r
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
%bcond_without test
%global modname m2r
Name:           python-m2r
Version:        0.2.1
Release:        0
Summary:        Markdown to reStructuredText converter
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/miyakogi/%{modname}
Source:         https://files.pythonhosted.org/packages/source/m/m2r/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module mistune}
BuildRequires:  %{python_module setuptools}
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils
Requires:       python-mistune
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
M2R converts a markdown file including reST markups to a valid reST format.

%prep
%setup -q -n %{modname}-%{version}
sed -i '/^#!.*/d' m2r.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/m2r
%python_expand %fdupes %{buildroot}%{$python_sitelib}/
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/

%post
%python_install_alternative m2r

%postun
%python_uninstall_alternative m2r

%check
%if %{with test}
%pytest
%endif

%files %{python_files}
%license LICENSE
%doc README.md CHANGES.md
%python_alternative %{_bindir}/m2r
%{python_sitelib}/%{modname}*
%pycache_only %{python_sitelib}/__pycache__

%changelog
