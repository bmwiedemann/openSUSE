#
# spec file for package mairix
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Summary:        A maildir indexer and searcher
License:        GPL-2.0
Group:          Productivity/Networking/Email/Utilities

Name:           mairix
Version:        0.22
Release:        0
Source0:        mairix-%{version}.tar.gz
Url:            http://www.rc0.org.uk/mairix/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex

%description
mairix is a tool for indexing email messages stored in maildir format
folders and performing fast searches on the resulting index.  The
output is a new maildir folder containing symbolic links to the matched
messages.



%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" 			\
./configure					\
		--prefix=/usr			\
		--docdir=%{_docdir}/mairix	\
		--mandir=%{_mandir}
CFLAGS="$RPM_OPT_FLAGS" 			\
make
strip mairix
# make docs

%install
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}
mkdir %{buildroot}
make DESTDIR=$RPM_BUILD_ROOT install
# make DESTDIR=$RPM_BUILD_ROOT install_docs
chmod 644 ACKNOWLEDGEMENTS README  COPYING  INSTALL dotmairixrc.eg

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/mairix
/usr/share/man/man*/*
%doc ACKNOWLEDGEMENTS README  COPYING  INSTALL dotmairixrc.eg

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%changelog
