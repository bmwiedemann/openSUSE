#
# spec file for package python-dephell-shells
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
%define skip_python2 1
Name:           python-dephell-shells
Version:        0.1.3
Release:        0
Summary:        Dephell plugin to activate virtual environment for the current shell
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dephell/dephell_shells
Source:         https://files.pythonhosted.org/packages/source/d/dephell_shells/dephell_shells-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-pexpect
Requires:       python-shellingham
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module shellingham}
# /SECTION
%python_subpackages

%description
Dephell plugin to activate virtual environment for the current shell.

%prep
%setup -q -n dephell_shells-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# name and path expect the default shell to be bash
%pytest -k 'not test_name and not test_path'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
