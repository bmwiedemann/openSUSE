#
# spec file for package sgml-skel
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sgml-skel
Version:        0.7.1
Release:        0
Summary:        Helper Scripts for the SGML System
License:        GPL-2.0+
Group:          Productivity/Publishing/SGML
Url:            https://github.com/openSUSE/sgml-skel
Source0:        https://github.com/openSUSE/sgml-skel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libxml2
Requires:       /bin/awk
Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       libxml2-tools
Requires:       libxslt-tools
Requires(post): /bin/awk
Requires(post): bash
Requires(post): coreutils
Requires(post): findutils
Requires(post): libxml2-tools
Requires(post): libxslt-tools
BuildArch:      noarch

%description
These scripts will help prepare and maintain parts of an SGML system.

%prep
%setup -q

%build
autoreconf -fiv
%configure

%install
%make_install
ln -sf sgml2xmlcat.sh %{buildroot}%{_bindir}/sgmlcat2x.sh
ln -sf install-catalog %{buildroot}%{_bindir}/install-catalog.sh
ln -sf edit-xml-catalog %{buildroot}%{_bindir}/edit-xml-catalog.sh
install -d -m755 %{buildroot}%{_datadir}/sgml
install -d -m755 %{buildroot}%{_sysconfdir}/{sgml,xml}
install -d -m755 %{buildroot}%{_localstatedir}/lib/sgml
touch %{buildroot}%{_sysconfdir}/sgml/catalog
xmlcatalog --noout --create %{buildroot}%{_sysconfdir}/xml/suse-catalog.xml
xmlcatalog --noout --create %{buildroot}%{_sysconfdir}/xml/catalog
# Use correct order: first new method, second old method
xmlcatalog --noout --add  "nextCatalog" "catalog-d.xml" "catalog-d.xml" %{buildroot}%{_sysconfdir}/xml/catalog
xmlcatalog --noout --add  "nextCatalog" "suse-catalog.xml" "suse-catalog.xml" %{buildroot}%{_sysconfdir}/xml/catalog
install -d -m755 %{buildroot}%{_sysconfdir}/xml/catalog.d

%post
# only create suse-catalog.xml at installation time; not in the update case
if [ "$1" = 1 ]; then
  [ -r %{_sysconfdir}/xml/suse-catalog.xml ] \
    || xmlcatalog --create  | sed 's:/>:>\
</catalog>:' >%{_sysconfdir}/xml/suse-catalog.xml
fi
update-xml-catalog

%files
%defattr(-, root, root)
%dir %{_sysconfdir}/sgml
%dir %{_sysconfdir}/xml
%dir %{_sysconfdir}/xml/catalog.d
%dir %{_localstatedir}/lib/sgml
%doc AUTHORS COPYING ChangeLog README*
%ghost %{_sysconfdir}/sgml/catalog
%ghost %{_sysconfdir}/xml/suse-catalog.xml
%ghost %{_sysconfdir}/xml/catalog-d.xml
%config %verify(not md5 size mtime) %{_sysconfdir}/xml/catalog
%{_bindir}/*
%{_mandir}/man1/*

%changelog
