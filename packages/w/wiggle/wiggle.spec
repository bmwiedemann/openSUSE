#
# spec file for package wiggle
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


Name:           wiggle
Version:        1.3
Release:        0
Summary:        A Tool for Applying Patches with Conflicts
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://neil.brown.name/wiggle/
Source0:        https://github.com/neilbrown/wiggle/archive/v%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
Wiggle is a program for applying patches that 'patch' cannot apply due
to conflicting changes in the original.

Wiggle will always apply all changes in the patch to the original. If
it cannot find a way to cleanly apply a patch, it inserts it in the
original in a manner similar to 'merge' and reports an unresolvable
conflict.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="-I. %{optflags}" wiggle

%install
%make_install

%files
%doc ANNOUNCE
%license COPYING
%{_bindir}/wiggle
%{_mandir}/man1/wiggle.1%{?ext_man}

%changelog
