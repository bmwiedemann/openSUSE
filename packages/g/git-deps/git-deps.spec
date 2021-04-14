#
# spec file for package git-deps
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           git-deps
Version:        1.0.2+git.1559732444.7c75531
Release:        0
Summary:        Tool to analyze git deps
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://github.com/aspiers/git-deps
Source:         %{name}-%{version}.tar.xz
Patch0:         dont-use-st-markdown.patch
Patch1:         Fix-issue-with-unbuffered-text-I-O-under-python3.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-pygit2
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-wheel
Requires:       python3-pygit2
# for html subpackage
Requires:       python3-Flask
#Requires:       nodejs-browserify # broken/missing
Requires:       npm
BuildArch:      noarch

%description
Tool to analyze git dependencies

file bugs at https://github.com/aspiers/git-deps/issues

%package html
Summary:        Tool to analyze git deps - HTML parts
Group:          Development/Tools/Version Control

%description html
Documentation for git-deps.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
python3 -s setup.py build

%install
python3 -s setup.py install -O1 --skip-build --force --root %{buildroot} --prefix %{_prefix}
%python_expand %fdupes %{buildroot}%{python_sitelib}

%files
%{_bindir}/git-deps
%{_bindir}/git-fixup
%{_bindir}/gitfile-handler
%{python_sitelib}/git_deps*
%license LICENSE.txt
%doc AUTHORS.rst CONTRIBUTING.md CHANGES.rst README.md USAGE.md
%doc HISTORY.md USE-CASES.md

%files html
%doc docs

%changelog
