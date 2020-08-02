#
# spec file for package dictd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           dictd
Version:        1.13.0
Release:        0
Summary:        DICT protocol (RFC 2229) server and command-line client
License:        GPL-1.0-or-later AND Zlib AND MIT
Group:          Productivity/Office/Dictionary
URL:            https://github.com/cheusov/dictd
Source0:        https://github.com/cheusov/dictd/archive/%{version}.tar.gz#/dictd-%{version}.tar.gz
Source1:        colorit.conf
Source2:        dictd.service
Patch0:         dictd-1.12.1-unused-return.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libdbi-devel
BuildRequires:  libmaa-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
# libtool-ltdl-devel  byacc
%if 0%{?suse_version}
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
%endif

%description
This package contains two programs. dict gives access to
electronic dictionaries on the Internet. With dictd, one can
set up a custom dictionary. To look up, for example, the word "grunt",
execute `dict grunt` at a command line. See the man pages of dict and
dictd for details.

%prep
%setup -q
%autopatch -p1

autoreconf -fv

%package devel
Summary:        Development files for dictd
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains two programs. dict gives access to
electronic dictionaries on the Internet. With dictd, one can
set up a custom dictionary. To look up, for example, the word "grunt",
execute `dict grunt` at a command line. See the man pages of dict and
dictd for details.

This package contains development files for the dictd package.

%build
export LDFLAGS="%{?__global_ldflags}" CPPFLAGS="%{optflags} -fPIC"
%configure --enable-dictorg --with-plugin-dbi
# --disable-plugin
make %{?_smp_mflags}

%install
%make_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/colorit.conf
cat <<EOF >%{buildroot}/%{_sysconfdir}/dictd.conf
global {
    #syslog
    #syslog_facility daemon
}

# Add database definitions here...

# We stop the search here
database_exit

# Add hidden database definitions here...

EOF

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/dictd.service

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdictd

# Makefile doesn't work correctly with libdir
if [ "x%{_libdir}" != "x%{_libexecdir}" ] ; then
    mkdir -p %{buildroot}%{_libdir}/
    mv -v %{buildroot}%{_libexecdir}/dictdplugin* %{buildroot}%{_libdir}/
fi
rm -fv %{buildroot}%{_libdir}/*.{la,a}

%pre
%service_add_pre dictd.service

%post
%service_add_post dictd.service
touch %{_localstatedir}/log/dictd
chmod 644 %{_localstatedir}/log/dictd

%preun
%service_del_preun dictd.service

%postun
%service_del_postun dictd.service

%files
%license COPYING
%doc ANNOUNCE NEWS README example*
%doc doc/dicf.ms doc/rfc.ms doc/rfc2229.txt doc/security.doc
%{_bindir}/dict*
%{_bindir}/colorit
%{_sbindir}/*dictd
%{_libdir}/dictdplugin_dbi.so*
%{_mandir}/man1/colorit*
%{_mandir}/man1/dict*
%{_mandir}/man8/dict*
%attr(0644,root,root) %{_unitdir}/dictd.service
%config(noreplace) %{_sysconfdir}/colorit.conf
%config(noreplace) %{_sysconfdir}/dictd.conf

%files devel
%license COPYING
%doc ANNOUNCE README TODO
%{_includedir}/*

%changelog
