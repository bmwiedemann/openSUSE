#
# spec file for package rzip
#
# Copyright (c) 2024 SUSE LLC
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


Name:           rzip
Version:        2.1
Release:        0
Summary:        A large-file compression program
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://rzip.samba.org
Source:         https://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
Patch0:         fill-buffer.patch
BuildRequires:  libbz2-devel
BuildRequires:  libtool

%description
rzip is a compression program, similar in functionality to gzip or
bzip2, but able to take advantage long distance redundencies in files,
which can sometimes allow rzip to produce much better compression
ratios than other programs.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install INSTALL_BIN=%{buildroot}/%{_bindir} INSTALL_MAN=%{buildroot}%{_mandir}

%files
%license COPYING
%{_bindir}/rzip
%{_mandir}/man1/rzip.1%{?ext_man}

%changelog
