#
# spec file for package python-pontos
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-pontos
Version:        0.2.0
Release:        0
Summary:        Common utilities and tools maintained by Greenbone Networks
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/greenbone/pontos
Source:         https://files.pythonhosted.org/packages/source/p/pontos/pontos-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-dephell-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The pontos Python package is a collection of utilities, tools, classes
and functions maintained by Greenbone Networks.
Pontos is the German name of the Greek titan Pontus, the titan of the
sea.

%prep
%setup -q -n pontos-%{version}
%dephell_gensetup

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pontos*

%changelog
