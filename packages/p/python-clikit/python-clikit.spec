#
# spec file for package python-clikit
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
Name:           python-clikit
Version:        0.3.2
Release:        0
Summary:        Helper to build testable command line interfaces
License:        MIT
URL:            https://github.com/sdispater/clikit
Source:         https://github.com/sdispater/clikit/archive/%{version}.tar.gz#/clikit-%{version}.tar.gz
BuildRequires:  %{python_module pastel}
BuildRequires:  %{python_module pylev}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
BuildRequires:  python3-dephell
Requires:       python-pastel
Requires:       python-pylev
Requires:       python-typing
BuildArch:      noarch
%ifpython2
Requires:       python2-enum34
%endif
%python_subpackages

%description
CliKit is a group of utilities to build beautiful and testable
command line interfaces.

%prep
%setup -q -n clikit-%{version}
dephell deps convert --from pyproject.toml --to setup.py
mv src/clikit .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
