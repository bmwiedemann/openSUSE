#
# spec file for package wine-gecko
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wine-gecko
Summary:        The Wine specific Gecko HTML rendering engine
License:        MPL-1.1+
Group:          Development/Tools/Other
Version:        2.47
Release:        0
Source0:        http://dl.winehq.org/wine/wine-gecko/%{version}/wine_gecko-%{version}-x86.msi
Source1:        http://dl.winehq.org/wine/wine-gecko/%{version}/wine_gecko-%{version}-x86_64.msi
BuildArch:      noarch
# Source of this CAB is at:
# http://wine.git.sourceforge.net/git/gitweb.cgi?p=wine/wine-gecko;a=summary
# build instructions are at http://wiki.winehq.org/BuildingWineGecko
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Supplements:    wine wine-snapshot

%description
This package contains the prepackaged Win32 Gecko rendering engine for use by Wine.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/wine/gecko
cp %{SOURCE0} $RPM_BUILD_ROOT/usr/share/wine/gecko
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/share/wine/gecko

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%dir /usr/share/wine
%dir /usr/share/wine/gecko
/usr/share/wine/gecko/*msi

%changelog
