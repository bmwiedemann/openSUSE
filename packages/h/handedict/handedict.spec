#
# spec file for package handedict
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

Name:           handedict
BuildRequires:  dos2unix
Provides:       locale(gjiten:zh)
Version:        20090318
Release:        0
Url:            http://chdw.de/dl
# original archive is at http://www.chinaboard.de/handedict/handedict_uv-20060906.tar.bz2
# repackaged here to save space in the source rpm
# (several big files from the original archive are not needed).
# Jan Hefti  <j.hefti@chinaboard.de> made the individual files available as well now,
# the big dictionary with the example sentences in UTF-8 can be downloaded here:
# http://www.chinaboard.de/handedict/handedict_uv.u8.bz2
Source0:        handedict_uv.u8.bz2
Source1:        License
Source10:       cedict-format.pl
Source11:       README.SUSE
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Free Chinese-German Dictionary in EDICT Format
License:        CC-BY-SA-3.0 and GPL-2.0+
Group:          System/I18n/Chinese

%description
This is a free Chinese-German dictionary that can be used, for example,
with Gjiten.

Everyone is invited to help develop it together with the authors (see
URL and e-mail addresses in the author list). It is based in large
parts on CEDICT which in turn has been modelled on Jim Breen's highly
successful EDICT (Japanese-English dictionary) project.



Authors:
--------
    Michael Klaus Engel <redaktion@chdw.de>
    Jan Hefti <redaktion@chdw.de>
    Helmut Anker <redaktion@chdw.de>
    Jennifer Gross <redaktion@chdw.de>
    Julia Mannigel <redaktion@chdw.de>
    Tian Xiaoyong <redaktion@chdw.de>
    Steffen Weidenhaus <redaktion@chdw.de>
    Zhao Chunhua <redaktion@chdw.de>
    Zheng Meishi <redaktion@chdw.de>

%prep 
%setup -q -n %{name} -c %{name} -T
cp $RPM_SOURCE_DIR/handedict_uv.u8.bz2 .
cp $RPM_SOURCE_DIR/README.SUSE .
cp $RPM_SOURCE_DIR/License .
chmod 755 $RPM_SOURCE_DIR/cedict-format.pl

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/edict
bunzip2 < handedict_uv.u8.bz2 | dos2unix | $RPM_SOURCE_DIR/cedict-format.pl  > $RPM_BUILD_ROOT/usr/share/edict/handedict
chmod 644 $RPM_BUILD_ROOT/usr/share/edict/*

%clean 

%files
%defattr(-, root, root)
%doc README.SUSE License
%dir /usr/share/edict/
/usr/share/edict/*

%changelog
