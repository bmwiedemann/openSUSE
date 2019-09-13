#
# spec file for package stardict-sounds-wyabdcrealpeopletts (Version 2.1.0)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           stardict-sounds-wyabdcrealpeopletts
Summary:        Wyabdc RealPeople TTS audio collection of english words
Version:        2.1.0
Release:        1
License:        GPL-2.0+
Group:          Productivity/Office/Dictionary
Url:            http://stardict.sourceforge.net
Provides:       locale(stardict:en)
BuildArch:      noarch
%if 0%{?suse_version} > 1020
Recommends:     stardict
%else
Requires:       stardict
%endif
Source0:        WyabdcRealPeopleTTS.tar.bz2
Source1:        license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         stardict_dir %_datadir/stardict
%define         stardict_dic_dir %stardict_dir/dic

%description
This package contains many wav files which can be used by StarDict to pronounce
english words. Files originally come from wyabdc, http://www.zhimajie.net,
thanks xiaozima.


%prep
%setup -q -T -c WyabdcRealPeopleTTS -a0

%build

%install
mkdir -p %buildroot/%stardict_dir
cp -a *  %buildroot/%stardict_dir/
mkdir -p %buildroot/%_docdir/%name
cp %{SOURCE1} %buildroot/%_docdir/%name
mv %buildroot/%stardict_dir/WyabdcRealPeopleTTS/{readme.txt,README} %buildroot/%_docdir/%name

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %_docdir/%name
%doc %_docdir/%name/license.txt
%doc %_docdir/%name/readme.txt
%doc %_docdir/%name/README
%dir %stardict_dir
%stardict_dir

%changelog
