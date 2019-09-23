#
# spec file for package isapnp
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


Name:           isapnp
Version:        1.26
Release:        0
Summary:        An ISA Plug and Play Configuration Utility
License:        GPL-2.0+
Group:          Hardware/Other
Source:         isapnptools-%{version}.tar.bz2
Source1:        boot.isapnp
Source2:        README.SUSE
Patch0:         isapnp-1.26-powerpc.diff
Patch2:         isapnp-autotools.diff
Patch3:         isapnp-codecleanup.diff
Patch4:         isapnp-static_nonstatic_mix.diff
BuildRequires:  automake
BuildRequires:  flex
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86

%description
Two programs--one allows the dumping of resource data and generation of
a skeleton configuration file, the other configures ISA PnP hardware
using a configuration file.

For more information, refer to:
%{_docdir}/isapnp/README.SUSE

%package devel
Summary:        ISA PnP library and headers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       isapnp:%{_includedir}/isapnp/pnp.h

%description devel
This package contains all that's needed to develop programs that use
libisapnp.

%prep
%setup -q -n isapnptools-%{version}
chmod u+x src/*
%patch0
%patch2
%patch3
%patch4

%build
%define warn_flags -W -Wall -Wstrict-prototypes -Wno-unused-parameter
rm -f acconfig.h
autoreconf -fiv
export CFLAGS="%{optflags} %{warn_flags}"
%configure \
  --sbindir=/sbin
touch src/isapnp_main.l
make all

%install
cp %{SOURCE2} .
make DESTDIR=%{buildroot} install
install -D -m 744 %{SOURCE1} %{buildroot}%{_initddir}/boot.isapnp

%post
%{fillup_and_insserv -y boot.isapnp}

%postun
%insserv_cleanup

%files
%defattr(-,root,root)
/sbin/isapnp
/sbin/pnpdump
%config %{_initddir}/boot.isapnp
%doc AUTHORS COPYING ChangeLog NEWS README README.SUSE
%doc doc/isapnpfaq.txt
%{_mandir}/man5/*.5%{ext_man}
%{_mandir}/man8/*.8%{ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/isapnp
%{_libdir}/libisapnp.a

%changelog
