#
# spec file for package hg-git
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           hg-git
Version:        0.8.10
Release:        0
Summary:        Mercurial Plugin for Communicating with Git Servers
License:        GPL-2.0+
Group:          Development/Tools/Version Control
Url:            https://hg-git.github.io
Source0:        https://pypi.python.org/packages/22/58/ce0a438b74a1a87292e926c4c1bac866acfae207ea11d2d0bd764117cdcc/%{name}-%{version}.tar.gz
Source1:        https://pypi.python.org/packages/22/58/ce0a438b74a1a87292e926c4c1bac866acfae207ea11d2d0bd764117cdcc/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  git-daemon
BuildRequires:  mercurial
BuildRequires:  netcat-openbsd
BuildRequires:  python-devel
BuildRequires:  python-dulwich >= 0.9.7
BuildRequires:  python-setuptools
Requires:       mercurial
Requires:       python-dulwich >= 0.9.7
BuildArch:      noarch

%description
This is the Hg-Git plugin for Mercurial, adding the ability to push and pull
to/from a Git server repository from Hg. This means you can collaborate on Git
based projects from Hg, or use a Git server as a collaboration point for a team
with developers using both Git and Hg.

The Hg-Git plugin can convert commits/changesets losslessly from one system to
another, so you can push via an Hg repository and another Hg client can pull it
and their changeset node ids will be identical - Mercurial data does not get
lost in translation.

%prep
%setup -q

%build
python setup.py build

%check
export PYTHONPATH="%{buildroot}%{python_sitelib}"
#pushd tests
#python run-tests.py --verbose --with-hg=%%{_bindir}/hg
#popd

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc COPYING README.md
%{python_sitelib}

%changelog
