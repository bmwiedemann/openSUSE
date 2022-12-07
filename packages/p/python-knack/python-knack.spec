#
# spec file for package python-knack
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-knack
Version:        0.10.1
Release:        0
Summary:        A Command-Line Interface framework
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/microsoft/knack
Source:         https://files.pythonhosted.org/packages/source/k/knack/knack-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module argcomplete}
BuildRequires:  %{python_module jmespath}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-argcomplete
Requires:       python-jmespath
Requires:       python-pygments
Requires:       python-tabulate
BuildArch:      noarch
%python_subpackages

%description
A Command-Line Interface framework

%prep
%setup -q -n knack-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
