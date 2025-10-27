#
# spec file for package tdiff
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2020-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           tdiff
Version:        0.8.9
Release:        0
Summary:        File tree diff tool
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://github.com/F-i-f/tdiff/
#Git-Clone:     https://github.com/F-i-f/tdiff.git
Source:         http://ftp.fifi.org/phil/tdiff/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libacl)
# SECTION test requirements
BuildRequires:  acl
# /SECTION

%description
Compare file system trees, showing any differences in their:
  - file size,
  - file block count (physical storage size),
  - owner user and group ids (uid & gid),
  - access, modification and inode change times,
  - hard link count, and sets of hard linked files,
  - extended attributes (if supported),
  - ACLs (if supported).

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Text/Utilities
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (tdiff and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm -Rvf %{buildroot}%{_datadir}/doc/tdiff/

%check
# Tests randomly fail - disable for now
# see: https://github.com/F-i-f/tdiff/issues/2
#make %%{?_smp_mflags} check

%files
%license COPYING
%doc AUTHORS NEWS README README.md
%{_bindir}/tdiff
%{_mandir}/man1/tdiff.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/tdiff

%changelog
