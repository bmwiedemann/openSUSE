#
# spec file for package docbook2x
#
# Copyright (c) 2025 SUSE LLC
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


Name:           docbook2x
Summary:        DocBook-to-Texinfo Converter
License:        MIT
Group:          Productivity/Publishing/DocBook
Version:        0.8.8
Release:        0
URL:            http://docbook2x.sourceforge.net/
Source0:        https://sourceforge.net/projects/docbook2x/files/docbook2x/%{version}/docbook2X-%{version}.tar.gz/download#/docbook2X-%{version}.tar.gz
Source1:        docbook2x-README.SUSE
Patch0:         docbook2X-0.8.8-catalog.diff
BuildRequires:  automake
BuildRequires:  docbook_4
BuildRequires:  libxslt-devel
BuildRequires:  makeinfo
BuildRequires:  openjade
BuildRequires:  perl-XML-DOM
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX
BuildRequires:  perl-libwww-perl
BuildRequires:  sgml-skel
Provides:       db2x = %{version}
Obsoletes:      db2x < %{version}
Provides:       docbook2X
Requires:       docbook_4
Requires:       openjade
Requires:       opensp
Requires:       perl-URI
Requires:       perl-XML-DOM
Requires:       perl-XML-Parser
Requires:       perl-XML-RegExp
Requires:       perl-XML-SAX
Requires:       perl-libwww-perl
Requires:       sgml-skel
Requires:       tidy
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         awk
PreReq:         grep
PreReq:         sed

%description
A new tool based on Perl modules.

%package doc
Summary:        DocBook-to-Texinfo Converter
Group:          Productivity/Publishing/DocBook
PreReq:         %install_info_prereq

%description doc
A new tool based on Perl modules.

%prep
%setup -q -n docbook2X-%{version}
cp %{S:1} README.SUSE
%patch -P 0 -p 1

%build
autoreconf --force --install
%configure --with-xmldecl=/usr/share/sgml/opensp/xml.dcl
sed -i.bak 's/${prefix}/\/usr/' perl/config.pl
# exit 1
%make_build htmldir=%{_docdir}/%{name}/html
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
xmlcatbin=/usr/bin/xmlcatalog
CATALOG=usr/share/docbook2X/dtd/catalog.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegateSystem" \
  "http://docbook2x.sf.net/latest/" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
%make_install \
  nsgmls_xmldecl=/usr/share/sgml/opensp/xml.dcl \
  htmldir=%{_docdir}/%{name}/html
rm -f %{buildroot}/%{_infodir}/dir
mv %{buildroot}%{_mandir}/man1/docbook2man.1 \
  %{buildroot}%{_mandir}/man1/docbook-to-man.1
mv %{buildroot}%{_mandir}/man1/docbook2texi.1 \
  %{buildroot}%{_mandir}/man1/docbook-to-texi.1
mv %{buildroot}%{_bindir}/docbook2man \
  %{buildroot}%{_bindir}/docbook-to-man
mv %{buildroot}%{_bindir}/docbook2texi \
  %{buildroot}%{_bindir}/docbook-to-texi
%perl_process_packlist
install -m644 -D -t %{buildroot}/etc/xml %{FOR_ROOT_CAT}

%define info_files docbook2texi-xslt docbook2man-xslt docbook2X

%post
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}

%postun
# remove entries only on removal of file
if [ ! -f %{_sysconfdir}/xml/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi
exit 0

%post doc
for f in %{info_files}; do
  %install_info --info-dir=%{_infodir} %{_infodir}/${f}.info.gz
done

%preun doc
for f in %{info_files}; do
  %install_info_delete --info-dir=%{_infodir} %{_infodir}/${f}.info.gz
done

%files
%config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}
%{_bindir}/*
%{_datadir}/docbook2X

%files doc
%license COPYING
%doc AUTHORS NEWS README README.SUSE
%{_docdir}/%{name}
%{_infodir}/*
%{_mandir}/*/*

%changelog
