#
# spec file for package iso_ent
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define INSTALL_DIR       install -m755 -d
%define INSTALL_DATA      install -m644 -p
%define sgml_dir          %{_datadir}/sgml

Name:           iso_ent
Version:        2000.11.03
Release:        0
Summary:        Character Entity Sets for ISO 8879:1986
License:        SUSE-Permissive
Group:          Productivity/Publishing/SGML
URL:            https://xml.coverpages.org/topics.html#entities
Source0:        https://xml.coverpages.org/ISOEnts.zip
Source1:        ISOgrk5.zip
Patch0:         iso_ent.dif
BuildRequires:  unzip
Requires(post): sgml-skel
Provides:       iso-ent
Provides:       iso-entities
BuildArch:      noarch

%description
ISO 8879:1986 and ISO 9573-15:1993 character entity sets

%prep
%autosetup -c -p1 -a1 -n %{name}

%build
# no-op

%install
%{INSTALL_DIR} %{buildroot}%{sgml_dir}/iso-ent \
               %{buildroot}%{sgml_dir}/ISO_8879:1986/entities \
               %{buildroot}%{sgml_dir}/ISO_9573-15:1993/entities

%{INSTALL_DATA} ISO*    %{buildroot}%{sgml_dir}/iso-ent
%{INSTALL_DATA} CATALOG %{buildroot}%{sgml_dir}/CATALOG.iso_ent

pushd %{buildroot}%{sgml_dir}
  rm -f ISO_8879-1986
  ln -s ISO_8879:1986 ISO_8879-1986
popd

pushd %{buildroot}%{sgml_dir}/ISO_8879:1986/entities
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

pushd %{buildroot}%{sgml_dir}
  rm -f ISO_9573-15-1993
  ln -s ISO_9573-15:1993 ISO_9573-15-1993
popd

pushd %{buildroot}%{sgml_dir}/ISO_9573-15:1993/entities
  rm -f * 2>/dev/null
  ln -s ../../iso-ent/ISOgrk5 Extra_Classical_Greek_Letters
popd

%post
sgml-register-catalog -a %{sgml_dir}/CATALOG.iso_ent >/dev/null 2>&1 || :

%postun
if [ "$1" = "0" ] && [ -x %{_bindir}/sgml-register-catalog ]; then
    sgml-register-catalog -r %{sgml_dir}/CATALOG.iso_ent >/dev/null 2>&1 || :
fi

%files
%{sgml_dir}/CATALOG.iso_ent
%{sgml_dir}/iso-ent
%{sgml_dir}/ISO_8879-1986
%{sgml_dir}/ISO_8879:1986
%{sgml_dir}/ISO_9573-15:1993
%{sgml_dir}/ISO_9573-15-1993

%changelog
