#
# spec file for package git-deps
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
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygit2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygit2
# for html subpackage
Requires:       python-Flask
#Requires:       nodejs-browserify # broken/missing
Requires:       npm
BuildArch:      noarch
%python_subpackages

%description
Tool to analyze git dependencies

file bugs at https://github.com/aspiers/git-deps/issues

%package html
Summary:        Tool to analyze git deps - HTML parts
Group:          Development/Tools/Version Control

%description html
Documentation for git-deps.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
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
