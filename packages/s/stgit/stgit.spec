#
# spec file for package stgit
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


Name:           stgit
Version:        1.5
Release:        0
Summary:        Stacked GIT - Source Code Management Tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://stacked-git.github.io
Source0:        https://github.com/ctmarinas/stgit/releases/download/v%{version}/stgit-%{version}.tar.gz
# Patch sent upstream, PR 81: https://github.com/stacked-git/stgit/pull/81
Patch1:         stgbashprompt-noexec.patch
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  xmlto
Requires:       git-core
BuildArch:      noarch

%description
StGIT is a Python application providing similar functionality to Quilt
(i.e. pushing/popping patches to/from a stack) on top of GIT. These
operations are performed using GIT commands and the patches are stored
as GIT commit objects, allowing easy merging of the StGIT patches into
other repositories using standard GIT functionality.

%prep
%setup -q
%patch1 -p1

%build
%python3_build
PYTHON=python3 make %{?_smp_mflags} prefix=%{_prefix} doc

%install
%python3_install
PYTHON=python3 make %{?_smp_mflags} prefix=%{_prefix} mandir=%{_mandir} DESTDIR=%{buildroot} install-doc
# avoid unreproducible pyc files https://bugs.python.org/issue34033 https://github.com/python/cpython/pull/8057
%py3_compile %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc CONTRIBUTING.md CHANGELOG.md TODO
%{_bindir}/stg
%{_mandir}/man1/stg*%{ext_man}
%{python3_sitelib}/*

%changelog
