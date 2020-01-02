#
# spec file for package python-dephell-argparse
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
Name:           python-dephell-argparse
Version:        0.1.2
Release:        0
Summary:        Argparse with groups, commands, colors
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/dephell/dephell_argparse
Source:         https://files.pythonhosted.org/packages/source/d/dephell-argparse/dephell_argparse-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing
BuildArch:      noarch

%python_subpackages

%description
Argparse on with groups, commands, colors.

%prep
%setup -q -n dephell_argparse-%{version}

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
