#
# spec file for package docbook-simple
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


Name:           docbook-simple
BuildRequires:  libxml2-tools
BuildRequires:  sgml-skel
BuildRequires:  unzip
Summary:        Simple DocBook DTD and Documentation
License:        HPND
Group:          Productivity/Publishing/DocBook
Version:        1.0
Release:        0
BuildArch:      noarch
Requires:       libxml2-tools
Requires:       sgml-skel
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         sed grep awk
#Provides: 
Url:            http://www.oasis-open.org/docbook/xml/simple/
Source0:        docbook-simple-1.0.zip
Source1:        CATALOG.docbook-simple-1.0
#Patch:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the Simple DocBook DTD.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755 -o root -g root
%define sgml_dir %{_datadir}/sgml
%define sgml_var_dir /var/lib/sgml
%define sgml_mod_dir %{sgml_dir}/docbook
%define sgml_mod_dtd_dir %{sgml_mod_dir}/dtd
%define sgml_mod_custom_dir %{sgml_mod_dir}/custom
%define sgml_mod_style_dir %{sgml_mod_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/docbook/custom/simple/%{version}
%define xml_mod_dtd_dir %{xml_mod_dir}/schema/dtd
%define xml_mod_custom_dir %{xml_mod_dir}/custom
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define xml_mod_style_prod_dir %{xml_mod_style_dir}
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml

%prep
echo $RPM_BUILD_ROOT
%setup -c -T
sed 's|@VERSION@|%{version}|
s|@DIR@|%{xml_mod_dtd_dir}|' %{S:1} > CATALOG.%{name}-%{version}
unzip -q -a %{S:0}
find -type d | xargs chmod 755
find -type f | xargs chmod 644

%build
# echo -ne 'PUBLIC "-//OASIS//DTD Simplified DocBook XML V1.0//EN" "sdocbook.dtd"\n'\
# 'SYSTEM "http://www.oasis-open.org/docbook/xml/simple/1.0/sdocbook.dtd" "sdocbook.dtd"' >catalog
# sed -e 's:\ \"\([-a-zA-Z0-9]*\.\(ent\|dtd\|dcl\|mod\)\)\"$: \"%{sgml_inst_dir}/\1\":g' \
#     catalog > CATALOG.%{name}-%{version}
xmlcatbin=/usr/bin/xmlcatalog
CATALOG=docbook-simple.xml
# etc/xml/%{name}.xml
# create the catalogs root and docbook specific
$xmlcatbin --noout --create $CATALOG
$xmlcatbin --noout --add "public" \
  "-//OASIS//DTD Simplified DocBook XML V1.0//EN" \
  "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
$xmlcatbin --noout --add "system" \
  "http://www.oasis-open.org/docbook/xml/simple/1.0/sdocbook.dtd" \
  "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=etc/xml/$CATALOG
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegateSystem" \
  "http://www.oasis-open.org/docbook/xml/simple/" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//OASIS//DTD Simplified DocBook XML" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir} \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir} \
  $RPM_BUILD_ROOT%{sgml_var_dir} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a [a-su-z][!C]* $RPM_BUILD_ROOT%{xml_mod_dtd_dir}
%{INSTALL_DATA} CATALOG.* $RPM_BUILD_ROOT%{sgml_var_dir}
# sgml2xmlcat.sh -i catalog -l -s %{buildroot}/usr/share/sgml \
#   -p %{inst_name}
pushd $RPM_BUILD_ROOT
  for c in var/lib/sgml/CATALOG.*; do
    rm -f %{buildroot}%{sgml_dir}/${c##*/} && ln -sf /$c %{buildroot}%{sgml_dir}/${c##*/}
  done
popd
# pushd $RPM_BUILD_ROOT%{sgml_dir}
#   for c in ../../../var/lib/sgml/CATALOG.*; do
#     rm -f ${c##*/} && ln -sf $c ${c##*/}
#   done
# popd
# sgml2xmlcat.sh -i CATALOG.%{name}-%{version} -c %{name}.xml
cat_dir=%{buildroot}/etc/xml
%{INSTALL_DIR} $cat_dir
# %{INSTALL_DATA} %{name}.xml $RPM_BUILD_ROOT/etc/xml/%{name}.xml
%{INSTALL_DATA} %{FOR_ROOT_CAT} %{name}.xml $cat_dir
%define all_cat %{name}-%{version}

%post
if [ -x %{regcat} ]; then
  for c in  %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
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
# %doc copyright-software.html
%config %{sgml_var_dir}/CATALOG.*
%config %{_sysconfdir}/xml/%{name}.xml
%config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}
%{sgml_dir}/CATALOG.*
%{xml_mod_dtd_dir}
%dir %{xml_dir}/docbook/custom
%dir %{xml_dir}/docbook/custom/simple
%dir %{xml_mod_dir}
%dir %{xml_mod_dir}/schema

%changelog
