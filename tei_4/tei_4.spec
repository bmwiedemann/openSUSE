#
# spec file for package tei_4 (Version 2006.8.14)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           tei_4
BuildRequires:  sgml-skel
License:        BSD-3-Clause
Group:          Productivity/Publishing/SGML
AutoReqProv:    on
Summary:        TEI 4 DTD (SGML and XML)
Version:        2006.8.14
Release:        1
Source0:        http://www.tei-c.org/Guidelines2/p4html.tar.gz
# # Also in p4html.tar.gz:
# Source1: http://www.tei-c.org/P4X/DTD/dtd.zip
Source2:        http://www.tei-c.org/Schemas/RelaxNG/P4X/teirng.zip
# Source1: tei4sgml.dec
# Source3: teicatalog.xml
# Patch: tei_4-catalog.diff
Url:            http://www.tei-c.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         /bin/touch /usr/bin/install
PreReq:         sed grep awk zlib
Requires:       iso_ent xmlcharent
Requires:       sgml-skel libxml2

%description
If you want to mark up literary and linguistic texts for online
research or for printing, the DTD of the TEI (Text Encoding Initiative)
is the way to go. The TEI DTD comes with special markup elements and
attributes for poems, plays, and novels as well as for critical
apparatus, taxonomy systems, etc.



Authors:
--------
    C M Sperberg-McQueen
    Lou Burnard
    Syd Bauman
    Steven DeRose
    Sebastian Rahtz

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
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
%setup -q -n TEI_P4
chmod -R a+rX,g-w,o-w,u+w .
find -type d | xargs chmod 755
# %patch0 -p 1

%build
# Prep XML catalog fragment
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
xmlcatbin=/usr/bin/xmlcatalog
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
   rm -fr $RPM_BUILD_ROOT
   %{INSTALL_DIR} $RPM_BUILD_ROOT
fi
# TEI
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_tei_dtd4_dir}
# %{INSTALL_DATA} tei*.{dec,dtd,ent} $RPM_BUILD_ROOT%{sgml_tei_dir}
%{INSTALL_DATA} DTD/* $RPM_BUILD_ROOT%{sgml_tei_dtd4_dir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -a . $RPM_BUILD_ROOT%{_docdir}/%{name}/html
rm -fr $RPM_BUILD_ROOT%{_docdir}/%{name}/html/DTD
ln -sf %{sgml_tei_dtd4_dir} $RPM_BUILD_ROOT%{_docdir}/%{name}/html/DTD
# normalize catalog and remove duplicates
awk '/^ *PUBLIC/ {print f;f=$0;}; /^[[:lower:]].*/ {f=f " " $0}' \
  DTD/catalog.tei \
  | sed 's/^ *//;s/ [ ]\+/ /;s:&DTDpath;:%{sgml_tei_dtd4_dir}/:' \
  | grep -v wdgis2.ent \
  | sort -u > $RPM_BUILD_ROOT%{sgml_tei_dtd4_dir}/catalog.tei
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_config_dir}
cp $RPM_BUILD_ROOT%{sgml_tei_dtd4_dir}/catalog.tei \
  $RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.tei_4
{ echo "CATALOG %{sgml_config_dir}/CATALOG.iso_ent";
  echo "OVERRIDE YES";
  echo "DTDDECL \"-//TEI P4//DTD Main DTD Driver File//EN\" %{sgml_tei_dtd4_dir}/teisgml.dec";
  echo "CATALOG %{sgml_config_dir}/CATALOG.tei_4";
} >$RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.tei_4sgml
{ echo "-- CATALOG %{sgml_config_dir}/CATALOG.db41xml --";
  echo "OVERRIDE YES";
  echo "-- DTDDECL \"-//TEI P4//DTD Main DTD Driver File XML//EN\" %{sgml_tei_dtd4_dir}/teilitex.dec --";
  echo "SGMLDECL %{sgml_tei_dtd4_dir}/teilitex.dec";
  echo "CATALOG %{sgml_config_dir}/CATALOG.tei_4";
} >$RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.tei_4xml
pushd $RPM_BUILD_ROOT%{sgml_dir}
  for c in CATALOG.*; do
    ln -sf ../../..%{sgml_config_dir}/$c .
    # ln -sf %{sgml_config_dir}/$c .
  done
popd
# parse-sgml-catalog.sh $RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.tei_4 \
#   | sort | uniq > CATALOG.norm
sgml2xmlcat.sh -i $RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.tei_4 \
  -l -s '%{buildroot}/usr/share/sgml' \
  -p $(echo %{sgml_tei_dtd4_dir} | sed 's|/usr/share/sgml/||') \
  -x tei-xmlcat
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_sysconf_dir}
sed "s|http://www.tei-c.org/Guidelines/DTD|file://%{sgml_tei_dtd4_dir}|" \
  DTD/teicatalog.xml \
  >$RPM_BUILD_ROOT%{_sysconfdir}/xml/tei_4.xml
for f in $(sed -n 's:.*uri=\"\(.*\)\".*:\1:p' DTD/teicatalog.xml); do
  g=${f##*/}
  xmlcatalog --noout --add "system" "$f" "file://%{sgml_tei_dtd4_dir}/$g" \
    $RPM_BUILD_ROOT%{_sysconfdir}/xml/tei_4.xml
done
mkdir -p ${RPM_BUILD_ROOT}%{xml_sysconf_dir}
install -m644 %{FOR_ROOT_CAT} ${RPM_BUILD_ROOT}%{xml_sysconf_dir}
#
%define all_cat %{name} tei_4sgml

%post
if [ -x %{regcat} ]; then
  for c in  %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
xmlcatbin=usr/bin/xmlcatalog
%if %suse_version < 810
  # autobuild on 8.0 does not install it early enough
  [ -x $xmlcatbin ] || {
    echo "warning: $xmlcatbin does not exist"
    echo "create etc/xml/catalog etc. manually"
    exit 0
  }
%endif
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
# remove entries only on removal of file
if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_docdir}/%{name}
# %doc fpi/teifpi.doc fpi/teifpi.html
%config %{xml_sysconf_dir}/%{FOR_ROOT_CAT}
%config %{xml_sysconf_dir}/tei_4.xml
%{sgml_tei_dtd4_dir}
%config %{sgml_config_dir}/CATALOG.tei*
%{sgml_dir}/CATALOG.tei*
%{sgml_dir}/TEI_P4
%dir %{sgml_tei_dir}
%dir %{sgml_tei_dtd_dir}

%changelog
