#
# spec file for package stardict-dic-enru-engcom
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


Name:           stardict-dic-enru-engcom
Summary:        English-Russian dictionary of computer terms
Version:        1.36
Release:        3
License:        GFDL-1.1
Group:          Productivity/Office/Dictionary
Url:            http://engcom.org.ru/
Provides:       locale(stardict:ru)
BuildArch:      noarch
%if 0%{?suse_version} > 1020
Recommends:     stardict
%else
Requires:       stardict
%endif
Source0:        engcom.tar.bz2
Source1:        license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         stardict_dir %_datadir/stardict
%define         stardict_dic_dir %stardict_dir/dic

%description
The open English-Russian dictionary of computer terms with more than 2000 articles in StarDict format. It is not an academic dictionary.


%prep
%setup -q -T -c engcom -a0 

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
