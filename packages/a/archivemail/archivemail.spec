#
# spec file for package archivemail
#
# Copyright (c) 2020 SUSE LLC
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


Name:           archivemail
Version:        0.9.0
Release:        0
Summary:        Tool for Archiving and Compressing Old Email in Mailboxes
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://archivemail.sf.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ed
BuildRequires:  python-base
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
archivemail is a tool for archiving and compressing old email in mailboxes. It
moves messages older than the specified number of days to a separate mbox
format mailbox that is compressed with gzip. It can also just delete old email
rather than archive it.

%prep
%setup -q
ed -s examples/archivemail_all 2>/dev/null <<'EOF'
,s/\/usr\/local\/bin\/archivemail/\/usr\/bin\/archivemail/
w
EOF

%build
%python2_build

%install
%python2_install
# we don't need the egg file which python => 2.5 installs
rm -f %{buildroot}/%{python_sitelib}/*

%files
%license COPYING
%doc CHANGELOG examples/* FAQ README TODO
%{_bindir}/archivemail
%{_mandir}/man1/archivemail.1%{?ext_man}

%changelog
