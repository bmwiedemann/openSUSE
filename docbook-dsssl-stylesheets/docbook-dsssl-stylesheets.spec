#
# spec file for package docbook-dsssl-stylesheets
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           docbook-dsssl-stylesheets
BuildRequires:  fdupes
BuildRequires:  sgml-skel
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat}
BuildArch:      noarch
Summary:        DSSSL Stylesheets for the DocBook DTD
License:        SUSE-XSL-Lint
Group:          Productivity/Publishing/DocBook
Version:        1.79
Release:        0
Url:            http://sourceforge.net/projects/docbook/
Source0:        http://downloads.sourceforge.net/project/docbook/docbook-dsssl/%{version}/docbook-dsssl-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/project/docbook/docbook-dsssl-doc/%{version}/docbook-dsssl-doc-%{version}.tar.gz
%define db2html dbtohtml.dsl
Source2:        dbtohtml.dsl
%define ld2db ld2db.dsl
Source3:        ld2db.dsl
Source4:        %{name}-README.SUSE
# Source5:      html-dbqanda.dsl
# Source6:      print-dbqanda.dsl
%define pkgdif docbkdsl.dif
Patch0:         docbkdsl.dif
Requires:       docbook_3
Requires:       docbook_4
Obsoletes:      docbkdsl
Provides:       docbkdsl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Use these DSSSL stylesheets to convert DocBook documents into other
formats. "Print" (TeX and RTF) and "online" (HTML) output formats are
available.

The stylesheets are customizable and, within limits, it is possible to
adapt them for your own needs. Numerous native languages are supported.

The authors of these stylesheets do not inlude any new features, but
only fix bugs.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755 -o root -g root
%define sgml_dir %{_datadir}/sgml

%prep
%setup -q -n docbook-dsssl-%{version} -b 1
# cp -p %{S:5} html/dbqanda.dsl
# cp -p %{S:6} print/dbqanda.dsl
cp -p %{_sourcedir}/%{db2html} .
cp -p %{_sourcedir}/%{ld2db} .
cp -p %{S:4} README.SUSE
%patch -P 0 -p 0
#patch -P 1 -p 1 -b .cvs

%build

%install
doc_dir=%{buildroot}/%{_defaultdocdir}/%{name}
sgml_dir=%{buildroot}/%{_datadir}/sgml
sgml_dir_db=%{buildroot}/%{_datadir}/sgml/docbook
sgml_dir_db_sty=%{buildroot}/%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
%{INSTALL_DIR} $sgml_dir_db_sty
cp -a [a-z]* $sgml_dir_db_sty
cp -a VERSION $sgml_dir_db_sty
%{INSTALL_DIR} $doc_dir
%{INSTALL_DIR} $sgml_dir/Norman_Walsh/document
%{INSTALL_DIR} $sgml_dir/Norman_Walsh/dtd
%{INSTALL_DIR} $sgml_dir/IDN_nwalsh.com/dtd
sed -e 's:^  \([a-z]\):  %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/\1:' \
    -e 's:^SGMLDECL ":SGMLDECL "%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/:' \
    < catalog > CATALOG.docbkdsl
# echo -e "\
# CATALOG \"/var/lib/sgml/CATALOG.iso_ent\"\n\
# CATALOG \"/var/lib/sgml/CATALOG.docbk31\"\n\
# CATALOG \"/var/lib/sgml/CATALOG.docbk30\"\n\
# CATALOG \"/var/lib/sgml/CATALOG.docbk41\"\n"\
#     >> docbook/CATALOG.docbkdsl
%{INSTALL_DATA} CATALOG.docbkdsl $sgml_dir/CATALOG.%{name}
pushd $sgml_dir
ln -sf CATALOG.%{name} CATALOG.docbkdsl
popd
# documentation
# pushd docbook
  for f in README BUGS TODO WhatsNew; do
    [ -f $f ] && %{INSTALL_DATA} $f $doc_dir/$f
  done
# popd
# misc
%{INSTALL_DIR} $sgml_dir_db_sty/misc
cp %{db2html} $sgml_dir_db_sty/misc
cp %{ld2db} $sgml_dir_db_sty/misc
# cp index.html $doc_dir
cp -p README.SUSE $doc_dir
pushd $sgml_dir/docbook
  rm -f dsssl-stylesheets
  ln -sf dsssl-stylesheets-%{version} dsssl-stylesheets
  # remove this when docbook-toys is updated
  # 2001-11-29 10:56:56 CET -ke-
  rm -f %{name}
  ln -sf dsssl-stylesheets-%{version} %{name}
popd
%fdupes %{buildroot}%{_datadir}

%post
# remove empty dirs if present (from ghost; pre 8.0)
# also remove dangling symlinks
D=usr/share/sgml
rmdir $D/docbkdsl >/dev/null 2>&1 || :
test -L $D/docbkdsl -a ! -e $D/docbkdsl && rm -f $D/docbkdsl
D=var/lib/sgml
rmdir $D/docbkdsl >/dev/null 2>&1 || :
test -L $D/docbkdsl -a ! -e $D/docbkdsl && rm -f $D/docbkdsl
D=usr/share/sgml/docbook
rmdir $D/%{name} >/dev/null 2>&1 || :
test -L $D/%{name} -a ! -e $D/%{name} && rm -f $D/%{name}
# register catalog
if [ -x %{regcat} ]; then
  for c in  %{name}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\"\?$" /etc/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
exit 0

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{name}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1
  done
fi
exit 0

%files
%defattr(-, root, root)
%{_datadir}/sgml/CATALOG.*
%{_datadir}/sgml/docbook/dsssl-stylesheets
%{_datadir}/sgml/docbook/%{name}
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
%{_defaultdocdir}/%{name}

%changelog
