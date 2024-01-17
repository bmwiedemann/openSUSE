#
# spec file for package cedict
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cedict
# Set version as official release date
Version:        20141224
Release:        0
Summary:        Free Chinese-English Dictionary in EDICT Format
License:        CC-BY-SA-3.0 and GPL-2.0+
Group:          System/I18n/Chinese
Url:            http://www.mdbg.net/chindict/chindict.php?page=cedict
Source0:        http://www.mdbg.net/chindict/export/cedict/%{name}_1_0_ts_utf-8_mdbg.zip
Source1:        cedict-format.pl
Source11:       README.SUSE
BuildRequires:  dos2unix
BuildRequires:  unzip
Provides:       locale(gjiten:zh)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a free Chinese-English dictionary that can be used, for
example, with Gjiten.

The objective of the CEDICT project is to create an online,
downloadable (as opposed to searchable-only) public-domain
Chinese-English dictionary. For the most part, the project is modelled
on Jim Breen's highly successful EDICT (Japanese-English dictionary)
project and is intended to be a collaborative effort with users
providing entries and corrections to the main file.

%prep
cp %{SOURCE0} .
unzip %{name}_1_0_ts_utf-8_mdbg.zip
cp %{SOURCE11} .
chmod 755 $RPM_SOURCE_DIR/cedict-format.pl

%build

%install
mkdir -p %{buildroot}%{_datadir}/edict
dos2unix < cedict_ts.u8 | $RPM_SOURCE_DIR/cedict-format.pl  > %{buildroot}%{_datadir}/edict/cedict_ts.u8
chmod 644 %{buildroot}%{_datadir}/edict/cedict_ts.u8

%files
%defattr(-, root, root)
%doc README.SUSE
%dir %{_datadir}/edict/
%{_datadir}/edict/cedict_ts.u8

%changelog
