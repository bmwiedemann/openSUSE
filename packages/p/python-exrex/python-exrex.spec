#
# spec file for package python-exrex
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-exrex
Version:        0.11.0
Release:        0
Summary:        Irregular methods for regular expressions
License:        AGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/asciimoo/exrex
#Source:         https://files.pythonhosted.org/packages/source/e/exrex/exrex-%%{version}.tar.gz
# pypi has no tests
Source:         https://github.com/asciimoo/exrex/archive/v%{version}.tar.gz#/exrex-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A command line tool and python module that generates all or random matching strings to a given regular expression and more.

%prep
%setup -q -n exrex-%{version}
sed -i '1s/^#!.*//' exrex.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/exrex
rm %{buildroot}%{_bindir}/exrex.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # comment
LANG=C.UTF-8 PYTHONPATH=%{buildroot}%{$python_sitelib} $python ./tests.py}

%post
%python_install_alternative exrex

%postun
%python_uninstall_alternative exrex

%files %{python_files}
%{python_sitelib}/exrex*
%{python_sitelib}/__pycache__/exrex.*
%{python_sitelib}/exrex-%{version}*-info
%license COPYING
%doc README.md doc/
%python_alternative %{_bindir}/exrex

%changelog
