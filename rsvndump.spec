# vim: set ts=4 sw=4 et:
#
# spec file for package rsvndump
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           rsvndump
Version:        0.6.1
Release:        0
Summary:        Remote Subversion Repository Dumping Tool
License:        GPL-3.0-only
Group:          Development/Tools/Version Control
URL:            https://rsvndump.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/rsvndump/rsvndump-%{version}.tar.gz
BuildRequires:  libapr-util1-devel
BuildRequires:  libapr1-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsvn_delta)
BuildRequires:  pkgconfig(libsvn_fs)
BuildRequires:  pkgconfig(libsvn_ra)
BuildRequires:  pkgconfig(libsvn_subr)

%description
rsvndump is a command line tool that is able to dump a subversion
repository that resides on a remote server. All data is dumped in the
format that can be read/written by svnadmin, so the data produced by
rsvndump can easily be imported into a new subversion repository.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang rsvndump

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/rsvndump

%files lang -f %{name}.lang
%license COPYING

%changelog
