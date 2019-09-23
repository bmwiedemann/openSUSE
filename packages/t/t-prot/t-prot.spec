#
# spec file for package t-prot
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           t-prot
Summary:        A Display Filter for RFC822 Messages
License:        BSD-4-Clause
Group:          Productivity/Networking/Email/Utilities
Version:        3.4
Release:        0
Url:            http://www.escape.de/users/tolot/mutt/
Source:         http://www.escape.de/~tolot/mutt/t-prot/downloads/%{name}-%{version}.tar.gz
Source1:        muttrc.t-prot
Requires:       perl(Getopt::Long)
Requires:       perl(Locale::gettext)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::gettext)

%description
t-prot detects and, when demanded, hides annoying parts in rfc822
messages: TOFU (see below), huge quoted blocks, signatures (especially
when they are too long), excessive punctuation, blocks of empty lines,
and trailing spaces and tabs. For use inside of MTAs or MDAs, it may
exit with appropriate libc exit codes, so annoying messages may be
bounced easily.

TOFU is an abbreviation that mixes German and English words. It expands
to "text oben, full-quote unten" that means "text above - full quote
below" and describes the style of many users who let their mailer or
newsreader quote everything of the previous message and just add some
text at the top.

%prep
%setup -q
cp %{SOURCE1} .

%build
sed -e "s#@docdir@#%{_defaultdocdir}/%{name}#g" t-prot.1 > x && mv x t-prot.1

%install
install -D -m 755 t-prot %{buildroot}%{_bindir}/t-prot
install -D -m 644 t-prot.1 %{buildroot}/%{_mandir}/man1/t-prot.1

%files
%defattr(-,root,root)
%doc ChangeLog README TODO muttrc.t-prot
%{_bindir}/t-prot
%{_mandir}/man1/t-prot.1.gz

%changelog
