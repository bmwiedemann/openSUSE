#
# spec file for package stgit
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


Name:           stgit
Version:        0.19
Release:        0
Summary:        Stacked GIT - Source Code Management Tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
Url:            https://github.com/ctmarinas/stgit
Source0:        https://github.com/ctmarinas/stgit/releases/download/v%{version}/stgit-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  git-core
BuildRequires:  python-devel
BuildRequires:  xmlto
Requires:       git-core
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description
StGIT is a Python application providing similar functionality to Quilt
(i.e. pushing/popping patches to/from a stack) on top of GIT. These
operations are performed using GIT commands and the patches are stored
as GIT commit objects, allowing easy merging of the StGIT patches into
other repositories using standard GIT functionality.

%prep
%setup -q

%build
make %{?_smp_mflags} prefix=%{_prefix} all doc

%install
make prefix=%{_prefix} DESTDIR=%{buildroot} install
make -C Documentation prefix=%{_prefix} mandir=%{_mandir} DESTDIR=%{buildroot} install

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README RELEASENOTES TODO
%{_bindir}/stg
%{_mandir}/man1/stg*%{ext_man}
%if 0%{?suse_version} > 1110
%{python_sitelib}/*
%else
%{py_sitedir}/*
%endif
%{_datadir}/stgit

%changelog
