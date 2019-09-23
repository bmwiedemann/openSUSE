#
# spec file for package python-ansicolor
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-ansicolor
Version:        0.2.6
Release:        0
# For license file
%define tag     a5a5c31dc6de5c864a0c5684ae326972573a712b
Summary:        Python module for ANSI color output and colored highlighting and diffing
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/numerodix/ansicolor
Source:         https://files.pythonhosted.org/packages/source/a/ansicolor/ansicolor-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/numerodix/ansicolor/%{tag}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Ansicolor is a library that offers ANSI color markup for
command line programs.

%prep
%setup -q -n ansicolor-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
