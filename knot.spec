#
# spec file for package knot
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1320
%bcond_without  dnstap
%bcond_without  lto
%else
%bcond_with     dnstap
%bcond_with     lto
%endif
%if 0%{?suse_version} > 1310
%bcond_without  rosedb
%else
%bcond_with     rosedb
%endif
%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif

Name:           knot
Version:        1.6.8
Release:        0
%define pkg_name knot
Summary:        An authoritative DNS daemon
License:        GPL-3.0+
Group:          Productivity/Networking/DNS/Servers
Url:            http://www.knot-dns.cz
Source0:        https://secure.nic.cz/files/knot-dns/%{pkg_name}-%{version}.tar.xz
Source1:        knot.conf
Source2:        knot.service
Patch0:         0001-loosen-openssl-dependency.patch
Patch1:         0002-make-configure.ac-compatible-with-old-tools.patch
#PATCH-FIX-UPSTREAM fix openssl 1.1+ build
Patch2:         knot-openssl-1.1+.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  liburcu-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  xz
Requires(pre):  pwdutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with rosedb}
BuildRequires:  lmdb-devel
%endif
%if 0%{?suse_version} > 1140 && ( 0%{?suse_version} != 1315 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ))
BuildRequires:  makeinfo
BuildRequires:  python-Sphinx
%endif
%if %{with dnstap}
BuildRequires:  libfstrm-devel
BuildRequires:  libprotobuf-c-devel >= 1.0.0
BuildRequires:  protobuf-c >= 1.0.0
%endif
%if %{with systemd}
%define has_systemd 1
BuildRequires:  systemd-devel
%{?systemd_requires}
%endif
Conflicts:      knot2

%description
Knot DNS is a high-performance authoritative DNS server implementation.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fvi
%configure \
  --sysconfdir=%{_sysconfdir} \
  --libexecdir=%{_libexecdir}/%{pkg_name} \
  --localstatedir=%{_localstatedir} \
  --includedir=%{_includedir}/knot/ \
  --disable-static \
  --enable-recvmmsg=yes \
%if %{with lto}
  --enable-lto=yes \
%endif
%if %{with dnstap}
  --enable-dnstap=yes \
%endif
%if %{with rosedb}
  --enable-rosedb \
%endif
%if %{with systemd}
  --enable-systemd=yes \
%endif
  --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}%{_docdir}/%{pkg_name}
install -d %{buildroot}%{_docdir}/%{pkg_name}/samples/
rm %{buildroot}%{_sysconfdir}/%{pkg_name}/*
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%if %{with systemd}
install -d %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE2} %{buildroot}%{_unitdir}/%{pkg_name}.service
ln -s service %{buildroot}%{_sbindir}/rcknot
%endif
install -p -m644 COPYING AUTHORS NEWS THANKS README %{buildroot}%{_docdir}/%{pkg_name}
install -p -m644 samples/*.conf samples/*.zone* %{buildroot}%{_docdir}/%{pkg_name}/samples/
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_libdir}/*.so

%pre
getent group knot >/dev/null || groupadd -r knot
getent passwd knot >/dev/null || \
  useradd -r -g knot -d %{_sysconfdir}/knot -s /sbin/nologin \
  -c "Knot DNS server" knot
%if %{with systemd}
%service_add_pre %{pkg_name}.service
%endif

%if %{with systemd}
%preun
%service_del_preun %{pkg_name}.service
%endif

%post
/sbin/ldconfig
%if %{with systemd}
%service_add_post %{pkg_name}.service
%endif

%postun
/sbin/ldconfig
%if %{with systemd}
%service_del_postun %{pkg_name}.service
%endif

%files
%defattr(-,root,root)
%dir %attr(750,root,root) %{_sysconfdir}/%{pkg_name}
%config(noreplace) %{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man?/*
%doc %{_docdir}/%{pkg_name}
%if %{with systemd}
%{_unitdir}/%{pkg_name}.service
%endif

%changelog
