#
# spec file for package ivtv
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


Name:           ivtv
BuildRequires:  gcc-c++
Url:            http://ivtvdriver.org/index.php/Main_Page
ExclusiveArch:  %ix86 ppc ppc64 x86_64
Version:        1.4.0
Release:        0
Summary:        Driver Implementation for iCompression or Conexant Video Capture Cards
License:        GPL-2.0
Group:          Productivity/Multimedia/Other
Source0:        %{name}-utils-%{version}.tar.bz2
Source1:        preamble
Patch0:         ivtv-optflags.patch
Patch1:         ivtv-splice.patch
Patch2:         ivtv-buffer.patch
Requires:       v4l-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The primary goal of the IVTV project is to provide a "clean room" Linux
open source driver implementation for video capture cards based on the
iCompression iTVC15 or Conexant CX23415/CX23416 MPEG Codec. Examples of
such cards are the Hauppauge PVR 250/350 series of MPEG video capture
cards, the Hauppauge "freestyle", and the AVerMedia M179 AVerTV. The
freestyle has not been tested, but it should work or at least be easy
to get working.

%prep
%setup -q -n ivtv-utils-%{version}
%patch0
%patch1
%patch2

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
# build utils
make -C utils

%install
# install utils
mkdir -p "%{buildroot}/usr/bin"
make -C utils DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr install
# install suspend file
mkdir -p "%{buildroot}/usr/lib/pm/config.d"
echo "SUSPEND_MODULES=\"ivtv\"" > %{buildroot}/usr/lib/pm/config.d/ivtv.config
# Remove ivtv-ctl and v4l2-ctl which are now provided by v4l-utils package (avoid conflicts during installation)
rm -f %{buildroot}/usr/bin/ivtv-ctl
rm -f %{buildroot}/usr/bin/v4l2-ctl

#
rm -fv doc/install.txt.orig
# not packaged ATM
rm -f %{buildroot}/usr/include/linux/ivtv.h
rm -f %{buildroot}/usr/include/linux/ivtvfb.h

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog doc utils/ivtvfwextract.pl
/usr/bin/*
%dir /usr/lib/pm
%dir /usr/lib/pm/config.d
/usr/lib/pm/config.d/ivtv.config

%changelog
