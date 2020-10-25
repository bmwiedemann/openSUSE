#
# spec file for package python-fissix
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-fissix
Version:        20.8.0
Release:        0
Summary:        Backport of lib2to3, with enhancements
License:        Python-2.0
URL:            https://github.com/jreese/fissix
Source:         https://files.pythonhosted.org/packages/source/f/fissix/fissix-%{version}.tar.gz
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
BuildArch:      noarch
%python_subpackages

%description
Backport of latest lib2to3, with enhancements.

%prep
%setup -q -n fissix-%{version}
sed -i '1{/^#!/d}' fissix/pgen2/token.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/fissix/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
