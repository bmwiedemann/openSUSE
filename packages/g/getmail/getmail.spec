#
# spec file for package getmail
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


Name:           getmail
Version:        5.13
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pyropus.ca/software/getmail/
Source:         http://pyropus.ca/software/getmail/old-versions/getmail-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
Patch1:         getmail-fix_paths.patch
Summary:        Simple, Secure and Reliable Email Retriever
License:        GPL-2.0-only
Group:          Productivity/Networking/Email/Utilities
Provides:       python-getmail = %{version}-%{release}
Provides:       python-getmailcore = %{version}-%{release}
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
BuildRequires:  perl
BuildRequires:  python-devel
%py_requires

%description
getmail is intended as a simple, secure, and reliable replacement for
fetchmail. It retrieves email (either all messages, or only unread messages)
from one or more POP3, SPDS, or IMAP4 servers (with or without SSL) for one or
more email accounts, and reliably delivers into qmail-style Maildirs, mboxrd
files, or through external MDAs (command deliveries) specified on a per-account
basis. getmail also has excellent support for domain (multidrop) mailboxes,
including delivering messages to different users or destinations based on the
envelope recipient address.


%package doc

Summary:        Documentation for %{name}
Group:          Productivity/Networking/Email/Utilities

%description doc
getmail is intended as a simple, secure, and reliable replacement for
fetchmail.

This package contains the configuration, FAQ and troubleshooting
documentation, under %{_docdir}/%{name}/

%prep
%setup -q
%patch1 -p1
%__sed -i \
	-e 's|@@DOCDIR@@|%{_docdir}/%{name}|g' \
	-e 's|@@MANDIR@@|%{_mandir}|g' \
	setup.py

pushd getmailcore
%__perl -ni -e 'print $_ unless m|^#!\s*/|' *.py
%__chmod 0644 *.py
popd #getmailcore

%build
CFLAGS="%{optflags}" \
%__python ./setup.py build

%install
%__python ./setup.py install \
	--prefix="%{_prefix}" \
	--root="%{buildroot}" \
	--record-rpm=files.lst

%__perl -ni -e 'chomp; print $_,"\n" unless m|^(%dir\s+)?%{_docdir}/?$|' files.lst
%__perl -pi -e 's/^/%doc / if m|^(%dir\s+)?%{_docdir}/|' files.lst
%__perl -pi -e 's/$/*/ if m|^%{_mandir}/|' files.lst

%__perl -ni -e 'print unless m,%{_docdir}/%{name}/.+\.(html|txt|css)$,' files.lst

%files -f files.lst
%defattr(-,root,root,0755)
%doc %dir %{_docdir}/%{name}

%files doc
%defattr(-,root,root,0755)
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/*.css

%changelog
