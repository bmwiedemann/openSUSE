#
# spec file for package yast2-trans-stats (Version 2.19.0)
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


Name:           yast2-trans-stats
#!BuildIgnore: yast2-build-test yast2-schema
#!BuildIgnore: java-sdk-1.5.0 java-devel
#!BuildIgnore: tomcat5
BuildRequires:  yast2-trans-allpacks
Version:        2.19.0
Release:        1
License:        GPL-2.0+
Group:          System/YaST
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         /usr
# Requires:	yast2-config-XXpkgXX
BuildArch:      noarch
Summary:        YaST2 - Translation Statistics

%description
The package contains statistic files (one file per language).  With the
help of these statistics Yast warns you if you select a language for
installation which is unsufficiently translated.



%prep

%build
for f in /usr/share/doc/packages/yast2-trans-*/status.txt; do
  [ -f $f ] || continue
  l=${f%/*}; l=${l##*-}
  case $l in
    en_*)
      echo 100 >$l.status
      ;;
    *)
      sed -n 's/^\([[:digit:]]\+\).*/\1/p' $f >$l.status
      ;;
  esac
  [ -s $l.status ] || rm $l.status
done

%install
install -d $RPM_BUILD_ROOT/usr/lib/YaST2/trans
install -m 644 *.status $RPM_BUILD_ROOT/usr/lib/YaST2/trans

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%dir /usr/lib/YaST2
/usr/lib/YaST2/trans

%changelog
