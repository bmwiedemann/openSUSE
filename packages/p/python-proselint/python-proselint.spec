#
# spec file for package python-proselint
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
%bcond_without python2
Name:           python-proselint
Version:        0.10.2
Release:        0
Summary:        A linter for prose
License:        BSD-3-Clause
URL:            https://github.com/amperser/proselint
Source:         https://files.pythonhosted.org/packages/source/p/proselint/proselint-%{version}.tar.gz
# test_weasel_words_misc is empty in release v0.10.2, and contains nose.SkipTest
Patch0:         disable-empty-test.patch
Patch1:         test-use-sys-executable.patch
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#amperser/proselint#1097 mcepl@suse.com
# this patch makes things totally awesome
Patch2:         remove_nose.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-dbm
Requires:       python-future
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%if %{with python2}
BuildRequires:  python-mock
%endif
# /SECTION
%python_subpackages

%description
proselint is a linter for English prose. (A linter is a computer
program that, like a spell checker, scans through a document and
analyzes it.)

Proselint is a command-line utility that can be integrated into
existing tools.

%prep
%setup -q -n proselint-%{version}
%autopatch -p1

sed -i -e '/^#!\//, 1d' proselint/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/proselint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative proselint

%postun
%python_uninstall_alternative proselint

%check
mkdir ~/bin
export PATH=~/bin:$PATH
%{python_expand cp %{buildroot}%{_bindir}/proselint-%{$python_bin_suffix} ~/bin/proselint
PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/proselint
%{python_sitelib}/proselint/
%{python_sitelib}/proselint-%{version}-py*.egg-info

%changelog
