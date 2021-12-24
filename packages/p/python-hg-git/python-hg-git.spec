#
# spec file for package python-hg-git
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


%if 0%{?suse_version} >= 1550
%bcond_without test
%else
%bcond_with test
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pythons python3
Name:           python-hg-git
Version:        0.10.3+hg.1646
Release:        0
Summary:        Hg-Git Mercurial plugin
License:        GPL-2.0-only
URL:            http://foss.heptapod.net/mercurial/hg-git
# Source:         https://files.pythonhosted.org/packages/source/h/hg-git/hg-git-%%{version}.tar.gz
Source:         hg-git-%{version}.tar.gz
BuildRequires:  %{python_module dulwich >= 0.19.0}
BuildRequires:  %{python_module gpg}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       mercurial
Requires:       python-dulwich >= 0.19.0
BuildArch:      noarch
Provides:       mercurial-extension-hg-git = %{version}-%{release}
Obsoletes:      mercurial-extension-hg-git < %{version}-%{release}
%python_subpackages

%description
This plugin for Mercurial adds the ability to push and pull to/from
a Git server repository from Hg. This means you can collaborate on Git
based projects from Hg, or use a Git server as a collaboration point for
a team with developers using both Git and Hg.

The Hg-Git plugin can convert commits/changesets losslessly from one
system to another, so you can push via a Mercurial repository and
another Hg client can pull it and their changeset node ids will be
identical - Mercurial data does not get lost in translation. It is
intended that Hg users may wish to use this to collaborate even if no
Git users are involved in the project, and it may even provide some
advantages if you’re using Bookmarks.

%prep
%autosetup -p1 -n hg-git-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
%python_exec tests/run-tests.py -v
%endif

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
