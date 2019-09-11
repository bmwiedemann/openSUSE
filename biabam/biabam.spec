#
# spec file for package biabam
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


Name:           biabam
Version:        0.9.7
Release:        0
Url:            http://mmj.dk/biabam/
Summary:        A Bash Attachment Mailer
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Clients
Source:         %name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       /usr/sbin/sendmail sharutils
BuildArch:      noarch

%description
BIABAM is a small tool, useful when you want to mail attachments from
the command line. It has similarities to mailing attachments from the
commandline with Mutt, but it only depends on bash and uuencode.

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install biabam $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-,root,root)
%doc COPYING README
/usr/bin/*

%changelog
