#
# spec file for package liboping
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           liboping
Version:        1.9.0
Release:        0
%define         soname 0
Summary:        Multiple Host Ping Library that supports ICMPv4 and ICMPv6
Source:         http://verplant.org/liboping/files/liboping-%{version}.tar.bz2
Source2:        baselibs.conf
Source99:       %{name}-rpmlintrc
Patch1:         liboping-perl_vendor.patch
Patch2:         liboping-conditional_IPV6_TCLASS.patch
Url:            http://verplant.org/liboping/
Group:          System/Libraries
License:        LGPL-2.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.65
BuildRequires:  automake
BuildRequires:  gcc  
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  libtool

%description
liboping is a C library for measuring network latency using ICMP echo
requests. It can send to and receive packets from multiple hosts in parallel,
which is nice for monitoring applications. Both IPv4 and IPv6 are supported
transparently for the programmer and user.

%package -n liboping%{soname}
Summary:        Multiple Host Ping Library that supports ICMPv4 and ICMPv6
Group:          System/Libraries
Provides:       liboping = %{version}-%{release}

%description -n liboping%{soname}
liboping is a C library for measuring network latency using ICMP echo
requests. It can send to and receive packets from multiple hosts in parallel,
which is nice for monitoring applications. Both IPv4 and IPv6 are supported
transparently for the programmer and user.

A program called oping is available on the oping package to show the
simplicity and potential of the library and provide the functionality at the
command line.

%package -n liboping-devel
Summary:        Multiple Host Ping Library that supports ICMPv4 and ICMPv6
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries/Other

%description -n liboping-devel
liboping is a C library for measuring network latency using ICMP echo
requests. It can send to and receive packets from multiple hosts in parallel,
which is nice for monitoring applications. Both IPv4 and IPv6 are supported
transparently for the programmer and user.

This package includes the header and shared library link, required for
building applications or libraries that use %{name}.
This package is not needed at runtime.

%package -n oping
Summary:        Multiple Host Ping that supports ICMPv4 and ICMPv6
Requires:       %{name} = %{version}-%{release}
Group:          Productivity/Networking/Other
License:        GPL-2.0

%description -n oping
oping is for measuring network latency using ICMP echo requests. It can send
to and receive packets from multiple hosts in parallel, which is nice for
monitoring applications. Both IPv4 and IPv6 are supported transparently.

%package -n noping
Summary:        Multiple Host Ping that supports ICMPv4 and ICMPv6
Requires:       %{name} = %{version}-%{release}
Group:          Productivity/Networking/Other
License:        GPL-2.0

%description -n noping
noping continuously pings lists of hosts, displays ping statistics "live"
and highlights aberrant round-trip times.

%package -n perl-Net-Oping
Summary:        Multiple Host Ping that supports ICMPv4 and ICMPv6
Group:          Development/Libraries/Perl
Requires:       perl = %{perl_version}

%description -n perl-Net-Oping
Net::Oping is for measuring network latency using ICMP echo requests.
It can send to and receive packets from multiple hosts in parallel, which is
nice for monitoring applications. Both IPv4 and IPv6 are supported
transparently.

%prep
%setup -q
%patch1 -p0
%patch2 -p1

%__sed -i 's/-Werror//g' src/Makefile*
# Do not use versioned automake binary for backward compatibility
%__sed -i 's/-${am__api_version}//g' configure

%build
aclocal && automake
%configure \
    --with-perl-bindings="INSTALLDIRS=vendor"
%__make -C bindings perl/Makefile

make %{?_smp_mflags}

%install
%__sed -e 's|perl5/site_perl/|perl5/vendor_perl/|g' bindings/perl/Makefile
%makeinstall
%__rm "%{buildroot}%{_libdir}"/*.la

%perl_process_packlist

%__rm -f "%{buildroot}/var/adm/perl-modules/%{name}"

%post   -n liboping%{soname} -p /sbin/ldconfig

%postun -n liboping%{soname} -p /sbin/ldconfig

%files -n liboping%{soname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/liboping.so.%{soname}
%{_libdir}/liboping.so.%{soname}.*.*

%files -n liboping-devel
%defattr(-,root,root)
%{_includedir}/oping.h
%{_libdir}/liboping.so
%{_libdir}/liboping.a
%{_libdir}/pkgconfig/liboping.pc
%{_mandir}/man3/*.3%{ext_man}

%files -n oping
%defattr(-,root,root)
%{_bindir}/oping
%{_mandir}/man8/oping.8%{ext_man}

%files -n noping
%defattr(-,root,root)
%{_bindir}/noping

%files -n perl-Net-Oping
%defattr(-,root,root)
%dir %{perl_vendorarch}/Net
%{perl_vendorarch}/Net/Oping.pm
%dir %{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Net/Oping
%{perl_man3dir}/Net::Oping.%{perl_man3ext}%{ext_man}

%changelog
