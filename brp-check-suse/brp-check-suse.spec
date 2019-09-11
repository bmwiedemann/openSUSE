#
# spec file for package brp-check-suse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           brp-check-suse
AutoReqProv:    off
Summary:        Build root policy check scripts
# we need the full perl because of XML Parsing and utf-8
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Requires:       perl
Version:        84.87+git20190702.bac0cab
Release:        0
Url:            https://github.com/openSUSE/brp-check-suse
#
# Note: don't rebuild this manually. Instead submit your patches
# for inclusion in the git repo at https://github.com/openSUSE/brp-check-suse
#
Source0:        %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global provfind sh -c "grep -v 'brp-desktop.data' | %__find_provides"
%global __find_provides %provfind

%description
This package contains all suse scripts called in the
build root checking or in parts implemeting SUSE policies.


%prep
%setup -q
%ifnarch x86_64 s390x ppc64 aarch64
rm brp-65-lib64-linux
%endif

%build
# nothing to do

%install
install -d $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d
mv brp*data $RPM_BUILD_ROOT/usr/lib/rpm/
cp -a brp-* $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d

%files
%defattr(-, root, root)
%license COPYING
/usr/lib/rpm/*

%changelog
