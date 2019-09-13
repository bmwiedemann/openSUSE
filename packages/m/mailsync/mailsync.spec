#
# spec file for package mailsync
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mailsync
Version:        5.2.1
Release:        0
Summary:        The Mail Sync Tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
Url:            http://sourceforge.net/projects/mailsync/
Source:         https://sourceforge.net/projects/mailsync/files/mailsync/%{version}/mailsync_%{version}.orig.tar.gz
Patch0:         mailsync-correct-format-errors.patch
Patch1:         mailsync-gcc9.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  imap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel

%description
Mailsync is a way of keeping a collection of mailboxes synchronized. The
mailboxes may be on the local file system or on an IMAP server.

%prep
%setup -q
%autopatch -p1

%build
# parameter is passed to ./configure, --help is fastest way out :-)
./autogen.sh --help
%configure
make %{?_smp_mflags}

%install
install -Dpm 0755 src/%{name} \
  %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 doc/%{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc AUTHORS COPYING NEWS README THANKS TODO doc/examples/ doc/ABSTRACT
%{_bindir}/mailsync
%{_mandir}/man1/mailsync.1%{ext_man}

%changelog
