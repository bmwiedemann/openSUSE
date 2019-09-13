#
# spec file for package vcron
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           vcron
Version:        2.3
Release:        0
Summary:        TK-Interface for cron and at
License:        GPL-2.0+
Group:          System/Base
Url:            http://www.Linux-kheops.com/pub/vcron/
Source:         vcron-%{version}.tar.bz2
Patch:          vcron-%{version}-path.patch
Patch1:         vcron-%{version}-tempfiles.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       at
Requires:       cron
Requires:       freetype2
Requires:       tcl >= 8
Requires:       tk >= 8

%description
TK-Interface for cron and at.



Authors:
--------
    Daniel Roche <dan@lectra.com>

%prep
%setup -n usr
%patch -p1
%patch1 -p1

%build

%install
install -D -m 755 local/bin/vcron $RPM_BUILD_ROOT/usr/bin/vcron
mkdir -p  $RPM_BUILD_ROOT/usr/lib
cp -R local/lib/vcron  $RPM_BUILD_ROOT/usr/lib/ 
install -m 755 -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}/
( 
  cd $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}/
  ln -sf ../../../../lib/vcron/doc/* ./
)

%files
%defattr(-,root,root)
/usr/bin/vcron
/usr/lib/vcron
%doc %{_defaultdocdir}/%{name}

%changelog
