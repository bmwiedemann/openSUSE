#
# spec file for package gitslave
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gitslave
Version:        2.0.2
Release:        0
Summary:        Creates a group of related repositories
License:        SUSE-Gitslave
Group:          Development/Tools/Version Control
Url:            http://gitslave.sourceforge.net
Source:         http://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
Requires:       git-core
Requires:       perl
Recommends:     perl-Parallel-Iterator
Recommends:     perl-Term-ProgressBar
BuildArch:      noarch
# PATCH-FIX-UPSTREAM - git format-patch -1 0fc40b1e57f00acddd64ed88e44d28206f3682d6
Patch0:         0001-fix-inappropriate-REPO-substitution.patch
# PATCH-FIX-UPSTREAM - https://sourceforge.net/p/gitslave/bugs/19/
Patch1:         0002-fix-gits-unexpected-status.patch
# PATCH-FIX-UPSTREAM - https://sourceforge.net/p/gitslave/bugs/27/
Patch2:         0003-fix-pod2man-invocation.patch 
# PATCH-FIX-UPSTREAM - https://sourceforge.net/p/gitslave/bugs/25/
Patch3:         0004-fix-deprecation-warnings.patch

%description
Creates a group of related repositories—a superproject repository and
a number of slave repositories—all of which are concurrently developed on and
on which all git operations should normally operate; so when you branch, each
repository in the project is branched in turn.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Tools/Version Control
Recommends:     %{name} = %{version}

%description doc
This package provides documentation and help files for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags}

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
%__cp gits $RPM_BUILD_ROOT/%{_bindir}

install -d $RPM_BUILD_ROOT/%{_mandir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
%__cp gits.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%files
%defattr(-,root,root)
%{_bindir}/gits
%{_mandir}/man1/gits.1.gz

%files doc
%defattr(-,root,root)
%doc README LICENSE.README LICENSE.TXT ReleaseNotes web/*

%changelog
