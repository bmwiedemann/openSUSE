#
# spec file for package docbook_4
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define regcat %{_bindir}/sgml-register-catalog
Name:           docbook_4
Version:        4.5
Release:        0
Summary:        DocBook DTD Version 4.x
License:        BSD-3-Clause AND MIT
Group:          Productivity/Publishing/DocBook
Url:            http://www.oasis-open.org/docbook/
Source2:        docbook_4-README.SUSE
Source3:        %{name}.xml
Source7:        CATALOG.docbook_4
Source8:        Makefile
# Only needed to regenerate docbook_4.xml
Source9:        generate-docbook_4-xmlcat.py

# DocBook 4.1
Source410:      http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
Source411:      docbook-xml-4.1.2-catalog.xml
Source412:      http://www.oasis-open.org/docbook/xml/4.1/docbkx412.zip
# No RNG and XSD files for DB4.1
Source414:      CATALOG.db41xml
# DocBook 4.2
Source420:      http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
Source421:      http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
Source422:      http://www.oasis-open.org/docbook/rng/4.2/docbook-rng-4.2.zip
Source423:      http://www.oasis-open.org/docbook/xsd/4.2/docbook-xsd-4.2.zip
Source424:      CATALOG.db42xml
# DocBook 4.3
Source430:      http://www.docbook.org/sgml/4.3/docbook-4.3.zip
Source431:      http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
Source432:      http://www.docbook.org/rng/4.3/docbook-rng-4.3.zip
Source433:      http://www.docbook.org/xsd/4.3/docbook-xsd-4.3.zip
Source434:      CATALOG.db43xml
# DocBook 4.4
Source440:      http://www.oasis-open.org/docbook/sgml/4.4/docbook-4.4.zip
Source441:      http://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip
Source442:      http://www.docbook.org/rng/4.4/docbook-rng-4.4.zip
Source443:      http://www.docbook.org/xsd/4.4/docbook-xsd-4.4.zip
Source444:      CATALOG.db44xml
# DocBook 4.5
Source450:      http://www.oasis-open.org/docbook/sgml/4.5/docbook-4.5.zip
Source451:      http://www.oasis-open.org/docbook/xml/4.5/docbook-xml-4.5.zip
Source452:      http://www.docbook.org/rng/4.5/docbook-rng-4.5.zip
Source453:      http://www.docbook.org/xsd/4.5/docbook-xsd-4.5.zip
Source454:      CATALOG.db45xml
# Patches
Patch1:         docbook-4-3.diff
Patch2:         docbook-4-3-xml-cat.diff
Patch3:         docbook.4.4.dcl.diff
#
BuildRequires:  fdupes
BuildRequires:  sgml-skel >= 0.7
BuildRequires:  unzip
Requires:       iso_ent
PreReq:         %{_bindir}/xmlcatalog
PreReq:         awk
PreReq:         grep
PreReq:         sed
PreReq:         sgml-skel
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Provides:       docbook
Provides:       docbook-dtd
Provides:       docbook-dtds
BuildArch:      noarch

%description
DocBook is a schema. It is particularly well-suited to books and papers
about computer hardware and software (though it is not limited to these
applications at all). This package has SGML- and XML-DTD versions
included. Some versions of DocBook contain also a RELAX NG and W3C
Schema.

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
%define xml_docbook_rng_dir %{xml_docbook_dir}/schema/rng
%define xml_docbook_xsd_dir %{xml_docbook_dir}/schema/xsd
%define xml_docbook_custom_dir %{xml_docbook_dir}/custom
%define xml_docbook_style_dir %{xml_docbook_dir}/stylesheet
%define sgml_config_dir %{_localstatedir}/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir %{_localstatedir}/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
%define my_all_cat docbook_4 db41xml db42xml db43xml db44xml db45xml

%prep
%setup -q -n %{name} -c -T
cp -p $RPM_SOURCE_DIR/%{name}-README.SUSE README.SUSE

# DocBook 4.1
unzip -q -a %{SOURCE410} -d docbook-sgml-4.1
unzip -q -a %{SOURCE412} -d docbook-xml-4.1.2
cp -vi %{SOURCE411} docbook-xml-4.1.2/catalog.xml
# DocBook 4.2
unzip -q -a %{SOURCE420} -d docbook-sgml-4.2
unzip -q -a %{SOURCE421} -d docbook-xml-4.2
unzip -q -a %{SOURCE422} -d docbook-rng-4.2
unzip -q -a %{SOURCE423} -d docbook-xsd-4.2
# DocBook 4.3
unzip -q -a %{SOURCE430} -d docbook-sgml-4.3
unzip -q -a %{SOURCE431} -d docbook-xml-4.3
unzip -q -a %{SOURCE432} -d docbook-rng-4.3
unzip -q -a %{SOURCE433} -d docbook-xsd-4.3
# DocBook 4.4
unzip -q -a %{SOURCE440} -d docbook-sgml-4.4
unzip -q -a %{SOURCE441} -d docbook-xml-4.4
unzip -q -a %{SOURCE442} -d docbook-rng-4.4
unzip -q -a %{SOURCE443} -d docbook-xsd-4.4
# DocBook 4.5
unzip -q -a %{SOURCE450} -d docbook-sgml-4.5
unzip -q -a %{SOURCE451} -d docbook-xml-4.5
unzip -q -a %{SOURCE452} -d docbook-rng-4.5
unzip -q -a %{SOURCE453} -d docbook-xsd-4.5

%patch1 -p 1 -p 0
%patch2 -p 1
%patch3 -p 1

# CATALOG.* files
cp %{SOURCE3} %{SOURCE7} %{SOURCE8} %{SOURCE414} %{SOURCE424} %{SOURCE434} %{SOURCE444} %{SOURCE454} .
chmod -R a+rX,g-w,o-w .
# Remove executable bit from files
find . -type f | xargs chmod a-x

%build
# Nothing to build

%install
make DESTDIR=%{buildroot} install

# cleanup
%fdupes -s %{buildroot}

%post
if [ -x %{regcat} ]; then
  for c in %{my_all_cat}; do
    %{regcat} -a  %{sgml_dir}/CATALOG.$c \
      >/dev/null 2>&1 || true
  done
fi

# in case of an update, remove old
if [ "2" = "$1" ]; then
  %{_bindir}/edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
      --del %{name}-%{version} || true
fi
if [ ! -f %{_sysconfdir}/xml/suse-catalog.xml -a -x %{_bindir}/edit-xml-catalog ]; then
%{_bindir}/edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
      --add %{_sysconfdir}/xml/%{FOR_ROOT_CAT}
fi

update-xml-catalog
exit 0

%postun
update-xml-catalog
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in %{my_all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c \
      >/dev/null 2>&1 || true
  done
fi
# remove entries only on removal of file
if [ "0" = "$1" -a ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} ] ; then
  %{_bindir}/edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
      --del %{name}-%{version}
fi
exit 0

%files
# %%config %%{sgml_config_dir}/CATALOG.*
%config %{_sysconfdir}/xml/catalog.d/%{name}.xml

%doc README.SUSE
%{sgml_dir}/CATALOG.*
%{sgml_docbook_dtd_dir}/4.1
%{sgml_docbook_dtd_dir}/4.2
%{sgml_docbook_dtd_dir}/4.3
%{sgml_docbook_dtd_dir}/4.4
%{sgml_docbook_dtd_dir}/4.5
#
%{sgml_docbook_dtd_dir}/4.1.2xml
%{sgml_docbook_dtd_dir}/4.2xml
%{sgml_docbook_dtd_dir}/4.3xml
%{sgml_docbook_dtd_dir}/4.4xml
%{sgml_docbook_dtd_dir}/4.5xml
#
%{xml_docbook_dtd_dir}/4.1.2
%{xml_docbook_dtd_dir}/4.2
%{xml_docbook_dtd_dir}/4.3
%{xml_docbook_dtd_dir}/4.4
%{xml_docbook_dtd_dir}/4.5
#
%{xml_docbook_rng_dir}/4.2
%{xml_docbook_rng_dir}/4.3
%{xml_docbook_rng_dir}/4.4
%{xml_docbook_rng_dir}/4.5
#
%{xml_docbook_xsd_dir}/4.2
%{xml_docbook_xsd_dir}/4.3
%{xml_docbook_xsd_dir}/4.4
%{xml_docbook_xsd_dir}/4.5
#
%dir %{sgml_dir}/docbook/dtd
%dir %{xml_docbook_dir}/schema
%dir %{xml_docbook_dtd_dir}
%dir %{xml_docbook_rng_dir}
%dir %{xml_docbook_xsd_dir}

%changelog
