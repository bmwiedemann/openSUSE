#
# spec file for package xorg-x11-util-devel
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


Name:           xorg-x11-util-devel
Version:        7.6_1
Release:        0
Summary:        Compatibility metapackage for X11 development
License:        MIT
Group:          Development/Libraries/X11
Url:            http://xorg.freedesktop.org/
Source0:        README.meta

## Requires of packages that we split away from xorg-x11-util-devel
Requires:       gccmakedep
Requires:       imake
Requires:       lndir
Requires:       makedepend
Requires:       xorg-cf-files
Requires:       xorg-sgml-doctools
## End Requires of packages that we split away from xorg-x11-util-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package is a compatibility metapackage. It used to contain the
gccmakedep, imake, lndir, makedepend, xorg-cf-files, xorg-sgml-doctools
utilities.

%prep
%setup -c -T
cp %{SOURCE0} .

%build

%install

%files
%defattr(-,root,root)
%doc README.meta

%changelog
