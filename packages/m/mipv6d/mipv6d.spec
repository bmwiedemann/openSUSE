#
# spec file for package mipv6d
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mipv6d
Version:        2.0.2.umip.0.4
Release:        0
Summary:        MIPL - Mobile IPv6 for Linux
License:        GPL-2.0
Group:          Productivity/Networking/Other
Url:            http://umip.org/
Source0:        mipv6-2.0.2-umip-0.4.tar.bz2
Source1:        mipv6d.service
Patch1:         mipv6-2.0.2-umip-0.4.diff
Patch2:         mipv6d-openssl11.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  indent
#BuildRequires:  libnetlink-devel
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MIPL Mobile IPv6 for Linux is an implementation of the Mobility Support
in IP version 6 (RFC 3775).

This user space part works together with Mobile IPv6 enabled Linux
kernels.  See INSTALL and any other documents referred there for
installation instructions and required kernel compile options.

MIPL Mobile IPv6 for Linux has been developed in the GO-Core Project at
the Helsinki University of Technology.	See AUTHORS for core
development team and THANKS for complete listing of contributors.

%prep
%setup -q -n mipv6-2.0.2-umip-0.4
%patch1 -p0
%patch2 -p1

%build
aclocal
autoheader
automake --foreign --copy --add-missing
autoconf
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# FIXME: you should use the %%configure macro
./configure \
	--disable-debug		\
	--prefix=%{_prefix}	\
	--sysconfdir=/etc
make %{?_smp_mflags} clean
make %{?_smp_mflags}

%install
%make_install
install -m0755 -d %{buildroot}%{_sysconfdir}
install -m0755 -d %{buildroot}%{_unitdir}
install -m0644    %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -sf            %{_sbindir}/service \
                  %{buildroot}%{_sbindir}/rcmipv6d
touch             %{buildroot}%{_sysconfdir}/mip6d.conf

%pre
%service_add_pre mipv6d.service

%post
%service_add_post mipv6d.service

%preun
%service_del_preun mipv6d.service

%postun
%service_del_postun mipv6d.service

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING README INSTALL.kernel README.IPsec NEWS
%doc extras/*
%doc licenses/*
%{_mandir}/man1/mip6d.1%{ext_man}
%{_mandir}/man5/mip6d.conf.5%{ext_man}
%{_mandir}/man7/mipv6.7%{ext_man}
%ghost %config(noreplace) %attr(600,root,root) %{_sysconfdir}/mip6d.conf
%{_unitdir}/%{name}.service
%{_sbindir}/mip6d
%{_sbindir}/rcmipv6d

%changelog
