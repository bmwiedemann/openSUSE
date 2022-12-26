#
# spec file for package python-comm
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


%define skip_python2 1
Name:           python-comm
Version:        0.1.2
Release:        0
Summary:        Jupyter Python Comm implementation
License:        BSD-3-Clause
URL:            https://github.com/ipython/comm
Source:         https://github.com/ipython/comm/archive/refs/tags/%{version}.tar.gz#/comm-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module traitlets >= 5.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-traitlets >= 5.3
BuildArch:      noarch
%python_subpackages

%description
Comm provides a way to register a Kernel Comm implementation,
as per the Jupyter kernel protocol. It also provides a base
Comm implementation and a default CommManager that can be used.

%prep
%setup -q -n comm-%{version}
sed -i -e 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/comm
%{python_sitelib}/comm-%{version}*-info

%changelog
