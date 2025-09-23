#
# spec file for package bird
#
# Copyright (c) 2025 SUSE LLC
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

%define bird_runtimedir %{_rundir}/bird
Name:           bird3
Version:        3.1.4
Release:        0
Summary:        The BIRD Internet Routing Daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Routing
URL:            https://bird.network.cz/
Source:         https://bird.nic.cz/download/bird-%{version}.tar.gz
Source1:        bird.service
Source3:        bird.tmpfiles.d
Source4:        system-user-bird.conf
Source5:        https://bird.nic.cz/download/bird-doc-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires(pre):  shadow
Provides:       bird = %{version}-%{release}
Provides:       bird6 = %{version}
Provides:       bird6:%{_sbindir}/bird6
Obsoletes:      bird6 < %{version}
Provides:       bird-common = %{version}
Obsoletes:      bird-common < %{version}
%if 0%{?suse_version} < 1600
Conflicts:      bird < 3.0.0
%else
Obsoletes:      bird < 3.0.0
%endif

%description
The BIRD project aims to develop a fully functional dynamic IP routing daemon
primarily targeted on (but not limited to) Linux, FreeBSD and other UNIX-like
systems and distributed under the GNU General Public License.

Supports the following:

* Both IPv4 and IPv6
* Multiple routing tables
* BGP
* RIP
* OSPF
* BFD
* Babel
* Static routes
* IPv6 Router Advertisements
* Inter-table protocol
* Command-line interface (using the `birdc' client; to get some help, just press `?')
* Powerful language for route filtering

%package doc
Summary:        Documentation for the BIRD Internet Routing Daemon
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The BIRD project aims to develop a fully functional dynamic IP routing daemon
primarily targeted on (but not limited to) Linux, FreeBSD and other UNIX-like
systems and distributed under the GNU General Public License.

This package holds the PDF documentation.

%prep
%autosetup -p1 -n bird-%{version} -a 5

%build
export CFLAGS="%{optflags} -fpic -DPIC -fno-strict-aliasing -Wno-parentheses -Wno-pointer-sign"
export LDFLAGS="-Wl,-z,relro -pie"
%configure \
	--with-runtimedir=%{bird_runtimedir}
%make_build all
%sysusers_generate_pre %{SOURCE4} bird system-user-bird.conf

%install
%make_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/bird.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/bird.conf
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcbird
install -D -d -m 0750 %{buildroot}%{_docdir}/bird
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/system-user-bird.conf

%check
%make_build test

%pre -f bird.pre
%service_add_pre bird.service

%preun
%service_del_preun bird.service

%post
%tmpfiles_create %_tmpfilesdir/bird.conf
%service_add_post bird.service

%postun
%service_del_postun bird.service

%files
%config(noreplace) %attr(0640,root,bird) %{_sysconfdir}/bird.conf
%{_sbindir}/bird
%{_sbindir}/birdc
%{_sbindir}/birdcl
%{_sbindir}/rcbird
%{_unitdir}/bird.service
%{_sysusersdir}/system-user-bird.conf
%{_tmpfilesdir}/bird.conf
%dir %attr(-,bird,bird) %ghost %{bird_runtimedir}

%files doc
%doc NEWS README
%doc doc/bird.conf.*
%doc bird-doc-%{version}/doc/*.pdf

%changelog
