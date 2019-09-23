#
# spec file for package mozaddon-devel
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mozaddon-devel
Version:        1
Release:        0
Summary:        RPM macros for building Mozilla extensions under openSUSE
License:        SUSE-Public-Domain
Group:          Development/Tools/Other

Source2:        mozaddondev-getappid
Source3:        macros.mozaddon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       unzip
Requires:       perl(Archive::Zip)
Requires:       perl(XML::Simple)

%description
XPI ID retrieval script and helpful RPM macros for packaging up
addons for the Mozilla suite.

%prep

%build

%install
b="%buildroot";
mkdir -p "$b/%_bindir" "$b/%_sysconfdir/rpm";
install -pm0755 "%{S:2}" "$b/%_bindir/";
install -pm0644 "%{S:3}" "$b/%_sysconfdir/rpm/";

%files
%defattr(-,root,root)
%config %_sysconfdir/rpm/
%_bindir/moz*

%changelog
