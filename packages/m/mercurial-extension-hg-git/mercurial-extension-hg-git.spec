#
# spec file for package mercurial-extension-hg-git
#
# Copyright (c) 2025 SUSE LLC
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

%if 0%{?suse_version} > 1600
# Tumbleweed
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           mercurial-extension-hg-git
Version:        1.2.0
Release:        0
Summary:        Hg-Git Mercurial plugin
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            http://foss.heptapod.net/mercurial/hg-git
Source0:        https://files.pythonhosted.org/packages/source/h/hg-git/hg_git-%{version}.tar.gz
Source90:       tests.blacklist
BuildRequires:  %{python_module dulwich >= 0.21.6}
BuildRequires:  %{pythons}
# python311-gpg is not available on Leap 15.6.
%if 0%{?suse_version} > 1600
BuildRequires:  %{python_module gpg}
%endif
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  openssh-clients
BuildRequires:  python-rpm-macros
# On Leap, setuptools_scm does not explicitly require toml, but needs it to provide the correct version in dist-info.
%if 0%{?suse_version} < 1550
BuildRequires:  %{python_module toml}
%endif
BuildRequires:  unzip
Requires:       %{python_module dulwich >= 0.21.6}
Requires:       mercurial
Provides:       %{python_module hg-git = %{version}-%{release}}
Obsoletes:      %{python_module hg-git < %{version}-%{release}}
BuildArch:      noarch

%description
This plugin for Mercurial adds the ability to push and pull to/from a Git server repository from Hg. This means you can collaborate on Git based projects from Hg, or use a Git server as a collaboration point for a team with developers using both Git and Hg.

The Hg-Git plugin can convert commits/changesets losslessly from one system to another, so you can push via a Mercurial repository and another Hg client can pull it and their changeset node ids will be identical - Mercurial data does not get lost in translation. It is intended that Hg users may wish to use this to collaborate even if no Git users are involved in the project, and it may even provide some advantages if you’re using Bookmarks.

%prep
%setup -q -n hg_git-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}

%check
%if %{with test}
make tests HGPYTHON=%{expand:%%__%{pythons}} TESTFLAGS="--blacklist=%{SOURCE90}"
%endif

%files
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
