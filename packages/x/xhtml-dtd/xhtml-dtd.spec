#
# spec file for package xhtml-dtd
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


Name:           xhtml-dtd
BuildRequires:  sgml-skel
Summary:        XHTML DTDs (Document Type Definitions)
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/HTML/Tools
Version:        2006.8.16
Release:        0
BuildArch:      noarch
Requires:       libxml2
BuildRequires:  sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Requires:       sgml-skel >= 0.7
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog
URL:            http://www.w3.org/MarkUp/
Source0:        http://www.w3.org/Consortium/Legal/copyright-software.html
Source1:        http://www.w3.org/TR/xhtml1/xhtml1.tgz
Source2:        http://www.w3.org/TR/2001/REC-xhtml11-20010531/xhtml11.tgz
Source3:        http://www.w3.org/TR/2000/REC-xhtml-basic-20001219/xhtml-basic.tgz
Source4:        http://www.w3.org/TR/2001/REC-xhtml-modularization-20010410/xhtml-modularization.tgz
# http://www.w3.org/TR/2001/REC-MathML2-20010221/REC-MathML2-20010221.zip
# http://www.w3.org/TR/2002/CR-SVG11-20020430/CR-SVG11-20020430.zip
Source5:        http://www.w3.org/TR/2002/WD-XHTMLplusMathMLplusSVG-20020809/XHTMLplusMathMLplusSVG.tgz
Source6:        CATALOG.xhtml-1
Source7:        CATALOG.xhtml-1-modularization
Source8:        CATALOG.xhtml-1.1
Source9:        CATALOG.xhtml-basic10
Source10:       CATALOG.xhtml-math-svg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Document Type Definitions (DTDs) for XHTML 1/1.1 and some modularized
variants.



%define sgml_dir %{_datadir}/sgml
%define sgml_var_dir /var/lib/sgml
%define sgml_mod_dir %{sgml_dir}/xhtml
%define sgml_mod_dtd_dir %{sgml_mod_dir}/dtd
%define sgml_mod_custom_dir %{sgml_mod_dir}/custom
%define sgml_mod_style_dir %{sgml_mod_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/xhtml
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
%setup -q -c -T
cp -p %{SOURCE0} .
cp %{S:6} %{S:7} %{S:8} %{S:9} %{S:10} .
%setup -q -D -T -a1 -a2 -a3 -a4 -a5
find -type d | xargs chmod 755

%build
# pushd xhtml1/DTD
#   cp xhtml.soc xhtml.soc.orig
#   # also add PUBLIC  "-//W3C//DTD XHTML 1.0//EN" "xhtml1-strict.dtd"
#   sed -e '/Strict/{p;s/ Strict//;}' xhtml.soc.orig > xhtml.soc
#   sed -e 's:\ \"\([-a-zA-Z0-9]*\.\(ent\|dtd\|dcl\)\)\"$: \"%{sgml_dir}/xhtml/xhtml-1.0/DTD/\1\":g' \
#     xhtml.soc | sed 's:^\(SGMLDECL.*\):-- \1 --:' > CATALOG.xhtml-1
# popd
# pushd REC-xhtml-basic-20001219
#   # cp xhtml-basic10.cat xhtml-basic10.cat.orig
#   sed -e 's:\ \"\([-a-zA-Z0-9]*\.\(ent\|dtd\|dcl\|mod\)\)\"$: \"%{sgml_dir}/xhtml/xhtml-basic10/\1\":g' \
#     xhtml-basic10.cat  | sed 's:^\(SGMLDECL.*\):-- \1 --:' > CATALOG.xhtml-basic10
# popd
# pushd xhtml-modularization/DTD
#   # create dummy files
#   touch xhtml-redecl-1.mod xhtml-ruby-1.mod xhtml11-arch.dtd \
#     xhtml-legacy-redecl-1.mod
#   # cp xhtml.cat xhtml.cat.orig
#   sed -e 's:\ \"\([-a-zA-Z0-9]*\.\(ent\|dtd\|dcl\|mod\)\)\"$: \"%{sgml_dir}/xhtml/xhtml-1-modularization/DTD/\1\":g' \
#     xhtml.cat | sed 's:^\(SGMLDECL.*\):-- \1 --:' > CATALOG.xhtml-1-modularization
# popd
# pushd xhtml11*/DTD
#   # cp xhtml11.cat xhtml.cat.orig
#   sed -e 's:\ \"\([-a-zA-Z0-9]*\.\(ent\|dtd\|dcl\|mod\)\)\"$: \"%{sgml_dir}/xhtml/xhtml-1.1/DTD/\1\":g' \
#     xhtml11.cat | sed 's:^\(SGMLDECL.*\):-- \1 --:' > CATALOG.xhtml-1.1
# popd

%install
if [ ! "x" = "x$RPM_BUILD_ROOT" ] ; then
   rm -fr $RPM_BUILD_ROOT
   %{INSTALL_DIR} $RPM_BUILD_ROOT
fi
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_mod_dtd_dir} \
  $RPM_BUILD_ROOT%{sgml_var_dir}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/{1.0,1.1} \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/{1.0-basic,1.0-modularization} \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.1-math-svg \
  $RPM_BUILD_ROOT%{sgml_var_dir} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1
### copyright-software.html
%{INSTALL_DATA} copyright-software.html \
  $RPM_BUILD_ROOT%{_docdir}/%{name}/copyright-software.html
### xhtml1
cp -a xhtml1/DTD/* $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.0
cp -a xhtml1/* $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1
rm -fr $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1/DTD
ln -sf %{xml_mod_dtd_dir}/1.0 $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1/DTD
# %{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/xhtml/xhtml-basic10
cp -a REC-xhtml-basic-20001219/*{mod,dtd,ent,dcl,cat} \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.0-basic
cp -a REC-xhtml-basic-20001219 $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/REC-xhtml-basic-20001219/*{mod,dtd,ent,dcl,cat}
for f in $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.0-basic/*{mod,dtd,ent,dcl,cat}; do
  ln -sf ${f#$RPM_BUILD_ROOT} \
    $RPM_BUILD_ROOT%{_docdir}/%{name}/REC-xhtml-basic-20001219/
done
# %{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/xhtml/xhtml-1-modularization \
%{INSTALL_DIR} $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1-modularization
cp -a xhtml-modularization/DTD/* \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.0-modularization
cp -a xhtml-modularization/* \
  $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1-modularization
rm -fr $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1-modularization/DTD
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1-modularization/*ps
ln -sf %{xml_mod_dtd_dir}/1.0-modularization \
  $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml1-modularization
cp -a WD-XHTMLplusMathMLplusSVG-20020809/DTD/* \
  $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.1-math-svg
### ***************************
### Move doc stuff to /usr/share/doc/packages
### ***************************
# 1.1
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.1 \
  $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml-1.1
cp -a xhtml11-20010531/DTD/* $RPM_BUILD_ROOT%{xml_mod_dtd_dir}/1.1
cp -a xhtml11-20010531/* $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml-1.1
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml-1.1/{*.ps,DTD}
ln -sf %{xml_mod_dtd_dir}/1.1 $RPM_BUILD_ROOT%{_docdir}/%{name}/xhtml-1.1
%{INSTALL_DATA} CATALOG.xhtml-* \
  $RPM_BUILD_ROOT%{sgml_var_dir}
pushd $RPM_BUILD_ROOT%{sgml_dir}
  for c in ../../../var/lib/sgml/CATALOG.xhtml-*; do
    rm -f ${c##*/} && ln -sf $c ${c##*/}
  done
popd
%define _buildshell /bin/bash
parse_cat() {
  sed -n -e '
/^\(OVERRIDE\|SGMLDECL\)/d
/^ /d
/^$/d
/^--/d
s:^\([a-z]*\).*"\(.*\)".*"\(.*\)":\1|\2|\3:p' $1
}
parse_cat xhtml1/DTD/xhtml.soc | while read line; do
  OLDIFS=$IFS; IFS='|'
  set -- $(echo "$line")
  IFS=$OLDIFS
  # echo $3 $2 $1
  install-dtd.sh -p xhtml/schema/dtd/1.0 -s $RPM_BUILD_ROOT%{xml_dir} \
    -f "$3" -i "$2" || exit 1
done
# done < <(../../parse_cat xhtml1/DTD/xhtml.soc)
parse_cat REC-xhtml-basic/*.cat | while read line; do
  OLDIFS=$IFS; IFS='|'
  set -- $(echo "$line")
  IFS=$OLDIFS
  install-dtd.sh -p xhtml/schema/dtd/1.0-basic -s $RPM_BUILD_ROOT%{xml_dir} \
    -f "$3" -i "$2" || exit 1
done
parse_cat xhtml-modularization/DTD/xhtml.cat | while read line; do
  OLDIFS=$IFS; IFS='|'
  set -- $(echo "$line")
  IFS=$OLDIFS
  case $3 in
	xhtml-redecl-1.mod|xhtml-ruby-1.mod|xhtml11-arch.dtd|xhtml-legacy-redecl-1.mod) continue ;;
  esac
  install-dtd.sh -p xhtml/schema/dtd/1.0-modularization -s $RPM_BUILD_ROOT%{xml_dir} \
    -f "$3" -i "$2" || exit 1
done
parse_cat xhtml11-20010531/DTD/xhtml11.cat | while read line; do
  OLDIFS=$IFS; IFS='|'
  set -- $(echo "$line")
  IFS=$OLDIFS
  install-dtd.sh -p xhtml/schema/dtd/1.1 -s $RPM_BUILD_ROOT%{xml_dir} \
    -f "$3" -i "$2" || exit 1
done
{
  for c in $(find . -name 'CATALOG.*'); do
    cat $c
  done
} | tr '\t' ' '| tr -s ' ' | sort | uniq >tmp.cat
sgml2xmlcat.sh -i tmp.cat -c xhtml.xml
grep ^PUBLIC tmp.cat \
  | awk -F/ '{gsub(/"/,""); l=NF-1;printf "%s %s\n", $NF, $l}' \
  | while read file version ; do
  # version=$2; file=$1
  case "$version" in
    1.1-math-svg)
      id="http://www.w3.org/2002/04/xhtml-math-svg/$file"
      ;;
    1.0-modularization)
      id="http://www.w3.org/TR/xhtml-modularization/DTD/$file"
      ;;
    1.0-basic)
      id="http://www.w3.org/TR/xhtml-basic/$file"
      ;;
    1.0)
      id="http://www.w3.org/TR/xhtml1/DTD/$file"
      ;;
    1.1)
      id="http://www.w3.org/TR/xhtml11/DTD/$file"
      ;;
  esac
  xmlcatalog --noout --add "system" "$id" \
    "file:///usr/share/xml/xhtml/schema/dtd/$version/$file" xhtml.xml
done
rm -f tmp.cat
%{INSTALL_DIR} $RPM_BUILD_ROOT/etc/xml/catalog.d
%{INSTALL_DATA} xhtml.xml $RPM_BUILD_ROOT/etc/xml/catalog.d/xhtml.xml

%define all_cat xhtml-1 xhtml-basic10 xhtml-1-modularization xhtml-1.1

%post
if [ -x %{regcat} ]; then
  for c in %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
update-xml-catalog

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in %{all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
update-xml-catalog

%clean
rm -fr $RPM_BUILD_ROOT
# %config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%config %{sgml_var_dir}/CATALOG.*
%config /etc/xml/catalog.d/xhtml.xml
%{sgml_dir}/*
%dir %{xml_mod_dir}
%dir %{xml_mod_schema_dir}
%{xml_mod_dtd_dir}
%{xml_dir}/W3C
# spec file ends here

%changelog
