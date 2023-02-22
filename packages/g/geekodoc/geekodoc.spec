#
# spec file for package geekodoc
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without  tests
#
Name:           geekodoc
Version:        2.2.2
Release:        0
Summary:        DocBook based RNG Schema for SUSE Documentation
License:        GPL-3.0-only
Group:          Productivity/Publishing/DocBook
URL:            https://github.com/openSUSE/geekodoc/archive/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.bz2
# Taken from maintenance/novdoc-2019-02-01
# Created with:
# $ git archive --prefix=novdoc-20190201/ \
#               --output=/tmp/novdoc-20190201.tar.bz2 \
#               --format=tar HEAD novdoc/ catalog.d/
Source10:       novdoc-20190201.tar.bz2
BuildRequires:  docbook_5 >= 5.1
BuildRequires:  fdupes
BuildRequires:  jing
BuildRequires:  libxml2-tools
BuildRequires:  make
%if 0%{?is_opensuse}
BuildRequires:  openSUSE-release
%else
BuildRequires:  sles-release
%endif
BuildRequires:  python3-rnginline
BuildRequires:  python3-setuptools
BuildRequires:  trang

Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun):sgml-skel >= 0.7
Conflicts:      suse-xsl-stylesheets < 2.0.6
BuildArch:      noarch

%description
GeekoDoc is a RELAX NG schema used for current SUSE documentation.

%package -n novdoc
Version:        1.0_%{version}
Release:        0
Summary:        DocBook based Schema for older SUSE Documentation
Group:          Productivity/Publishing/DocBook
Conflicts:      suse-xsl-stylesheets < 2.0.6

%description -n novdoc
NovDoc is a DTD/RELAX NG schema used for older SUSE documentation.

%prep
%autosetup
tar -xf %{SOURCE10}
mv novdoc-20190201/novdoc .
mv novdoc-20190201/catalog.d/novdoc.xml catalog.d/

%build
touch geekodoc/rng/geekodoc5.rnc
# GeekoDoc
./build.sh -vv

# Novdoc
%make_build -C novdoc/rng

%install
docbookxi_rnc="$(xmlcatalog /etc/xml/catalog http://www.docbook.org/xml/5.1/rng/docbookxi.rnc)"
docbookxi_rng="$(xmlcatalog /etc/xml/catalog http://www.docbook.org/xml/5.1/rng/docbookxi.rng)"

install -d %{buildroot}%{_datadir}/xml/{geekodoc/rng/{1_5.1,2_5.2},novdoc/rng} \
           %{buildroot}%{_sysconfdir}/xml/catalog.d

# Fix include for "lonely" schema:
sed -i "s#include \"docbookxi.rnc\"#include \"$docbookxi_rnc\"#" \
    build/geekodoc/rng/1_5.1/geekodoc-v1.rnc
sed -i "s#<include href=\"docbookxi.rng\">#<include href=\"$docbookxi_rng\">#" \
    build/geekodoc/rng/1_5.1/geekodoc-v1.rng

#### Install flat GeekoDoc:
cp -a  build/geekodoc/rng/ %{buildroot}%{_datadir}/xml/geekodoc/

pushd %{buildroot}%{_datadir}/xml/geekodoc/rng
# For compatibility reasons:
ln -s 1_5.1/geekodoc-v1-flat.rnc geekodoc5-flat.rnc
ln -s 1_5.1/geekodoc-v1-flat.rng geekodoc5-flat.rng
  pushd 1_5.1/
    ln -s geekodoc-v1-flat.rnc geekodoc5-flat.rnc
    ln -s geekodoc-v1-flat.rng geekodoc5-flat.rng
  popd
popd

#### Install Novdoc:
cp -a novdoc/dtd %{buildroot}%{_datadir}/xml/novdoc
cp novdoc/rng/novdocxi-flat.rn? novdoc/rng/novell.ent %{buildroot}%{_datadir}/xml/novdoc/rng

#### Install catalogs:
cp catalog.d/* %{buildroot}%{_sysconfdir}/xml/catalog.d/

# Fixup catalog paths
sed -i 's#"\.\./#"%{_datadir}/xml/#' %{buildroot}%{_sysconfdir}/xml/catalog.d/*

# Deal with duplicates
%fdupes  %{buildroot}%{_datadir}/xml/

%post
update-xml-catalog

%postun
update-xml-catalog

%post -n novdoc
update-xml-catalog

if [ ! -f %{_sysconfdir}/xml/suse-catalog.xml -a -x %{_bindir}/edit-xml-catalog ] ; then
    # susexsl entry
    edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
       --del suse_schemas
    edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
       --del novdoc-1.0
fi
exit 0

%postun -n novdoc
update-xml-catalog

%if 0%{with tests}
%check
./tests/run-tests.sh -V xmllint
./tests/run-tests.sh -V jing

echo "### Checking catalog entries..."
for uri in \
   urn:x-suse:rnc:v1:geekodoc-flat \
   urn:x-suse:rng:v1:geekodoc-flat \
   urn:x-suse:rnc:v2:geekodoc-flat \
   urn:x-suse:rng:v2:geekodoc-flat \
   urn:x-suse:rng:geekodoc5-flat.rng \
   urn:x-suse:rng:geekodoc5-flat.rnc \
   https://github.com/openSUSE/geekodoc/raw/master/geekodoc/rng/geekodoc5-flat.rnc \
   https://github.com/openSUSE/geekodoc/raw/master/geekodoc/rng/geekodoc5-flat.rng \
   ;
  do
  xmlcatalog %{buildroot}%{_sysconfdir}/xml/catalog.d/geekodoc.xml $uri || exit $?
done
%endif

%files
%license LICENSE ChangeLog
%config %{_sysconfdir}/xml/catalog.d/geekodoc*.xml
%dir %{_datadir}/xml/geekodoc
%{_datadir}/xml/geekodoc/*
# These files are just build artifacts that need to be excluded:
%exclude %{_datadir}/xml/geekodoc/rng/*/docbook*
%exclude %{_datadir}/xml/geekodoc/rng/*/db*
%exclude %{_datadir}/xml/geekodoc/rng/*/its*
%exclude %{_datadir}/xml/geekodoc/rng/*/trans*
%exclude %{_datadir}/xml/geekodoc/rng/*/xinclude*
%exclude %{_datadir}/xml/geekodoc/rng/*/*.rni
%exclude %{_datadir}/xml/geekodoc/rng/*/geekodoc-v[12].rn[cg]
%exclude %{_datadir}/xml/geekodoc/rng/*/geekodoc5.rnc

%files -n novdoc
%license LICENSE
%config %{_sysconfdir}/xml/catalog.d/novdoc.xml
%dir %{_datadir}/xml/novdoc
%{_datadir}/xml/novdoc/*

%changelog
