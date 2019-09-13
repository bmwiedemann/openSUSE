#
# spec file for package stardict-dic-enru-mueller7
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

# norootforbuild


Name:           stardict-dic-enru-mueller7
Summary:        English-Russian dictionary by professor V. K. Mueller
Version:        1.2
Release:        2
License:        GPL-2.0+
Group:          Productivity/Office/Dictionary
Url:            http://mueller-dic.chat.ru/
Provides:       locale(stardict:ru)
BuildArch:      noarch
%if 0%{?suse_version} > 1020
Recommends:     stardict
%else
Requires:       stardict
%endif
Source0:        mueller7.tar.bz2
Source1:        license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         stardict_dir %_datadir/stardict
%define         stardict_dic_dir %stardict_dir/dic

%description
English-Russian dictionary by professor V. K. Mueller, 7 edition with 46231 articles in StarDict format.


%prep
%setup -q -T -c mueller7 -a0 

%build

%install
mkdir -p %buildroot/%stardict_dic_dir
cp -a *  %buildroot/%stardict_dic_dir/
mkdir -p %buildroot/%_docdir/%name
cp %{SOURCE1} %buildroot/%_docdir/%name

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %_docdir/%name
%doc %_docdir/%name/license.txt
%dir %stardict_dir
%dir %stardict_dic_dir
%stardict_dic_dir

%changelog
