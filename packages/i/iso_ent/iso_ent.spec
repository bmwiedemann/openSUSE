#
# spec file for package iso_ent
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           iso_ent
BuildRequires:  sgml-skel
BuildRequires:  unzip
BuildArch:      noarch
Provides:       iso-ent
Provides:       iso-entities
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat}
Version:        2000.11.03
Release:        0
Summary:        Character Entity Sets for ISO 8879:1986
License:        SUSE-Permissive
Group:          Productivity/Publishing/SGML
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define ke_pkg ISOEnts.zip
Source0:        http://www.oasis-open.org/cover/ISOEnts.zip
Source1:        ISOgrk5.gz
Patch:          iso_ent.dif

%description
Character entity sets for ISO 8879:1986.


%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define sgml_dir %{_datadir}/sgml
%define sgml_config_dir /var/lib/sgml

%prep
%setup -n %{name} -c -T
unzip -aq $RPM_SOURCE_DIR/%{ke_pkg}
cp -p $RPM_SOURCE_DIR/ISOgrk5.gz .
gunzip ISOgrk5.gz
%patch -p1

%build

%install
root=$RPM_BUILD_ROOT
# sgml_dir=${root}%{_datadir}/sgml
# sgml_dir_config=${root}/var/lib/sgml
sgml_dir_iso=$RPM_BUILD_ROOT%{sgml_dir}/iso-ent
sgml_dir_ISO=$RPM_BUILD_ROOT%{sgml_dir}/ISO_8879:1986/entities
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_config_dir}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/iso-ent
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir}/{ISO_8879:1986,ISO_9573-15:1993}/entities
%{INSTALL_DATA} ISO* $RPM_BUILD_ROOT%{sgml_dir}/iso-ent
%{INSTALL_DATA} CATALOG $RPM_BUILD_ROOT%{sgml_config_dir}/CATALOG.iso_ent
pushd $RPM_BUILD_ROOT%{sgml_dir}
ln -sf ../../../var/lib/sgml/CATALOG.iso_ent CATALOG.iso_ent
rm -f ISO_8879-1986 
ln -s ISO_8879:1986 ISO_8879-1986
popd
pushd ${sgml_dir_ISO}
rm -f * 2>/dev/null
ln -s ../../iso-ent/ISOamsa Added_Math_Symbols:_Arrow_Relations
ln -s ../../iso-ent/ISOamsb Added_Math_Symbols:_Binary_Operators
ln -s ../../iso-ent/ISOamsc Added_Math_Symbols:_Delimiters
ln -s ../../iso-ent/ISOamsn Added_Math_Symbols:_Negated_Relations
ln -s ../../iso-ent/ISOamso Added_Math_Symbols:_Ordinary
ln -s ../../iso-ent/ISOamsr Added_Math_Symbols:_Relations
ln -s ../../iso-ent/ISObox Box_and_Line_Drawing
ln -s ../../iso-ent/ISOcyr1 Russian_Cyrillic
ln -s ../../iso-ent/ISOcyr2 Non-Russian_Cyrillic
ln -s ../../iso-ent/ISOdia Diacritical_Marks
ln -s ../../iso-ent/ISOgrk1 Greek_Letters
ln -s ../../iso-ent/ISOgrk2 Monotoniko_Greek
ln -s ../../iso-ent/ISOgrk3 Greek_Symbols
ln -s ../../iso-ent/ISOgrk4 Alternative_Greek_Symbols
ln -s ../../iso-ent/ISOlat1 Added_Latin_1
ln -s ../../iso-ent/ISOlat2 Added_Latin_2
ln -s ../../iso-ent/ISOnum Numeric_and_Special_Graphic
ln -s ../../iso-ent/ISOpub Publishing
ln -s ../../iso-ent/ISOtech General_Technical
popd
pushd $RPM_BUILD_ROOT%{sgml_dir}
rm -f ISO_9573-15-1993
ln -s ISO_9573-15:1993 ISO_9573-15-1993
popd
pushd $RPM_BUILD_ROOT%{sgml_dir}/ISO_9573-15:1993/entities
rm -f * 2>/dev/null
ln -s ../../iso-ent/ISOgrk5 Extra_Classical_Greek_Letters
popd

%post
if [ -x %{regcat} ]; then
  for c in iso_ent; do
    %{regcat} -a %{sgml_dir}/CATALOG.$c \
      >/dev/null 2>&1 || true
  done
fi
exit 0

%postun
if [  "$1" = "0" -a -x %{regcat} ]; then
  for c in CATALOG.iso_ent; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
# %doc README.SuSE
%config /var/lib/sgml/CATALOG.iso_ent
%{sgml_dir}/CATALOG.iso_ent
%{sgml_dir}/iso-ent
%{sgml_dir}/ISO_8879-1986
%{sgml_dir}/ISO_8879:1986
%{sgml_dir}/ISO_9573-15:1993
%{sgml_dir}/ISO_9573-15-1993

%changelog
