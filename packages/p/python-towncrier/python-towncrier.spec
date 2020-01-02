#
# spec file for package python-towncrier
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-towncrier
Version:        19.2.0
Release:        0
License:        MIT
Summary:        Building newsfiles for your project
Url:            https://github.com/hawkowl/towncrier
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/t/towncrier/towncrier-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module incremental}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module incremental}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module Twisted}
BuildRequires:  git-core
# /SECTION
BuildRequires:  fdupes
Requires:       git-core
Requires:       python-click
Requires:       python-incremental
Requires:       python-Jinja2
Requires:       python-toml
BuildArch:      noarch

%python_subpackages

%description
Building newsfiles for your project.

%prep
%setup -q -n towncrier-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%python3_only %{_bindir}/towncrier
%{python_sitelib}/*

%changelog
