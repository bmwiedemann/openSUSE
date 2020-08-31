#
# spec file for package patchutils
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


Name:           patchutils
Version:        0.4.2
Release:        0
Summary:        A Collection of Tools for Manipulating Patch Files
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://cyberelk.net/tim/software/patchutils/
Source0:        http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.xz
Source1:        http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.xz.sig
Patch2:         rediff-hunk-init-fix.diff
BuildRequires:  automake
Requires:       diffutils
Requires:       patch

%description
Patchutils contains a collection of tools for manipulating patch files:
interdiff, combinediff, filterdiff, fixcvsdiff, rediff, lsdiff, and
splitdiff. You can use interdiff to create an incremental patch between
two patches that are against a common source tree. Combinediff can be
used for creating a cumulative diff from two incremental patches.
Filterdiff is for extracting or excluding patches from a patch set
based on modified files matching shell wildcards. Lsdiff lists modified
files in a patch. Rediff corrects hand-edited patches.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build --jobs=1 check

%install
%make_install
install -m 0755 -d %{buildroot}%{_mandir}/man1/
install -m 0644 -t %{buildroot}%{_mandir}/man1/ doc/*.1

%files
%license COPYING
%doc BUGS README
%{_bindir}/combinediff
%{_bindir}/dehtmldiff
%{_bindir}/editdiff
%{_bindir}/espdiff
%{_bindir}/filterdiff
%{_bindir}/fixcvsdiff
%{_bindir}/flipdiff
%{_bindir}/gitdiff
%{_bindir}/gitdiffview
%{_bindir}/grepdiff
%{_bindir}/interdiff
%{_bindir}/lsdiff
%{_bindir}/patchview
%{_bindir}/recountdiff
%{_bindir}/rediff
%{_bindir}/splitdiff
%exclude %{_bindir}/svndiff
%exclude %{_bindir}/svndiffview
%{_bindir}/unwrapdiff
%{_mandir}/man1/*.1%{?ext_man}

%changelog
