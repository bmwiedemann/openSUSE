#
# spec file for package yast2-trans-allpacks
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           yast2-trans-allpacks
Version:        2.21.0
Release:        1
License:        LGPL-2.1+
Group:          System/YaST
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         /usr
Requires:       yast2-trans-af yast2-trans-ar yast2-trans-ast yast2-trans-bg yast2-trans-bn yast2-trans-bs yast2-trans-ca yast2-trans-cs yast2-trans-cy yast2-trans-da yast2-trans-de yast2-trans-el yast2-trans-en_GB yast2-trans-en_US yast2-trans-es yast2-trans-et yast2-trans-fa yast2-trans-fi yast2-trans-fr yast2-trans-gl yast2-trans-gu yast2-trans-hi yast2-trans-hr yast2-trans-hu yast2-trans-id yast2-trans-it yast2-trans-ja yast2-trans-jv yast2-trans-ka yast2-trans-km yast2-trans-kn yast2-trans-ko yast2-trans-ku yast2-trans-lo yast2-trans-lt yast2-trans-mk yast2-trans-mr yast2-trans-nb yast2-trans-nds yast2-trans-nl yast2-trans-nn yast2-trans-pa yast2-trans-pl yast2-trans-pt yast2-trans-pt_BR yast2-trans-ro yast2-trans-ru yast2-trans-si yast2-trans-sk yast2-trans-sl yast2-trans-sr yast2-trans-sv yast2-trans-sw yast2-trans-ta yast2-trans-tg yast2-trans-th yast2-trans-tr yast2-trans-uk yast2-trans-vi yast2-trans-wa yast2-trans-xh yast2-trans-zh_CN yast2-trans-zh_TW yast2-trans-zu
BuildArch:      noarch
Summary:        Internal: Require all YaST Translation Packages (Empty)
Source:         list-trans-packs.sh
Source1:        README

%description
The package requires all YaST translation packages
(yast2-trans-{??,??_??}).  Otherwise it is empty.

For internal use only.



%prep
cp %{S:1} .

%build

%install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README

%changelog
