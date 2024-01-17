#
# spec file for package icecast
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           icecast
Version:        2.4.4
Release:        0
Summary:        Audio Streaming Server
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Servers
Url:            http://www.icecast.org/
Source:         http://downloads.xiph.org/releases/icecast/icecast-%{version}.tar.gz
Source2:        icecast.service
Source3:        icecast.logrotate
Source99:       icecast.rpmlintrc
# PATCH-MISSING-TAG -- See http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         icecast-2.3.1_runas_icecast_user.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         icecast-fix-no-add-needed.patch
Patch3:         icecast-add_pidfile_directive.patch
# PATCH-FEATURE-OPENSUSE -- mp3 frame validation
Patch100:       icecast-mp3-frame-validation.patch
BuildRequires:  curl-devel
BuildRequires:  dos2unix
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  speex-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow
Recommends:     logrotate
%{?systemd_requires}

%description
Icecast is a MP3 and OGG streaming server able to serve many clients
with MP3 and OGG audio.

%package doc
Summary:        Documentation for Icecast
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Icecast is a MP3 and OGG streaming server able to serve many clients
with MP3 and OGG audio.

This package contains the upstream HTML documentation and the sample
configuration files from upstream.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch100 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install docdir=%{_docdir}/%{name}
# service file
install -d -m 0755 %{buildroot}%{_sbindir}
install -d "%{buildroot}%{_unitdir}/system"
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/icecast.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# create missing dirs
install -d -m 0755 %{buildroot}%{_localstatedir}/{lib,log}/%{name}

# logrotate
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# fix warning about bad line endings
dos2unix %{buildroot}%{_docdir}/icecast/assets/css/style.css

%pre
%{_sbindir}/groupadd -r %{name} >/dev/null 2>&1 || :
%{_sbindir}/useradd  -g %{name} -s /bin/false -r -c "Icecast streaming server" -d %{_localstatedir}/lib/%{name} %{name} >/dev/null 2>&1 || :
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%dir %doc %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/ChangeLog
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}.xml
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/icecast
%{_datadir}/icecast
%{_sbindir}/rc%{name}
%config %{_unitdir}/%{name}.service
# TODO: enable chroot support in this dir
%{_localstatedir}/lib/%{name}
%attr(750,%{name},%{name}) %{_localstatedir}/log/%{name}

%files doc
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README
%exclude %{_docdir}/%{name}/AUTHORS
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/TODO
%exclude %{_docdir}/%{name}/ChangeLog

%changelog
