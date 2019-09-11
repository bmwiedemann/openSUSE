#
# spec file for package html-dtd
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


Name:           html-dtd
BuildRequires:  sgml-skel
Url:            http://www.w3.org/MarkUp/
Provides:       html_dtd
Obsoletes:      html_dtd
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat}
BuildArch:      noarch
Version:        2004.1.26
Release:        0
Summary:        HTML DTDs (Document Type Definitions) and Documents
License:        W3C-19980720
Group:          Productivity/Publishing/HTML/Tools
Source0:        http://www.w3.org/MarkUp/html-spec/html-spec-19950922.tar.gz
# Separate files at: http://www.w3.org/TR/REC-html32.html:
Source1:        html-3.2.tar.gz
# Separate files at: ftp://ftp.cs.tcd.ie/isohtml:
# Source2: iso-html.tar.gz
Source3:        http://www.w3.org/TR/1998/REC-html40-19980424/html40.tgz
Source4:        http://www.w3.org/MarkUp/html40-updates/REC-html40-19980424-errata.html
# the real filename is w/o "1"... :
# Source5: http://www.w3.org/TR/html40/html40.tgz
Source5:        http://www.w3.org/TR/html40/html401.tgz
Source7:        http://www.w3.org/Consortium/Legal/copyright-software.html
Source8:        %{name}-README.SUSE
Source9:        CATALOG.html
Source10:       CATALOG.html-3.2
Source11:       CATALOG.html-4.0
Patch:          html_dtd.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Document Type Definitions (DTDs) for HTML 2.0, HTML 3.2, HTML 4.0, and
HTML 4.01.  This package also contains the documentation (located in
/usr/share/doc/packages/html-dtd).



%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define sgml_dir %{_datadir}/sgml
%define sgml_html_dir %{sgml_dir}/html
%define sgml_html_dtd_dir %{sgml_html_dir}/dtd
%define sgml_var_dir /var/lib/sgml

%prep
%setup -c -T
cp %{S:9} %{S:10} %{S:11} .
mkdir html
(cd html && tar zxf $RPM_SOURCE_DIR/html-spec-19950922.tar.gz)
%setup -T -D -a1
# iso
#%setup -T -D -a2
mkdir html-4.0
(cd html-4.0 && tar zxf $RPM_SOURCE_DIR/html40.tgz \
             && cp -p $RPM_SOURCE_DIR/REC-html40-19980424-errata.html .)
mkdir html-4.01
(cd html-4.01 && tar zxf $RPM_SOURCE_DIR/html401.tgz)
cp -p %{SOURCE7} .
%{INSTALL_DATA} %{SOURCE8} README.SUSE
%patch -p1
find . -type f | xargs chmod 644 
find . -type d | xargs chmod 755

%build
pushd html-4.01
{
  sed -e 's:\ \([a-zA-Z0-9]*\.\(ent\|dtd\)\)$: %{sgml_html_dtd_dir}/4.01/\1:g' \
    HTML4.cat
  echo 'PUBLIC "-//W3C//ENTITIES Latin 1//EN//HTML" "%{sgml_html_dtd_dir}/4.01/HTMLlat1.ent"'
  for d in  '-//W3C//DTD HTML 4.01//EN' \
    '-//W3C//DTD HTML 4.01 Transitional//EN' \
    '-//W3C//DTD HTML 4.01 Frameset//EN'; do
   echo "DTDDECL \"$d\" \"%{sgml_html_dtd_dir}/4.01/HTML4.decl\""
  done
} > ../CATALOG.html-4.01

%install
find . -name '*.gif' | xargs chmod 644
export RPM_BUILD_ROOT
if [ ! "x" = "x$RPM_BUILD_ROOT" ] ; then
   rm -fr $RPM_BUILD_ROOT
   %{INSTALL_DIR} $RPM_BUILD_ROOT
fi
# %{INSTALL_DIR} %{sgml_dir}/iso-html
# %{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/{html,html-3.2,html-4.0,html-4.01}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_html_dtd_dir}/{2.0,3.2,4.0,4.01}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_var_dir}
cp CATALOG.html* $RPM_BUILD_ROOT%{sgml_var_dir}
(cd html && %{INSTALL_DATA} catalog *.dtd html.decl ISOlat1.sgml \
  $RPM_BUILD_ROOT%{sgml_html_dtd_dir}/2.0 \
  && rm -f *.ms *.texi Makefile *.sgm)
(cd html-3.2 \
  && %{INSTALL_DATA} HTML32.cat HTML32.dtd ISOlat1.ent \
  $RPM_BUILD_ROOT%{sgml_html_dtd_dir}/3.2)
(cd html-4.0 \
  && %{INSTALL_DATA} *.cat *.decl *.dtd *.ent \
  $RPM_BUILD_ROOT%{sgml_html_dtd_dir}/4.0)
(cd html-4.01 \
  && %{INSTALL_DATA} *.cat *.decl *.dtd *.ent \
  $RPM_BUILD_ROOT%{sgml_html_dtd_dir}/4.01)
for f in $(find $RPM_BUILD_ROOT%{sgml_html_dtd_dir} -name '*.decl'); do
  pushd ${f%/*} >/dev/null
  file=${f##*/}
  ln -s ${file} ${file/.decl/.dcl}
  popd >/dev/null
done
# useful links
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/IETF/dtd
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/W3C/{dtd,entities}
# %{INSTALL_DIR} %{sgml_dir}/ISO_15xxx/{entities,dtd}
(cd $RPM_BUILD_ROOT%{sgml_dir}/IETF/dtd \
  && ln -sf ../../html/dtd/2.0/html.dtd HTML \
  && ln -sf ../../html/dtd/2.0/html.dtd HTML_2.0 \
  && ln -sf ../../html/dtd/2.0/html.dtd HTML_Level_2 \
  && ln -sf ../../html/dtd/2.0/html.dtd HTML_2.0_Level_2 \
  && ln -sf ../../html/dtd/2.0/html-1.dtd HTML_Level_1 \
  && ln -sf ../../html/dtd/2.0/html-1.dtd HTML_2.0_Level_1 \
  && ln -sf ../../html/dtd/2.0/html-s.dtd HTML_Strict \
  && ln -sf ../../html/dtd/2.0/html-s.dtd HTML_2.0_Strict \
  && ln -sf ../../html/dtd/2.0/html-s.dtd HTML_Strict_Level_2 \
  && ln -sf ../../html/dtd/2.0/html-s.dtd HTML_2.0_Strict_Level_2 \
  && ln -sf ../../html/dtd/2.0/html-1s.dtd HTML_Strict_Level_1 \
  && ln -sf ../../html/dtd/2.0/html-1s.dtd HTML_2.0_Strict_Level_1 )
(cd $RPM_BUILD_ROOT%{sgml_dir}/W3C/dtd \
  && ln -sf ../../html/dtd/3.2/HTML32.dtd HTML_3.2 \
  && ln -sf ../../html/dtd/3.2/HTML32.dtd HTML_3.2_Final )
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f strict.dtd \
               -i '-//W3C//DTD HTML 4.0//EN'
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f loose.dtd \
               -i '-//W3C//DTD HTML 4.0 Transitional//EN'
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f frameset.dtd \
               -i '-//W3C//DTD HTML 4.0 Frameset//EN'
# "Latin 1" and "Latin1"
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLlat1.ent \
               -i '-//W3C//ENTITIES Latin 1//EN//HTML'
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLlat1.ent \
               -i '-//W3C//ENTITIES Latin1//EN//HTML'
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLspecial.ent \
               -i '-//W3C//ENTITIES Special//EN//HTML'
install-dtd.sh -p html/dtd/4.0 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLsymbol.ent \
               -i '-//W3C//ENTITIES Symbols//EN//HTML'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f strict.dtd \
               -i '-//W3C//DTD HTML 4.01//EN'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f loose.dtd \
               -i '-//W3C//DTD HTML 4.01 Transitional//EN'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f frameset.dtd \
               -i '-//W3C//DTD HTML 4.01 Frameset//EN'
# "Latin 1" and "Latin1"
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLlat1.ent \
               -i '-//W3C//ENTITIES Latin 1//EN//HTML'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLlat1.ent \
               -i '-//W3C//ENTITIES Latin1//EN//HTML'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLspecial.ent \
               -i '-//W3C//ENTITIES Special//EN//HTML'
install-dtd.sh -p html/dtd/4.01 -s $RPM_BUILD_ROOT%{sgml_dir} \
               -f HTMLsymbol.ent \
               -i '-//W3C//ENTITIES Symbols//EN//HTML'
%define all_html_ver html html-3.2 html-4.0 html-4.01
pushd $RPM_BUILD_ROOT%{sgml_dir}
  ln -sf ../../../var/lib/sgml/CATALOG.html CATALOG.html
  ln -sf ../../../var/lib/sgml/CATALOG.html-3.2 CATALOG.html-3.2
  ln -sf ../../../var/lib/sgml/CATALOG.html-4.0 CATALOG.html-4.0
  ln -sf ../../../var/lib/sgml/CATALOG.html-4.01 CATALOG.html-4.01
popd
#  && ln -sf ../../../var/lib/sgml/CATALOG.iso-html CATALOG.iso-html

%post
if [ -x %{regcat} ]; then
  for c in  %{all_html_ver}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
exit 0

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_html_ver}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
exit 0

%files
%defattr(-, root, root)
%doc README.SUSE index.html
%doc html
%doc html-3.2
%doc html-4.0
%doc html-4.01
%doc copyright-software.html
# %doc iso-html
%config /var/lib/sgml/CATALOG.*
# %config /var/lib/sgml/CATALOG.iso-html
%dir /usr/share/sgml/W3C
/usr/share/sgml/CATALOG.*
# /usr/share/sgml/CATALOG.iso-html
/usr/share/sgml/IETF
#/usr/share/sgml/ISO_15xxx
%dir /usr/share/sgml/W3C/dtd
/usr/share/sgml/W3C/dtd/*
%dir /usr/share/sgml/W3C/entities
/usr/share/sgml/W3C/entities/*
%dir /usr/share/sgml/html
/usr/share/sgml/html/dtd
# /usr/share/sgml/html-4.0
# /usr/share/sgml/html-4.01
# /usr/share/sgml/html
# /usr/share/sgml/iso-html

%changelog
