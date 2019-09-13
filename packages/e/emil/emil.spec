#
# spec file for package emil
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           emil
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
Version:        2.1.0beta9
Release:        0
Summary:        E-Mail Filter
Source:         ftp://ftp.uu.se/pub/unix/networking/mail/emil/emil-2.1.0-beta9.tar.gz
Patch:          emil-2.1.0-beta9.diff
Patch1:         ftp://ftp.uu.se/pub/unix/networking/mail/emil/emil-2.1.0-beta9.patch1
Patch2:         warn.patch
Patch3:         emil-2.1.0-beta9-flex.patch
Patch4:         emil-2.1.0-beta9-getline.patch
Patch5:         emil-2.1.0-beta9-destdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program enables you to convert MIME, SUN mailtool, and 'plain old
style RFC822'.

It is especially useful for elm users.

%prep
%setup -q -n emil-2.1.0-beta9
%patch
%patch1
%patch2
%patch3
%patch4
%patch5

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} SENDMAILPATH=/usr/sbin/sendmail

%install
%makeinstall

%files
%defattr(-,root,root)
/usr/bin/emil
%{_libdir}/charsets.cpl
%config %{_libdir}/emil.cf
%{_mandir}/man8/emil.8.gz
%{_mandir}/man8/emil.cf.8.gz

%changelog
