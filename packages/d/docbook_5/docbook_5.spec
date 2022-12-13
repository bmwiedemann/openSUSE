#
# spec file for package docbook_5
#
# Copyright (c) 2022 SUSE LLC
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


%define schemaversions 5.0 5.1 5.2CR3
%define realversion 5.2CR3
#
Name:           docbook_5
Version:        5.2cr3
Release:        0
Summary:        DocBook Schemas (DTD, RELAX NG, W3C Schema) for Version 5.x
License:        SUSE-Oasis-Specification-Notice
Group:          Productivity/Publishing/DocBook
URL:            https://www.oasis-open.org/docbook/
# XML Catalog Entry
Source1:        %{name}.xml
Source2:        %{name}-README.SUSE
# DocBook Sources
Source3:        docbook-5.0-docs.tar.bz2
Source4:        docbook-5.1-docs.tar.bz2
Source6:        Makefile
# DB 5.0
Source500:      docbook-5.0.tar.bz2
# DB 5.1
Source510:      docbook-5.1.tar.bz2
# DB 5.2
Source520:      docbook-%{realversion}.zip
# PATCH-FIX-OPENSUSE docbook_5-nvdl.patch change path to schema files
Patch501:       %{name}-nvdl.patch
#
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  sgml-skel
BuildRequires:  unzip
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun):sgml-skel >= 0.7
BuildArch:      noarch

%description
DocBook is a schema. It is particularly well-suited to books and papers
about computer hardware and software (though it is not limited to these
applications at all).

Version 5 is a complete rewrite of DocBook in RELAX NG.
The intent of this rewrite is to produce a schema that is true to the
spirit of DocBook while simultaneously removing inconsistencies that
have arisen as a natural consequence of DocBook's long, slow evolution.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The documentation for the DocBook 5.x specification (%{schemaversions})

%define xml_dir                %{_datadir}/xml
%define xml_docbook_dir        %{xml_dir}/docbook
%define xml_schema_dir         %{xml_dir}/docbook/schema
%define xml_docbook_dtd_dir    %{xml_schema_dir}/dtd
%define xml_docbook_rng_dir    %{xml_schema_dir}/rng
%define xml_docbook_sch_dir    %{xml_schema_dir}/sch
%define xml_docbook_xsd_dir    %{xml_schema_dir}/xsd
%define xml_docbook_nvdl_dir   %{xml_schema_dir}/nvdl
%define xml_docbook_custom_dir %{xml_docbook_dir}/custom
%define xml_docbook_style_dir  %{xml_docbook_dir}/stylesheet
%define xml_config_dir         %{_localstatedir}/lib/xml
%define xml_sysconf_dir        %{_sysconfdir}/xml

%prep
%setup -q -n %{name} -c -T
sed -i 's_@VERSION@_%{realversion}_g' %{SOURCE1}
# Copy catalog, README, and Makefile
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE6} .

# Unpack the sources:
tar -xf %{SOURCE500}
tar -xf %{SOURCE510}
unzip %{SOURCE520}
# Unpack the documentation:
tar -xf %{SOURCE3}
tar -xf %{SOURCE4}

chmod -R a+rX,g-w,o-w .
find . -type f | xargs chmod a-x

# Patching
%patch501

%build
# Nothing to build

%install
make DESTDIR=%{buildroot}

# cleanup
%fdupes %{buildroot}

%post
update-xml-catalog

%postun
update-xml-catalog

%check
%define catalog %{buildroot}%{xml_sysconf_dir}/catalog.d/docbook_5.xml
if [ -e %{catalog} ]; then
  xmlcatalog %{catalog} http://www.oasis-open.org/docbook/xml/5.2/rng/docbook.rnc
  exit 0
else
  exit 10
fi

%files
%config %{xml_sysconf_dir}/catalog.d/docbook_5.xml
%doc *README*
%doc docbook-%{realversion}/release-notes

#
%dir %{xml_docbook_dir}/schema
%dir %{xml_docbook_dtd_dir}
%dir %{xml_docbook_rng_dir}
%dir %{xml_docbook_sch_dir}
%dir %{xml_docbook_xsd_dir}
%dir %{xml_docbook_nvdl_dir}
%dir %{xml_docbook_style_dir}
# 5.0
%{xml_docbook_dtd_dir}/5.0
%{xml_docbook_rng_dir}/5.0
%{xml_docbook_sch_dir}/5.0
%{xml_docbook_xsd_dir}/5.0
%{xml_docbook_nvdl_dir}/5.0
# 5.1
%{xml_docbook_rng_dir}/5.1
%{xml_docbook_sch_dir}/5.1
%{xml_docbook_nvdl_dir}/5.1
#5.2*
%{xml_docbook_sch_dir}/%{realversion}
%{xml_docbook_rng_dir}/%{realversion}
%{xml_docbook_nvdl_dir}/%{realversion}
#5.2
%{xml_docbook_sch_dir}/5.2
%{xml_docbook_rng_dir}/5.2
%{xml_docbook_nvdl_dir}/5.2
# Upgrade stylesheet
%{xml_docbook_style_dir}/upgrade
#
%{_bindir}/db4-entities.pl

%files doc
%doc docbook*spec-cd-01.{pdf,html,xml}
%doc docbook*-os.{pdf,html,xml}

%changelog
