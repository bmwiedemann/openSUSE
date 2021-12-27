#
# spec file for package python-fissix
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-fissix
Version:        21.11.13
Release:        0
Summary:        Backport of lib2to3, with enhancements
License:        Python-2.0
URL:            https://github.com/jreese/fissix
Source:         https://files.pythonhosted.org/packages/source/f/fissix/fissix-%{version}.tar.gz
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0.1}
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
sed -i '1{/^#!/d}' fissix/pgen2/token.py fissix/tests/pytree_idempotency.py
chmod -x fissix/pgen2/token.py fissix/tests/pytree_idempotency.py
# remove tests with python2 syntax, because they fail to compile during pyproject_install
mv fissix/tests/data testdata

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv testdata fissix/tests/data
# ensure that pickled cache files don't interfere between flavors
%python_expand mkdir build/cache
export XDG_CACHE_HOME=$PWD/build/cache
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fissix
%{python_sitelib}/fissix-%{version}*-info

%changelog
