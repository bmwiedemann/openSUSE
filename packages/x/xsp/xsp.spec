#
# spec file for package xsp
#
# Copyright (c) 2020 SUSE LLC.
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


%define xspConfigsLocation %{_sysconfdir}/xsp/2.0
%define xspAvailableApps %{xspConfigsLocation}/applications-available
%define xspEnabledApps %{xspConfigsLocation}/applications-enabled
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           xsp
Version:        4.7.1
Release:        0
Summary:        Web Server Hosting ASP.NET
License:        MIT
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/mono/xsp
Source:         https://github.com/mono/xsp/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xsp.conf
Patch1:         %{name}-3.0.11-fix-bashisms.patch
Patch2:         mono-440-build-fix.patch
Patch3:         mono-4-install.patch
Patch4:         xsp-add-systemd-support.patch
Patch5:         asp-state4-signals.patch
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  mono-data-oracle
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel >= 2.10.0
BuildRequires:  mono-web
BuildRequires:  monodoc-core
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
Requires:       libfpm_helper0 = %{version}
%{?systemd_ordering}
%if 0%{?suse_version} >= 1330
BuildRequires:  strip-nondeterminism
Requires(post): group(www)
Requires(post): user(wwwrun)
Requires(pre):  group(www)
Requires(pre):  user(wwwrun)
%endif

%description
The XSP server is a Web server that hosts the Mono System.Web
classes for running what is commonly known as ASP.NET.

%package -n libfpm_helper0
Summary:        Mono.WebServer.FPM Helper
Group:          System/Libraries

%description -n libfpm_helper0
Library of Mono.WebServer.FPM Helper.

%package -n libfpm_helper-devel
Summary:        Development files of libfpm_helper0
Group:          Development/Libraries/C and C++
Requires:       libfpm_helper0 = %{version}

%description -n libfpm_helper-devel
Development Files of libfpm_helper0.

%define mcsver %({ mcs --version | awk '{print $5}' | cut -f1 -d"." ; mcs --version | awk '{print $5}' | cut -f2 -d"." ; } | xargs printf "%03d")
%if 0%{?mcsver} >= 4000
%define target2_dir xsp2
%define target4_dir xsp4
%else
%define target2_dir 2.0
%define target4_dir 4.5
%endif

%prep
%setup -q
%patch1 -p1
%if 0%{?mcsver} >= 4004
%patch2 -p1
%endif
%if 0%{?mcsver} >= 4000
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1

%build
NOCONFIGURE=1 ./autogen.sh
# Cannot use the configure macro because noarch-redhat-linux is not recognized by the auto tools in the tarball
./configure --prefix=%{_prefix} \
	    --libexecdir=%{_prefix}/lib \
	    --libdir=%{_prefix}/lib \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --sysconfdir=%{_sysconfdir}
%make_build

%install
[ -x %{_bindir}/strip-nondeterminism ] && strip-nondeterminism docs/Mono.FastCGI/Mono.FastCGI.zip docs/Mono.WebServer/Mono.WebServer.zip
%make_install
find %{buildroot}%{_prefix}/lib -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_prefix}/lib/xsp/unittests
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}
mkdir -p %{buildroot}/%{xspAvailableApps}
mkdir -p %{buildroot}/%{xspEnabledApps}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}/srv/xsp2
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}/run/xsp2
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d/
mkdir -p %{buildroot}%{_sbindir}
install -m 644 man/mono-asp-apps.1 %{buildroot}%{_mandir}/man1/mono-asp-apps.1
install -m 644 packaging/opensuse/sysconfig.xsp2 %{buildroot}%{_fillupdir}
install -m 644 packaging/opensuse/xsp2.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/xsp2
# new {
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
install -m 755 packaging/opensuse/xsp2.init %{buildroot}%{_datadir}/%{name}/scripts
mkdir -p %{buildroot}%{_unitdir}
install -m 644 packaging/opensuse/xsp2.service %{buildroot}%{_unitdir}/xsp2.service
# } end new
install -m 755 tools/mono-asp-apps/mono-asp-apps %{buildroot}%{_bindir}/mono-asp-apps
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/
ln -s service %{buildroot}%{_sbindir}/rcxsp2
%fdupes %{buildroot}/%{_prefix}

%pre
%service_add_pre xsp2.service

%post
install -d -m 0711 --owner=wwwrun --group=www /run/xsp2
%service_add_post xsp2.service

%preun
%service_del_preun xsp2.service

%postun
%service_del_postun xsp2.service

%post -n libfpm_helper0 -p /sbin/ldconfig
%postun -n libfpm_helper0 -p /sbin/ldconfig

%files -n libfpm_helper0
%{_prefix}/lib/libfpm_helper.so.0.0.0

%files -n libfpm_helper-devel
%{_prefix}/lib/libfpm_helper.so
%{_prefix}/lib/libfpm_helper.so.0

%files
%doc NEWS README
%{_bindir}/*
%{_datadir}/pkgconfig/*
%dir %{_prefix}/lib/mono/%{target4_dir}
%{_prefix}/lib/mono/%{target4_dir}/Mono.WebServer2.dll
%{_prefix}/lib/mono/%{target4_dir}/fastcgi-mono-server4.exe
%{_prefix}/lib/mono/%{target4_dir}/mod-mono-server4.exe
%{_prefix}/lib/mono/%{target4_dir}/xsp4.exe
%{_prefix}/lib/mono/%{target4_dir}/mono-fpm.exe
%{_prefix}/lib/mono/gac/Mono.WebServer2
%{_prefix}/lib/mono/gac/fastcgi-mono-server4
%{_prefix}/lib/mono/gac/mod-mono-server4
%{_prefix}/lib/mono/gac/xsp4
%{_prefix}/lib/mono/gac/mono-fpm
%{_prefix}/lib/monodoc/sources/Mono.WebServer.*
%{_prefix}/lib/monodoc/sources/Mono.FastCGI.*
%{_prefix}/lib/xsp
%{_mandir}/*/*
# new {
%{_datadir}/%{name}
%{_unitdir}/xsp2.service
# } end new
%config %{_sysconfdir}/logrotate.d/xsp2
%{_fillupdir}/*
%attr(0711,wwwrun,www) /srv/xsp2
%ghost %attr(0711,wwwrun,www) /run/xsp2
%{_prefix}/lib/tmpfiles.d/
%{_sysconfdir}/%{name}
%{_sbindir}/rcxsp2

%changelog
