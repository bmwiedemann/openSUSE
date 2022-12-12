#
# spec file for package mercurial-extension-hg-git
#
# Copyright (c) 2022 SUSE LLC
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

Name:           mercurial-extension-hg-git
Version:        1.0.1
Release:        0
Summary:        Hg-Git Mercurial plugin
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            http://foss.heptapod.net/mercurial/hg-git
Source0:        https://files.pythonhosted.org/packages/source/h/hg-git/hg-git-%{version}.tar.gz
Source90:       tests.blacklist
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-gpg
BuildRequires:  python3-setuptools
BuildRequires:  unzip
Requires:       mercurial
Requires:       python3-dulwich >= 0.19.0
Provides:       python3-hg-git = %{version}-%{release}
Obsoletes:      python3-hg-git < %{version}-%{release}
BuildArch:      noarch

%description
This plugin for Mercurial adds the ability to push and pull to/from a Git server repository from Hg. This means you can collaborate on Git based projects from Hg, or use a Git server as a collaboration point for a team with developers using both Git and Hg.

The Hg-Git plugin can convert commits/changesets losslessly from one system to another, so you can push via a Mercurial repository and another Hg client can pull it and their changeset node ids will be identical - Mercurial data does not get lost in translation. It is intended that Hg users may wish to use this to collaborate even if no Git users are involved in the project, and it may even provide some advantages if you’re using Bookmarks.

%prep
%setup -q -n hg-git-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
%if %{with test}
make tests HGPYTHON=python3 TESTFLAGS="--blacklist=%{SOURCE90}"
%endif

%files
%doc README.rst
%license COPYING
%{python3_sitelib}/*

%changelog
