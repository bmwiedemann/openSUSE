#
# spec file for package tei_4
#
# Copyright (c) 2024 SUSE LLC
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


%define regcat %{_bindir}/sgml-register-catalog
Name:           tei_4
Version:        2006.8.14
Release:        0
Summary:        TEI 4 DTD (SGML and XML)
License:        BSD-3-Clause
Group:          Productivity/Publishing/SGML
URL:            https://www.tei-c.org/
Source0:        p4html.tar.gz
# Source1: http://www.tei-c.org/P4X/DTD/dtd.zip
# Source1: tei4sgml.dec
# # Also in p4html.tar.gz:
Source2:        teirng.zip
# Source3: teicatalog.xml
BuildRequires:  sgml-skel
Requires:       iso_ent
Requires:       libxml2
Requires:       sgml-skel
Requires:       xmlcharent
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{_bindir}/edit-xml-catalog
PreReq:         %{_bindir}/install
PreReq:         %{_bindir}/xmlcatalog
PreReq:         %{regcat}
PreReq:         /bin/touch
PreReq:         awk
PreReq:         grep
PreReq:         sed
PreReq:         zlib
BuildArch:      noarch

%description
If you want to mark up literary and linguistic texts for online
research or for printing, the DTD of the TEI (Text Encoding Initiative)
is the way to go. The TEI DTD comes with special markup elements and
attributes for poems, plays, and novels as well as for critical
apparatus, taxonomy systems, etc.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755
%define sgml_config_dir %{_localstatedir}/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir %{_localstatedir}/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml
%define sgml_dir %{_datadir}/sgml
%define sgml_tei_dir %{sgml_dir}/tei
%define sgml_tei_dtd_dir %{sgml_tei_dir}/dtd
%define sgml_tei_dtd4_dir %{sgml_tei_dtd_dir}/4.0
%define sgml_tei_custom_dir %{sgml_tei_dir}/custom
%define sgml_tei_style_dir %{sgml_tei_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_tei_dir %{xml_dir}/docbook
%define xml_tei_dtd_dir %{xml_tei_dir}/dtd
%define xml_tei_dtd4_dir %{xml_tei_dtd_dir}/4.0
%define xml_tei_custom_dir %{xml_tei_dir}/custom
%define xml_tei_style_dir %{xml_tei_dir}/stylesheet

%prep
%autosetup -p1 -n TEI_P4
chmod -R a+rX,g-w,o-w,u+w .
find -type d | xargs chmod 755

%build
# Prep XML catalog fragment
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
xmlcatbin=%{_bindir}/xmlcatalog
# build root catalog fragment
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
CATALOG=etc/xml/%{name}.xml
xmlcatalog --noout --add "delegatePublic" \
    "-//TEI P4//DTD" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
xmlcatalog --noout --add "delegatePublic" \
    "-//TEI P4//ELEMENTS" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
xmlcatalog --noout --add "delegatePublic" \
    "-//TEI P4//ENTITIES" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
xmlcatalog --noout --add "delegateSystem" \
    "http://www.tei-c.org/Guidelines/DTD/" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
xmlcatalog --noout --add "delegateURI" \
    "http://www.tei-c.org/Guidelines/DTD/" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
if [ ! "x" = "x$RPM_BUILD_ROOT" ] ; then
   %{INSTALL_DIR} %{buildroot}
fi
# TEI
%{INSTALL_DIR} %{buildroot}%{sgml_tei_dtd4_dir}
# %%{INSTALL_DATA} tei*.{dec,dtd,ent} $RPM_BUILD_ROOT%%{sgml_tei_dir}
%{INSTALL_DATA} DTD/* %{buildroot}%{sgml_tei_dtd4_dir}
mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a . %{buildroot}%{_docdir}/%{name}/html
rm -fr %{buildroot}%{_docdir}/%{name}/html/DTD
ln -sf %{sgml_tei_dtd4_dir} %{buildroot}%{_docdir}/%{name}/html/DTD
# normalize catalog and remove duplicates
awk '/^ *PUBLIC/ {print f;f=$0;}; /^[[:lower:]].*/ {f=f " " $0}' \
  DTD/catalog.tei \
  | sed 's/^ *//;s/ [ ]\+/ /;s:&DTDpath;:%{sgml_tei_dtd4_dir}/:' \
  | grep -v wdgis2.ent \
  | sort -u > %{buildroot}%{sgml_tei_dtd4_dir}/catalog.tei
%{INSTALL_DIR} %{buildroot}%{sgml_config_dir}
cp %{buildroot}%{sgml_tei_dtd4_dir}/catalog.tei \
  %{buildroot}%{sgml_config_dir}/CATALOG.tei_4
{ echo "CATALOG %{sgml_config_dir}/CATALOG.iso_ent";
  echo "OVERRIDE YES";
  echo "DTDDECL \"-//TEI P4//DTD Main DTD Driver File//EN\" %{sgml_tei_dtd4_dir}/teisgml.dec";
  echo "CATALOG %{sgml_config_dir}/CATALOG.tei_4";
} >%{buildroot}%{sgml_config_dir}/CATALOG.tei_4sgml
{ echo "-- CATALOG %{sgml_config_dir}/CATALOG.db41xml --";
  echo "OVERRIDE YES";
  echo "-- DTDDECL \"-//TEI P4//DTD Main DTD Driver File XML//EN\" %{sgml_tei_dtd4_dir}/teilitex.dec --";
  echo "SGMLDECL %{sgml_tei_dtd4_dir}/teilitex.dec";
  echo "CATALOG %{sgml_config_dir}/CATALOG.tei_4";
} >%{buildroot}%{sgml_config_dir}/CATALOG.tei_4xml
pushd %{buildroot}%{sgml_dir}
  for c in CATALOG.*; do
    ln -sf ../../..%{sgml_config_dir}/$c .
    # ln -sf %%{sgml_config_dir}/$c .
  done
popd
# parse-sgml-catalog.sh $RPM_BUILD_ROOT%%{sgml_config_dir}/CATALOG.tei_4 \
#   | sort | uniq > CATALOG.norm
sgml2xmlcat.sh -i %{buildroot}%{sgml_config_dir}/CATALOG.tei_4 \
  -l -s '%{buildroot}%{_datadir}/sgml' \
  -p $(echo %{sgml_tei_dtd4_dir} | sed 's|%{_datadir}/sgml/||') \
  -x tei-xmlcat
%{INSTALL_DIR} %{buildroot}%{xml_sysconf_dir}
sed "s|http://www.tei-c.org/Guidelines/DTD|file://%{sgml_tei_dtd4_dir}|" \
  DTD/teicatalog.xml \
  >%{buildroot}%{_sysconfdir}/xml/tei_4.xml
for f in $(sed -n 's:.*uri=\"\(.*\)\".*:\1:p' DTD/teicatalog.xml); do
  g=${f##*/}
  xmlcatalog --noout --add "system" "$f" "file://%{sgml_tei_dtd4_dir}/$g" \
    %{buildroot}%{_sysconfdir}/xml/tei_4.xml
done
mkdir -p %{buildroot}%{xml_sysconf_dir}
install -m644 %{FOR_ROOT_CAT} %{buildroot}%{xml_sysconf_dir}
#
%define all_cat %{name} tei_4sgml

%post
if [ -x %{regcat} ]; then
  for c in  %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" %{_sysconfdir}/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
xmlcatbin=usr/bin/xmlcatalog
edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
  --add %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
# remove entries only on removal of file
if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x %{_bindir}/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi

%files
%{_docdir}/%{name}
%config %{xml_sysconf_dir}/%{FOR_ROOT_CAT}
%config %{xml_sysconf_dir}/tei_4.xml
%{sgml_tei_dtd4_dir}
%config %{sgml_config_dir}/CATALOG.tei*
%{sgml_dir}/CATALOG.tei*
%{sgml_dir}/TEI_P4
%dir %{sgml_tei_dir}
%dir %{sgml_tei_dtd_dir}

%changelog
