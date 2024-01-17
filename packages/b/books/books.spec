#
# spec file for package books
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



Name:           books
License:        GPL-2.0+ and SUSE-LDPL-2.0
Group:          Documentation/Other
Provides:       handbuch lx-buch1
AutoReqProv:    off
Summary:        Several Linux Books
Version:        2009.1.12
Release:        1
BuildArch:      noarch
Source:         LDP.tgz
Source1:        http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/module-programming-guide/lkmpg-1.1.0.pdf.tar.gz
Source11:       http://www.linuxdoc.org/LDP/nag2/nag2.pdf
Source12:       http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/system-admin-guide/sag-0.6.2.pdf.gz
Source13:       http://www.linuxdoc.org/LDP/lki/lki.pdf
Source14:       http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/users-guide/user-beta-1.pdf.gz
Source15:       http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/programmers-guide/lpg-0.4.pdf
Source16:       http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/install-guide/install-guide-3.2.pdf.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#

%prep
%setup -n LDP -a 1
cp -a %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} .
gunzip *.gz

%build
mv lkmpg-1.1.0.pdf/*.pdf .
rmdir lkmpg-1.1.0.pdf

%install
install -d $RPM_BUILD_ROOT/usr/share/doc/Books
cp -a LDP* README linux-logo.ps *.pdf $RPM_BUILD_ROOT/usr/share/doc/Books

%files
%defattr(-,root,root)
%doc /usr/share/doc/Books

%description
This package contains some books, which are installed under
/usr/share/doc/Books.

The books are:

"Linux Installation and getting started" by Matt Welsh

"Linux Programmers Guide" by Sven Goldt and Sven van der Meer

"Linux Network Administrators Guide, Second Edition" by Olaf Kirch and
Terry Dawson

"Linux System Administrators Guide" by Lars Wirzenius

"Linux Users Guide" by Larry Greenfield

"Linux Kernel 2.4 Internals" by Tigran Aivazian

"The Linux Kernel Module Programming Guide" by Ori Pomerantz




%changelog
