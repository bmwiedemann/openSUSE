#
# spec file for package python-user_agent
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-user_agent
Version:        0.1.9
Release:        0
Summary:        User-Agent generator for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lorien/user_agent
Source:         https://files.pythonhosted.org/packages/source/u/user_agent/user_agent-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This module generates random, valid web user agents.

%prep
%setup -q -n user_agent-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ua
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative ua

%postun
%python_uninstall_alternative ua

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/ua
%{python_sitelib}/*

%changelog
