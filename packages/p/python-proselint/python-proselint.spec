#
# spec file for package python-proselint
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
Name:           python-proselint
Version:        0.10.2
Release:        0
Summary:        A linter for prose
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/amperser/proselint
Source:         https://files.pythonhosted.org/packages/source/p/proselint/proselint-%{version}.tar.gz
# test_weasel_words_misc is empty in this release, and `setup.py test` doesnt recognise nose's SkipTest
Patch0:         disable-empty-test.patch
Patch1:         test-use-sys-executable.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-future
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module six}
BuildRequires:  python2-gdbm
BuildRequires:  python2-mock
BuildRequires:  python3-dbm
# /SECTION
%ifpython3
Requires:       python3-dbm
%endif
%ifpython2
Recommends:     python-gdbm
%endif
%python_subpackages

%description
proselint is a linter for English prose. (A linter is a computer
program that, like a spell checker, scans through a document and
analyzes it.)

Proselint is a command-line utility that can be integrated into
existing tools.

%prep
%setup -q -n proselint-%{version}
%patch0 -p1
%patch1 -p1
sed -i -e '/^#!\//, 1d' proselint/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python3_only %{_bindir}/proselint
%{python_sitelib}/proselint/
%{python_sitelib}/proselint-%{version}-py*.egg-info

%changelog
