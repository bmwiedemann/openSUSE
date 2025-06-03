#
# spec file for package python-mulpyplexer
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


%define pkg_version 0.9
Name:           python-mulpyplexer
Version:        0.09
Release:        0
Summary:        A module that multiplexes interactions with lists of python objects
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/zardus/mulpyplexer
Source:         https://files.pythonhosted.org/packages/source/m/mulpyplexer/mulpyplexer-%{version}.tar.gz
Source1:        https://github.com/zardus/mulpyplexer/raw/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Mulpyplexer is a piece of code that can multiplex interactions with lists of python objects.

%prep
%setup -q -n mulpyplexer-%{version}
[ -e LICENSE ] || cp %{SOURCE1} LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/mulpyplexer.py
%{python_sitelib}/mulpyplexer-%{pkg_version}*-info
%pycache_only %{python_sitelib}/__pycache__/mulpyplexer*

%changelog
