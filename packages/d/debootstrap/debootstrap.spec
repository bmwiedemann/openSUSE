#
# spec file for package debootstrap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Frank Lichtenheld <frank@lichtenheld.de>
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


Name:           debootstrap
Version:        1.0.115
Release:        0
Summary:        Bootstrap a basic Debian system
License:        MIT
Group:          Development/Tools/Other
URL:            https://salsa.debian.org/installer-team/debootstrap
Source:         https://salsa.debian.org/installer-team/debootstrap/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-norootforbuild.patch
Requires:       wget
Recommends:     gpg2
BuildArch:      noarch

%description
debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this
by downloading .deb files from a mirror site, and carefully
unpacking them into a directory which can eventually be chrooted
into.

%prep
%setup -q
%patch0 -p1

%build
# Nothing to build.

%install
%make_install
install -Dpm 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%license debian/copyright
%doc README TODO debian/changelog
%{_sbindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
