#
# spec file for package apt-cacher-ng
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define debian_release 1
Name:           apt-cacher-ng
Version:        3.1
Release:        0
Summary:        A caching proxy specialized for Linux distribution packages
License:        BSD-4-Clause AND MIT
Url:            http://www.unix-ag.uni-kl.de/~bloch/acng/
Source0:        http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}.orig.tar.xz
Source1:        http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}-%{debian_release}.debian.tar.xz
Source2:        %{name}.service
Source3:        %{name}.default
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow
Suggests:       cron
Suggests:       logrotate
%{?systemd_ordering}

%description
Apt-Cacher NG is a caching proxy for downloading packages from Debian-style
software repositories (or possibly from other types).

The main principle is that a central machine hosts the proxy for a local
network, and clients configure their APT setup to download through it.
Apt-Cacher NG keeps a copy of all useful data that passes through it, and when
a similar request is made, the cached copy of the data is delivered without
being re-downloaded.

Apt-Cacher NG has been designed from scratch as a replacement for apt-cacher,
but with a focus on maximizing throughput with low system resource
requirements. It can also be used as replacement for apt-proxy and approx with
no need to modify clients' sources.list files.

%prep
%setup -qa1
# systemd in openSUSE is at /usr/lib/
sed -i 's@lib/systemd@usr/&@' systemd/CMakeLists.txt

%build
%cmake -DDOCDIR=%{_docdir}/%{name} -DSDINSTALL:BOOL=ON -DSYSCONFDIR=%{_sysconfdir}
%make_jobs

%install

%cmake_install

# Add the service symlink
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Debian file to control daemon options
install -m 644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/default/%{name}

# Debian logrotate file
install -m 644 -D debian/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
# Debian cron file
install -m 755 -D debian/%{name}.cron.daily %{buildroot}%{_sysconfdir}/cron.daily/%{name}

# default configuration
for dir in log cache; do
    mkdir -p %{buildroot}%{_localstatedir}/$dir/%{name}
done

# Use our service file
install -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%pre
getent group apt-cacher-ng >/dev/null || \
	%{_sbindir}/groupadd -r apt-cacher-ng
getent passwd apt-cacher-ng >/dev/null || \
	%{_sbindir}/useradd -r -M -g apt-cacher-ng -s /sbin/nologin \
	-c "apt-cacher-ng proxy" apt-cacher-ng
%service_add_pre apt-cacher-ng.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/acng.conf
%config(noreplace) %{_sysconfdir}/%{name}/security.conf
%dir %{_sysconfdir}/default
%config(noreplace) %{_sysconfdir}/default/%{name}
%dir %{_sysconfdir}/avahi/services
%dir %{_sysconfdir}/avahi
%config %{_sysconfdir}/avahi/services/%{name}.service
%config %{_sysconfdir}/logrotate.d/%{name}
%attr (755,root,root) %{_sysconfdir}/cron.daily
%config %{_sysconfdir}/cron.daily/%{name}
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_libexecdir}/%{name}/
%{_docdir}/%{name}/
%{_mandir}/man8/*.8%{ext_man}
%dir %{_unitdir}
%{_unitdir}/%{name}.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%dir %ghost /run/%{name}
%dir %{_localstatedir}/log/%{name}
%dir %{_localstatedir}/cache/%{name}

%changelog
