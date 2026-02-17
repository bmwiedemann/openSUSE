#
# spec file for package python-ansicolor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# For license file
%define tag     a5a5c31dc6de5c864a0c5684ae326972573a712b
Name:           python-ansicolor
Version:        0.3.3
Release:        0
Summary:        Python module for ANSI color output and colored highlighting and diffing
License:        Apache-2.0
URL:            https://github.com/numerodix/ansicolor
Source:         https://files.pythonhosted.org/packages/source/a/ansicolor/ansicolor-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/numerodix/ansicolor/%{tag}/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ansicolor
%{python_sitelib}/ansicolor-%{version}*-info

%changelog
