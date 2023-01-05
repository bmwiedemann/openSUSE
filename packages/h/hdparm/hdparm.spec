#
# spec file for package hdparm
#
# Copyright (c) 2023 SUSE LLC
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


Name:           hdparm
Version:        9.65
Release:        0
Summary:        A Program to get and set hard disk parameters
License:        SUSE-Permissive
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/hdparm/
Source:         https://downloads.sourceforge.net/project/hdparm/hdparm/hdparm-%{version}.tar.gz
Patch1:         hdparm-nostrip.patch
Patch2:         hdparm-wiper-warn.patch
Patch3:         hdparm-leak-fix.patch
Patch4:         hdparm-9.43-fix-bashisms.patch
# https://sourceforge.net/p/hdparm/patches/52/
Patch5:         avoid-linux-includes.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Requires(post): coreutils
Provides:       base:/sbin/hdparm

%description
A shell utility to access and tune the ioctl features of the Linux IDE
driver and IDE drives.

%prep
%setup -q
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%make_build CFLAGS="%{optflags} -Wall -Wstrict-prototypes" LDFLAGS= CC="gcc"
cp -p wiper/README.txt README.wiper

%install
mkdir -p "%{buildroot}%{_mandir}/man8"
install -d "%{buildroot}/%{_sbindir}"
%make_install binprefix="%{_prefix}"
mv contrib/README contrib/README.contrib
install -d "%{buildroot}%{_libexecdir}/hdparm"
install -m 755 contrib/idectl "%{buildroot}%{_libexecdir}/hdparm"
install -m 755 contrib/ultrabayd "%{buildroot}%{_libexecdir}/hdparm"
install -m 755 wiper/wiper.sh "%{buildroot}/%{_sbindir}"
%if 0%{?suse_version} < 1550
mkdir -p "%{buildroot}/sbin"
ln -sf %{_sbindir}/wiper.sh "%{buildroot}/sbin"
ln -sf %{_sbindir}/hdparm "%{buildroot}/sbin"
%endif

%files
%license LICENSE.TXT
%doc Changelog README.acoustic contrib/README.contrib README.wiper
%{_mandir}/man8/hdparm.8%{?ext_man}
%if 0%{?suse_version} < 1550
/sbin/hdparm
/sbin/wiper.sh
%endif
%{_sbindir}/hdparm
%{_sbindir}/wiper.sh
%{_libexecdir}/hdparm

%changelog
