#
# spec file for package cim-schema
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cim-schema
Version:        2.50.0
Release:        0
Summary:        Common Information Model (CIM) Schema
License:        SUSE-DMTF
Group:          System/Management
Url:            http://www.dmtf.org/
Source0:        http://www.dmtf.org/sites/default/files/cim/cim_schema_v2500/cim_schema_%{version}Experimental-MOFs.zip
Source1:        loadmof.sh
Source2:        rmmof.sh
BuildRequires:  unzip
# openlmi-* requires the experimental variant
Provides:       cim-schema-experimental = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Common Information Model (CIM) is a model for describing overall
management information in a network or enterprise environment. CIM
consists of a specification and a schema. The specification defines the
details for integration with other management models. The schema
provides the actual model descriptions.

%prep
%setup -q -c

%build

%install
MOFDIR=%{_datadir}/mof
CIMDIR=$MOFDIR/cimv%{version}
for i in `find . -name "*.mof"`; do
  perl -p -i -e 's/\r//g' $i
done
install -d %{buildroot}/$CIMDIR
perl -p -i -e 's/\\/\//g' cim*.mof
echo "" >> qualifiers.mof
echo "// Optional Qualifiers: " >> qualifiers.mof
echo "" >> qualifiers.mof
cat qualifiers_optional.mof >> qualifiers.mof
rm qualifiers_optional.mof
chmod -R go-wx .
chmod -R a+rX .
mv * %{buildroot}/$CIMDIR/
ln -s cimv%{version} %{buildroot}/$MOFDIR/cim-current
pushd %{buildroot}/$CIMDIR/
ln -s cim*.mof CIM_Schema.mof
popd
install -d %{buildroot}%{_prefix}/bin
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/
perl -p -i -e 's~^#pragma include ("qualifiers_optional\.mof")~\/\/#pragma include ("qualifiers_optional\.mof")~g' %{buildroot}/$MOFDIR/cim-current/CIM_Schema.mof
perl -p -i -e \
	's~^#pragma include \("qualifiers_optional\.mof"\)~\/\/#pragma include ("qualifiers_optional\.mof")~g' \
	%{buildroot}/$MOFDIR/cim-current/CIM_Schema.mof

%files
%defattr(-, root, root)
%dir %{_datadir}/mof
%dir %{_datadir}/mof/cimv%{version}
%{_datadir}/mof/cimv%{version}/*
%{_datadir}/mof/cim-current
%{_bindir}/loadmof.sh
%{_bindir}/rmmof.sh

%changelog
