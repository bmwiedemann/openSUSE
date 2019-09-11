#
# spec file for package sgrep
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sgrep
Version:        1.92a
Release:        0
Summary:        Searching for Structured Patterns
License:        GPL-2.0+
Group:          Productivity/Text/Utilities
Source:         ftp://ftp.cs.helsinki.fi/pub/Software/Local/Sgrep/sgrep-%{version}.tar.gz
Patch:          sgrep-sgreprc.diff
Patch1:         sgrep-no-build-date.patch
Url:            http://www.cs.helsinki.fi/~jjaakkol/sgrep.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sgrep is like "grep" but it will also work for structured patterns. You
can use the program to extract fragments from SGML/XML or any other
well formed text files (including UTF-8 encoded files).

%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q
%patch -p 1
%patch1

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
  ./configure --prefix=%{_prefix} --sysconfdir=/etc --datadir=/etc \
              --mandir=%{_mandir}
make

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%{INSTALL_DATA} sample.sgreprc $RPM_BUILD_ROOT/%{_sysconfdir}/sgreprc
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sample.sgreprc

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README sgrep.lsm
%doc sample.sgreprc
%config %{_sysconfdir}/sgreprc
%{_bindir}/sgrep
%{_mandir}/*/*

%changelog
