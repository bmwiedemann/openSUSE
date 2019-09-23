#
# spec file for package svn2git
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


Name:           svn2git
Version:        1.0.16
Release:        0
Summary:        Importer for one time conversion from SVN to Git
License:        GPL-3.0-only
Group:          Development/Tools/Version Control
URL:            http://github.com/svn-all-fast-export/svn2git
Source0:        https://github.com/svn-all-fast-export/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel
BuildRequires:  pkgconfig(Qt5Core)
Requires:       git
Requires:       subversion

%description
Tool to convert an SVN repository to Git based on a custom written ruleset, in
order to properly migrate all branches and tags.

%prep
%setup -q

%build
%qmake5 -o Makefile fast-export2.pro CONFIG+=RELEASE
%make_jobs

%install
install -Dm755 svn-all-fast-export %{buildroot}/%{_bindir}/svn-all-fast-export
ln -s %{_bindir}/svn-all-fast-export %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc samples README.md
%{_bindir}/svn-all-fast-export
%{_bindir}/%{name}

%changelog
