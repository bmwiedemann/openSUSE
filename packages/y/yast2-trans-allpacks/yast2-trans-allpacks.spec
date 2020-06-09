#
# spec file for package yast2-trans-allpacks
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-trans-allpacks
Version:        4.3.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         /usr
Requires:       yast2-trans-af
Requires:       yast2-trans-ar
Requires:       yast2-trans-ast
Requires:       yast2-trans-bg
Requires:       yast2-trans-bn
Requires:       yast2-trans-bs
Requires:       yast2-trans-ca
Requires:       yast2-trans-cs
Requires:       yast2-trans-cy
Requires:       yast2-trans-da
Requires:       yast2-trans-de
Requires:       yast2-trans-el
Requires:       yast2-trans-en_GB
Requires:       yast2-trans-es
Requires:       yast2-trans-et
Requires:       yast2-trans-fa
Requires:       yast2-trans-fi
Requires:       yast2-trans-fr
Requires:       yast2-trans-gl
Requires:       yast2-trans-gu
Requires:       yast2-trans-hi
Requires:       yast2-trans-hr
Requires:       yast2-trans-hu
Requires:       yast2-trans-id
Requires:       yast2-trans-it
Requires:       yast2-trans-ja
Requires:       yast2-trans-jv
Requires:       yast2-trans-ka
Requires:       yast2-trans-km
Requires:       yast2-trans-kn
Requires:       yast2-trans-ko
Requires:       yast2-trans-ku
Requires:       yast2-trans-lo
Requires:       yast2-trans-lt
Requires:       yast2-trans-mk
Requires:       yast2-trans-mr
Requires:       yast2-trans-nb
Requires:       yast2-trans-nds
Requires:       yast2-trans-nl
Requires:       yast2-trans-nn
Requires:       yast2-trans-pa
Requires:       yast2-trans-pl
Requires:       yast2-trans-pt
Requires:       yast2-trans-pt_BR
Requires:       yast2-trans-ro
Requires:       yast2-trans-ru
Requires:       yast2-trans-si
Requires:       yast2-trans-sk
Requires:       yast2-trans-sl
Requires:       yast2-trans-sr
Requires:       yast2-trans-sv
Requires:       yast2-trans-sw
Requires:       yast2-trans-ta
Requires:       yast2-trans-tg
Requires:       yast2-trans-th
Requires:       yast2-trans-tr
Requires:       yast2-trans-uk
Requires:       yast2-trans-vi
Requires:       yast2-trans-wa
Requires:       yast2-trans-xh
Requires:       yast2-trans-zh_CN
Requires:       yast2-trans-zh_TW
Requires:       yast2-trans-zu
BuildArch:      noarch
Summary:        Internal: Require all YaST Translation Packages (Empty)
License:        LGPL-2.1-or-later
Group:          System/YaST
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
