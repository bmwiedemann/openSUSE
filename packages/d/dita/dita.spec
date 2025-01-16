#
# spec file for package dita
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


Name:           dita
BuildRequires:  sgml-skel
BuildRequires:  unzip
URL:            http://www.oasis-open.org/committees/dita/
License:        SUSE-Oasis-Specification-Notice
Group:          Productivity/Publishing/XML
Requires:       sgml-skel
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         awk
PreReq:         coreutils
PreReq:         grep
PreReq:         sed
Summary:        OASIS Darwin Information Typing Architecture (DITA)
Version:        1.1
Release:        0
Source0:        http://www.oasis-open.org/committees/download.php/24944/dita1.1.zip
Source1:        http://www.oasis-open.org/committees/download.php/15396/dita-document-definitions-1.0.1.zip
# Patch:          dita-catalog.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the DITA specifications, DTDs, and schemas.



%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755
%define sgml_dir %{_datadir}/sgml
%define sgml_pack_dir %{sgml_dir}/%{name}
%define sgml_pack_dtd_dir %{sgml_pack_dir}/dtd
%define sgml_pack_custom_dir %{sgml_pack_dir}/custom
%define sgml_pack_style_dir %{sgml_pack_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_pack_dir %{xml_dir}/dita
%define xml_pack_dtd_dir %{xml_pack_dir}/schema/dtd
%define xml_pack_rng_dir %{xml_pack_dir}/schema/rng
%define xml_pack_xsd_dir %{xml_pack_dir}/schema/xsd
%define xml_pack_custom_dir %{xml_pack_dir}/custom
%define xml_pack_style_dir %{xml_pack_dir}/stylesheet
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml

%prep
%setup -c -n %{name}1.1
source="archspec-source.zip langspec-source.zip"
zip="archspec-html.zip langspec-html.zip ditadtd.zip ditaschema.zip"
for z in $zip; do
  unzip -a $z
done
unzip -a -o %{S:1}
# %%patch -p 1
chmod -R a+rX,g-w,o-w .
find . -type f | xargs chmod a-x

%build
xmlcatbin=/usr/bin/xmlcatalog
$xmlcatbin --create --noout $CATALOG
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=etc/xml/$CATALOG
cat42=%{xml_pack_dtd_dir}/1.1/catalog-dita.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
for s in \
  "-//OASIS//DTD DITA" \
  "-//OASIS//ELEMENTS DITA Concept//EN" \
  "-//OASIS//ENTITIES DITA Topic Class//EN" \
  "-//OASIS//ELEMENTS DITA" \
  "-//OASIS//ENTITIES DITA"
do
  $xmlcatbin --noout --add "delegatePublic" "$s" \
    "file://$cat42" %{FOR_ROOT_CAT}.tmp
done
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
#%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_config_dir}
#%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_config_dir}
%{INSTALL_DIR} $RPM_BUILD_ROOT{%{xml_pack_xsd_dir},%{xml_pack_dtd_dir}}/1.1
# catalog-dita.txt
# catalog-dita.xml
cp dtd/* $RPM_BUILD_ROOT%{xml_pack_dtd_dir}/1.1
# DTDDECL "-//OASIS//DTD DocBook XML V4.1.2//EN" /usr/share/sgml/opensp/xml.dcl
{
  echo OVERRIDE YES
  grep  '\.dtd\"' dtd/catalog-dita.txt \
    | awk -F\" '{printf "DTDDECL \"%s\" /usr/share/sgml/opensp/xml.dcl\n", $2}'
  cat dtd/catalog-dita.txt
} > $RPM_BUILD_ROOT%{xml_pack_dtd_dir}/1.1/%{name}.cat
ln -s %{xml_pack_dtd_dir}/1.1/catalog-dita.xml \
  $RPM_BUILD_ROOT%{xml_pack_dtd_dir}/1.1/catalog.xml
cp schema/* $RPM_BUILD_ROOT%{xml_pack_xsd_dir}/1.1
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_pack_dtd_dir}
ln -s %{xml_pack_dtd_dir}/1.1 \
  $RPM_BUILD_ROOT%{sgml_pack_dtd_dir}/1.1
cat_dir=%{buildroot}/etc/xml
%{INSTALL_DIR} $cat_dir
%{INSTALL_DATA} %{FOR_ROOT_CAT} $cat_dir

%post
if [ -x %{regcat} ]; then
  %{regcat} -a %{xml_pack_dtd_dir}/1.1/%{name}.cat \
    >/dev/null 2>&1 || true
fi
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}
exit 0

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in %{xml_pack_dtd_dir}/1.1/%{name}.cat; do
    %{regcat} -r $c \
      >/dev/null 2>&1 || true
  done
fi
# remove entries only on removal of file
if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi
exit 0

%files
%defattr(-, root, root)
%doc archspec langspec
# %config %{sgml_config_dir}/CATALOG.*
# %doc README.SuSE
# %{sgml_dir}/CATALOG.*
%{xml_pack_dir}
%{sgml_pack_dir}
%config %{xml_sysconf_dir}/%{FOR_ROOT_CAT}

%changelog
