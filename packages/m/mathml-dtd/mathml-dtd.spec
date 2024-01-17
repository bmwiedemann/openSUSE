#
# spec file for package mathml-dtd (Version 20031021)
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


Name:           mathml-dtd
BuildRequires:  sgml-skel
Summary:        MathML DTD
Version:        20031021
Release:        204
Group:          Productivity/Publishing/XML
BuildArch:      noarch
Requires:       sgml-skel libxml2
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         sed grep awk
#Provides: 
License:        BSD-3-Clause
Url:            http://www.w3.org/TR/MathML2/
Source0:        http://www.w3.org/Math/DTD/mathml2.tgz
# http://www.w3.org/TR/MathML2/mathml-html.zip
Source1:        copyright-software.html
#Patch: 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Contains the DTD "Mathematical Markup Language" (MathML) Version 2.0,
W3C Recommendation 21 February 2001.



%define sgml_dir %{_datadir}/sgml
%define sgml_var_dir /var/lib/sgml
%define sgml_mod_dir %{sgml_dir}/mathml
%define sgml_mod_dtd_dir %{sgml_mod_dir}/dtd
%define sgml_mod_custom_dir %{sgml_mod_dir}/custom
%define sgml_mod_style_dir %{sgml_mod_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/mathml
%define xml_mod_schema_dir %{xml_mod_dir}/schema
%define xml_mod_dtd_dir %{xml_mod_schema_dir}/dtd
%define xml_mod_custom_dir %{xml_mod_dir}/custom
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml
%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q -n mathml2
cp %{S:1} .
# -c -T
# unzip -q -a %{S:0}
# find -type d | xargs chmod 755

%build
# pushd mathml2
awk '
/ *PUBLIC/{$2=$2;w=$0}
/\.ent/ && w != "" {print w " " $1; w=""}
/SYSTEM.*\.(dtd|mod)/ && w != "" {print w " " $2; w=""}' \
mathml2.dtd mathml2-qname-1.mod >catalog
  sed -e 's:\ \"\([-a-zA-Z0-9/]*\.\(ent\|dtd\|dcl\|mod\)\)\"$: \"%{xml_mod_dtd_dir}/2.0/\1\":g' \
    catalog > CATALOG.mathml-2.0
# popd

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/2.0 \
  $RPM_BUILD_ROOT%{sgml_var_dir} $RPM_BUILD_ROOT%{sgml_dir} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a copyright-software.html $RPM_BUILD_ROOT%{_docdir}/%{name}
%{INSTALL_DATA} CATALOG.* $RPM_BUILD_ROOT%{sgml_var_dir}
cp -a * $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/2.0
# sgml2xmlcat.sh -i catalog -l \
#   -s %{buildroot}%{xml_dir} \
#   -p mathml/dtd/2.0
#
pushd $RPM_BUILD_ROOT
  for c in var/lib/sgml/CATALOG.*; do
    # rm -f ${c##*/} && ln -sf $c ${c##*/}
    rm -f $RPM_BUILD_ROOT/usr/share/sgml/${c##*/} \
      && ln -sf /$c $RPM_BUILD_ROOT/usr/share/sgml/${c##*/}
  done
popd
#
sgml2xmlcat.sh -i CATALOG.mathml-2.0 -c mathml.xml
xmlcatbin=/usr/bin/xmlcatalog
$xmlcatbin --noout --add "system" \
  http://www.w3.org/TR/MathML2/dtd/xhtml-math11-f.dtd \
  "file://%{xml_mod_dtd_dir}/2.0/xhtml-math11-f.dtd" \
  mathml.xml
$xmlcatbin --noout --add "system" \
  http://www.w3.org/TR/MathML2/dtd/mathml2.dtd \
  "file://%{xml_mod_dtd_dir}/2.0/mathml2.dtd" \
  mathml.xml
$xmlcatbin --noout --add "system" \
  http://www.w3.org/TR/MathML2/dtd/mathml2-qname-1.mod \
  "file://%{xml_mod_dtd_dir}/2.0/mathml2-qname-1.mod" \
  mathml.xml
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=etc/xml/mathml.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
# $xmlcatbin --noout --add "delegateSystem" \
#  "http://www.w3.org/TR/xhtml" \
$xmlcatbin --noout --add "delegatePublic" "-//W3C//DTD MathML" \
  "file:///$CATALOG"  %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}
cat_dir=%{buildroot}/etc/xml
%{INSTALL_DIR} $cat_dir
%{INSTALL_DATA} mathml.xml %{FOR_ROOT_CAT} $cat_dir
%define all_cat mathml-2.0

%post
if [ -x %{regcat} ]; then
  for c in  %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_html_ver}; do
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
# %doc copyright-software.html
%config %{sgml_var_dir}/CATALOG.*
%config /etc/xml/*.xml
%doc %{_docdir}/%{name}
%dir %{xml_mod_schema_dir}
%{xml_mod_dtd_dir}
%{sgml_dir}/CATALOG.*
%dir %{xml_mod_dir}
# %{sgml_dir}/W3C/*/*

%changelog
