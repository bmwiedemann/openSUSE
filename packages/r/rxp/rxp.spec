#
# spec file for package rxp
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rxp
Version:        1.4.8
Release:        0
Summary:        XML Parser in C
License:        GPL-2.0+
Group:          Productivity/Publishing/XML
Url:            http://www.cogsci.ed.ac.uk/~richard/rxp.html
Source:         ftp://ftp.cogsci.ed.ac.uk/pub/richard/rxp-%{version}.tar.bz2
Patch0:         rxp-1.4.8.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The current version of RXP supports XML 1.1, Namespaces 1.1, xml:id,
and XML Catalogs. To use an XML Catalog, set the environment variable
XML_CATALOG_FILES to a space-separated list of catalog files.

RXP was written by Richard Tobin at the Language Technology Group,
Human Communication Research Centre, University of Edinburgh.

A simple application (called rxp) is provided. It parses and writes XML
data, optionally expanding entities, defaulting attributes, and
translating to a different output encoding.

Bug reports should be sent to richard@cogsci.ed.ac.uk.



Authors:
--------
    Richard Tobin <richard@cogsci.ed.ac.uk>

%prep
%setup -q
%patch0 -p1

%build
mv Makefile Makefile.orig
%{__sed} -e 's/^LIBS:/\#LIBS:/'  Makefile.orig > Makefile
%{__make} "DEBUG=%{optflags}" # CHAR_SIZE=8

%install
%{__install} -d -m755 %{buildroot}
%{__install} -d -m755 %{buildroot}/usr/bin
%{__install} -d -m755 %{buildroot}%{_mandir}/man1
%{__install} -m755 rxp %{buildroot}/usr/bin
%{__install} -m644 rxp.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-, root, root)
%doc COPYRIGHT COPYING Manual Threads
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
