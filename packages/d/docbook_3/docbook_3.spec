#
# spec file for package docbook_3
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


%define regcat %{_bindir}/sgml-register-catalog
### Version macros are defined so I can use them below,
### don't use macros for "Source:" and "Patch:" values.
%define dtd30 docbk30.zip
%define dtd31 docbk31.zip
# Docu now to be found at http://www.oasis-open.org/docbook/documentation/
%define docu dbhset.tar.gz
%define db3xver 3.1.7
%define db3x db3x317.zip
%define db3sxver 3.1.7.1
%define sdb sdb3171.zip
%define  pkgdif docbk30.dif
Name:           docbook_3
Version:        3.1
Release:        0
Summary:        DocBook DTD 3.x
License:        BSD-3-Clause AND MIT
Group:          Productivity/Publishing/DocBook
URL:            https://www.oasis-open.org/docbook/
Source0:        https://docbook.org/sgml/3.0/docbk30.zip
Source1:        https://docbook.org/sgml/3.1/docbk31.zip
# at ora, no longer available. 2023-05-22
# Source2:        http://www.ora.com/davenport/dbdoc/dbhset.tar.gz
Source2:        dbhset.tar.gz
# URL no longer available 2023-05-23
# Source3:        http://nwalsh.com/docbook/xml/3.1.7/db3x317.zip
Source3:        db3x317.zip
# URL no longer available 2023-05-23
# Source4:        http://nwalsh.com/docbook/simple/3.1.7.1/sdb3171.zip
Source4:        sdb3171.zip
Source5:        %{name}-README.SUSE
# URL no longer available 2023-05-23
# Source6:        http://www.labs.redhat.com/png/png-support.dtd
Source6:        png-support.dtd
# URL no longer available 2023-05-23
# Source7:        http://www.labs.redhat.com/png/png-support-3.1.dtd
Source7:        png-support-3.1.dtd
Source8:        CATALOG.db3sxml
Source9:        CATALOG.db3xml
Source10:       CATALOG.docbk30
# CATALOG.docbk31
Source11:       CATALOG.docbook_3
Source12:       CATALOG.gnome
Patch0:         docbk30.dif
BuildRequires:  fdupes
BuildRequires:  sgml-skel
BuildRequires:  unzip
Requires:       docbook_4
Requires:       iso_ent
Requires(pre):  %{_bindir}/xmlcatalog
Requires(pre):  %{regcat}
BuildArch:      noarch

%description
This package contains version 3.0 and 3.1 and an XML version.  It is
suitable for writing technical documentation.

The documentation can be found in %{_docdir}/docbook_3.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755
%define sgml_dir %{_datadir}/sgml
%define sgml_docbook_dir %{sgml_dir}/docbook
%define sgml_docbook_dtd_dir %{sgml_docbook_dir}/dtd
%define sgml_docbook_custom_dir %{sgml_docbook_dir}/custom
%define sgml_docbook_style_dir %{sgml_docbook_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_docbook_dir %{xml_dir}/docbook
%define xml_docbook_dtd_dir %{xml_docbook_dir}/schema/dtd
%define xml_docbook_custom_dir %{xml_docbook_dir}/custom
%define xml_docbook_style_dir %{xml_docbook_dir}/stylesheet
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_sysconf_dir %{_sysconfdir}/xml

%prep
%setup -q -n %{name} -c -T
cp %{SOURCE5} README.SUSE
%{INSTALL_DIR} dtd/{3.0,3.1} html xml sdb
cd dtd/3.0
unzip -aq %{_sourcedir}/%{dtd30}
cd ../3.1
unzip -aq %{_sourcedir}/%{dtd31}
cd ../../xml
unzip -aq %{_sourcedir}/%{db3x}
cd ../sdb
unzip -aq %{_sourcedir}/%{sdb}
cd ../html
tar -xzf %{_sourcedir}/%{docu}
cd ..
cp -p %{_sourcedir}/png-support.dtd .
cp -p %{_sourcedir}/png-support-3.1.dtd .
cp %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} .
patch -s -p0 <%{_sourcedir}/%{pkgdif}
rm -f html/index.html.orig
chmod -R a+rX,g-w,o-w .
find %{_builddir} -type d -exec chmod 755 {} +

%build

%install
pkg_name=%{name}
doc_dir=%{buildroot}/%{_defaultdocdir}/$pkg_name
%{INSTALL_DIR} $doc_dir/{30,31}
%{INSTALL_DIR} %{buildroot}%{sgml_docbook_dtd_dir}/{3.0,3.1,3.x-gnome}
%{INSTALL_DATA} dtd/3.0/* %{buildroot}/%{sgml_docbook_dtd_dir}/3.0
%{INSTALL_DATA} dtd/3.1/* %{buildroot}/%{sgml_docbook_dtd_dir}/3.1
%{INSTALL_DATA} png-support.dtd png-support-3.1.dtd \
  %{buildroot}/%{sgml_docbook_dtd_dir}/3.x-gnome
# xml
%{INSTALL_DIR} %{buildroot}/%{xml_docbook_dtd_dir}/{3.1,3.1-sdb}
cp -a xml/* %{buildroot}/%{xml_docbook_dtd_dir}/3.1
cp -a sdb/* %{buildroot}/%{xml_docbook_dtd_dir}/3.1-sdb
ln -sf %{xml_docbook_dtd_dir}/3.1 %{buildroot}/%{sgml_docbook_dtd_dir}/3.1xml
ln -sf %{xml_docbook_dtd_dir}/3.1-sdb \
  %{buildroot}/%{sgml_docbook_dtd_dir}/3.1-sdbxml
%{INSTALL_DATA} element-list.txt README.SUSE $doc_dir
c=$(echo CATALOG.*)
%{INSTALL_DATA} $c %{buildroot}/%{sgml_dir}
ln -sf %{sgml_dir}/CATALOG.docbook_3 \
  %{buildroot}/%{sgml_dir}/CATALOG.docbk31
# docomentation
cp -a html $doc_dir

# Reduce dupliticites
%fdupes %{buildroot}

%post
if [ -x %{regcat} ]; then
  for c in docbook_3; do
    %{regcat} -a  %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || true
  done
fi
exit 0

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in docbook_3; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || true
  done
fi
exit 0

%files
%{sgml_dir}/CATALOG.*
%{sgml_docbook_dtd_dir}/3*
%{xml_docbook_dtd_dir}/3*
%{_defaultdocdir}/%{name}
%dir %{sgml_docbook_dtd_dir}
%dir %{xml_docbook_dir}/schema
%dir %{xml_docbook_dtd_dir}

%changelog
