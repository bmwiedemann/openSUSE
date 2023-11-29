#
# spec file for package rawhide
#
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rawhide
Version:        3.3
Release:        0
Summary:        Find files using pretty C expressions
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://raf.org/rawhide/
Source:         https://raf.org/rawhide/download/%{name}-%{version}.tar.gz
Patch0:         rawhide-3.3-configure-ignore-unknown-arguments.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libpcre2-8)

%description
Rawhide (rh(1)) lets you search for files on the command line using
expressions and user-defined functions in a mini-language inspired
by C. It's like find(1), but more fun to use.

Search criteria can be very readable and self-explanatory and/or
very concise and typeable, and you can create your own lexicon of
search terms. The output can include lots of detail, like ls(1).

You can search with file glob patterns and Perl-compatible regular
expressions (regexes). You can search by name, path, symlink target
path, body, access control list (ACL), extended attributes (EA),
and all the usual file metadata (file type, permissions, owner,
size, modification time, etc.).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING LICENSE
%config %{_sysconfdir}/rawhide.conf
%dir %{_sysconfdir}/rawhide.conf.d
%config %{_sysconfdir}/rawhide.conf.d/attributes
%{_bindir}/rh
%{_mandir}/man1/rh.1%{?ext_man}
%{_mandir}/man5/rawhide.conf.5%{?ext_man}

%changelog
