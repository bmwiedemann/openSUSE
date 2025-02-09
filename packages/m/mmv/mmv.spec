#
# spec file for package mmv
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


Name:           mmv
Version:        2.10
Release:        0
Summary:        Move/Copy/Append/Link Multiple Files by Wildcard Patterns
License:        GPL-1.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/rrthomas/mmv/
Source:         https://github.com/rrthomas/mmv/releases/download/v%{version}/mmv-%{version}.tar.gz
BuildRequires:  c_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bdw-gc)

%description
Mmv moves (or copies, appends, or links, as specified) each source file matching
a from pattern to the target name specified by the to pattern.  This multiple
action is performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other target names.
Furthermore, before doing anything, mmv attempts to detect any errors that would
result from the entire set of actions specified and gives the user the choice of
either proceeding by avoiding the offending parts or aborting.

%prep
%autosetup

%build
%configure --docdir="%{_defaultdocdir}/%{name}"
%make_build

%install
%make_install
cp -a COPYING "%{buildroot}/%{_defaultdocdir}/%{name}/"

%files
%{_defaultdocdir}/%{name}/
%{_bindir}/mad
%{_bindir}/mcp
%{_bindir}/mln
%{_bindir}/mmv
%{_mandir}/man1/mad.1%{?ext_man}
%{_mandir}/man1/mcp.1%{?ext_man}
%{_mandir}/man1/mln.1%{?ext_man}
%{_mandir}/man1/mmv.1%{?ext_man}

%changelog
