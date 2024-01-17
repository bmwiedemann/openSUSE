#
# spec file for package eciadsl-usermode
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



Name:           eciadsl-usermode
Url:            http://eciadsl.flashtux.org
Summary:        A Beta-Quality Usermode Driver for the ECI ADSL USB Modem
Version:        0.11
Release:        132
License:        GPL-2.0+
Group:          Hardware/Other
Source0:        %name-%version.tar.bz2
Source1:        eciadsl-synch_bin.tar.bz2
Patch1:         eciadsl.patch
Patch2:         eciadsl-kernel-header.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         /usr

%description
This package contains the driver for the ECI Hi-Focus ADSL USB modem.
It also supports many USB ADSL modems based on the Globespan chipset.
It is not a kernel module. It is a user-mode program that handles the
modem. A kernel module is under development.

%prep
%setup -q -T -b 0 -a 1
%patch1
%patch2

%build
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure
make %{?_smp_mflags}

%install
	make DESTDIR=%buildroot install
        cp eciadsl-synch_bin/* %buildroot/etc/eciadsl

%post
echo "Now you need to configure the driver. Please read the README"
echo "and INSTALL files located in /usr/share/doc/packages/eciadsl-usermode."

%files
%defattr(-,root,root)
%_prefix/bin/*
%config(noreplace) /etc/eciadsl
%doc README* INSTALL* TROUBLESHOOTING* BUGS TODO rc.adsl

%changelog
