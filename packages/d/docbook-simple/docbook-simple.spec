#
# spec file for package docbook-simple
#
# Copyright (c) 2021 SUSE LLC
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


Name:           docbook-simple
BuildRequires:  unzip
Summary:        Simple DocBook DTD and Documentation
License:        HPND
Group:          Productivity/Publishing/DocBook
Version:        1.1
Release:        0
BuildArch:      noarch
Requires:       libxml2-tools
Requires:       sgml-skel
Requires(post): /usr/bin/install-catalog
Requires(post): /usr/bin/xmlcatalog
Requires(postun): /usr/bin/xmlcatalog
URL:            https://www.oasis-open.org/docbook/xml/simple/
Source0:        https://www.oasis-open.org/docbook/xml/simple/%{version}/docbook-simple-%{version}.zip
Source1:        %{name}-%{version}.cat
Source2:        %{name}-%{version}.xml

%description
This package contains the Simple DocBook DTD.

%define xml_dir %{_datadir}/xml
%define sgml_dir %{_datadir}/sgml
%define xml_mod_root %{xml_dir}/docbook/simple
%define xml_mod_dir %{xml_mod_root}/%{version}
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_sysconf_dir %{_sysconfdir}/xml
%define xml_catalog %{xml_sysconf_dir}/catalog
%define sgml_catalog %{sgml_sysconf_dir}/catalog

%prep
%setup -q -c -n %{version}
sed 's|@XML_DTD_DIR@|%{xml_mod_dir}|' %{SOURCE1} > $(basename %{SOURCE1})
sed 's|@XML_DTD_DIR@|%{xml_mod_dir}|' %{SOURCE2} > $(basename %{SOURCE2})
# make sure everything is readable
chmod a+r *

%build
# nothing to build

%install
# install versioned directory of dtd files
mkdir -p %{buildroot}%{xml_mod_dir}
cp -a *.{css,dtd,mod} %{buildroot}%{xml_mod_dir}
# install package catalogs
mkdir -p %{buildroot}%{sgml_dir}
mkdir -p %{buildroot}%{xml_mod_dir}
install -p -m 644 "$(basename %{SOURCE1})" %{buildroot}%{sgml_dir}
install -p -m 644 "$(basename %{SOURCE2})" %{buildroot}%{xml_mod_root}

%post
# SGML catalog registration
if [ -w %{sgml_catalog} ]; then
  install-catalog --add \
    "%{sgml_dir}/%{name}-%{version}.cat" \
    "%{sgml_catalog}" 1>/dev/null
# Workaround bug in install-catalog (from Fedora)
  sed -i '/^CATALOG.*log\"$/d' %{sgml_dir}/%{name}-%{version}.cat
  sed -i '/^CATALOG.*log$/d' %{sgml_dir}/%{name}-%{version}.cat
fi
# XML catalog registration
if [ -w %{xml_catalog} ]; then
  xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//DTD Simplified" \
    "file://%{xml_mod_dir}/%{name}-%{version}.xml" %{xml_catalog}
  xmlcatalog --noout --add "delegateURI" \
    "http://www.oasis-open.org/docbook/xml/simple/1.1/" \
    "file://%{xml_mod_dir}/%{name}-%{version}.xml" %{xml_catalog}
# Some resolvers misinterpret uri entries
  xmlcatalog --noout --add "delegateSystem" \
    "http://www.oasis-open.org/docbook/xml/simple/1.1/" \
    "file://%{xml_mod_dir}/%{name}-%{version}.xml" %{xml_catalog}
fi

%postun
if [ "$1" = 0 ]; then
  xmlcatalog --sgml --noout --del \
    %{sgml_catalog} \
    %{sgml_dir}/%{name}-%{version}.cat

  xmlcatalog --noout --del \
    "file://%{xml_mod_dir}/%{name}-%{version}.xml" \
     %{xml_catalog} 
fi
 
%files
%{xml_mod_dir}
%dir %{xml_mod_root}
%{sgml_dir}/%{name}-%{version}.cat
%{xml_mod_root}/%{name}-%{version}.xml

%changelog
