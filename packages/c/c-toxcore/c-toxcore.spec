#
# spec file for package c-toxcore
#
# Copyright (c) 2024 SUSE LLC
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
%define _soversion 2
Name:           c-toxcore
Version:        0.2.19
Release:        0
Summary:        Secure decentralized instant messaging application
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://tox.chat/
Source0:        https://github.com/TokTok/c-toxcore/archive/v%{version}.tar.gz#./%{name}-%{version}.tar.gz
Source1:        %{name}-user.conf
Source2:        %{name}.tmpfiles.d
# Dont't find right key at this time. :(
#Source3:        https://github.com/TokTok/c-toxcore/releases/download/v%%{version}/%%{name}-%%{version}.tar.gz.asc
Source4:        %{name}.keyring
Source10:       https://github.com/camgunz/cmp/archive/v20/cmp-v20.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libconfig-devel
BuildRequires:  libopus-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  libvpx-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
Requires(pre):  shadow
Provides:       bundled(cmp) = 20
%sysusers_requires
%{?systemd_requires}

%description
Project Tox, also known as Tox, is a FOSS instant messaging
application aimed to replace Skype.
With the rise of government monitoring programs,
Tox provides an easy to use application that allows you to connect
with friends and family without anyone else listening in.
While other big-name services require you to pay for features,
Tox is totally free and comes without advertising

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libtoxcore%{_soversion} = %{version}

%description devel
Development libraries and headers needed to build software using %{name}.

%package daemon
Summary:        Bootstrap-daemon for toxcore
Group:          Productivity/Networking/Instant Messenger

%description daemon
Bootstrap-daemon to dispose hashtable for toxcore.

%package -n libtoxcore%{_soversion}
Summary:        Core library for toxcore
Group:          System/Libraries

%description -n libtoxcore%{_soversion}
This are the Core library for toxcore.

%prep
%autosetup -p1
# install submodules
pushd third_party/cmp
tar -xvzf %{SOURCE10} --strip 1
popd
# change location of bootstrap bin
sed -ri 's:%{_prefix}/local/bin/tox-bootstrapd:%{_bindir}/tox-bootstrapd:g' other/bootstrap_daemon/tox-bootstrapd.service
# change user and of bootstrapd
sed -ri 's:User=tox-bootstrapd:User=tox:g' other/bootstrap_daemon/tox-bootstrapd.service
sed -ri 's:Group=tox-bootstrapd:Group=toxcmd:g' other/bootstrap_daemon/tox-bootstrapd.service
# change location of bootstrap kyes
sed -ri 's:%{_localstatedir}/lib/tox-bootstrapd/keys:%{_sysconfdir}/tox/bootstrapd/keys:g' other/bootstrap_daemon/tox-bootstrapd.conf

%build
# system user config
%sysusers_generate_pre %{SOURCE1} %{name} %{name}-user.conf
# SHARED_LIBS=ON produces a stray libmisc_tools.so which is not part of `make install`.
# SHARED_LIBS=OFF still produces libtoxcore.so.2, so... *shrug*
#
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DBUILD_TOXAV=ON \
      -DMUST_BUILD_TOXAV=ON \
      -DBOOTSTRAP_DAEMON=ON \
      -DDHT_BOOTSTRAP=ON \
      -DENABLE_STATIC=OFF  \
      -DBUILD_SHARED_LIBS:BOOL=OFF \
      ..

%cmake_build

%install
%cmake_install

# system user config
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}-user.conf

# Install dir /var/run/graylog2-server
install -d -m 0755 %{buildroot}%{_prefix}/lib/tmpfiles.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/tox-bootstrapd.conf

# Install dir /var/lib/tox-bootstrapd
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/tox-bootstrapd/
# Install dir /etc/tox/bootstrapd/keys
install -d -m 0700 %{buildroot}%{_sysconfdir}/tox/bootstrapd/keys

# Install dir /etc and bootstrap-config
mkdir -p %{buildroot}/%{_sysconfdir}
install -D -m 0640 other/bootstrap_daemon/tox-bootstrapd.conf %{buildroot}%{_sysconfdir}/tox/bootstrapd/tox-bootstrapd.conf

# Install init-scripts
mkdir -p %{buildroot}/%{_sbindir}
install -D -m 0644 other/bootstrap_daemon/tox-bootstrapd.service %{buildroot}%{_unitdir}/tox-bootstrapd.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rctox-bootstrapd

%pre daemon -f %{name}.pre
%service_add_pre tox-bootstrapd.service

%post daemon
%service_add_post tox-bootstrapd.service
systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/tox-bootstrapd.conf

%post -n libtoxcore%{_soversion} -p /sbin/ldconfig

%preun daemon
%service_del_preun tox-bootstrapd.service

%postun daemon
%service_del_postun tox-bootstrapd.service

%postun -n libtoxcore%{_soversion} -p /sbin/ldconfig

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/tox
%{_includedir}/tox/*

%files
%license LICENSE
%doc README.md DONATORS CHANGELOG.md

%files daemon
%dir %{_sysconfdir}/tox
%dir %{_sysconfdir}/tox/bootstrapd
%{_sysusersdir}/%{name}-user.conf
%config(noreplace) %{_sysconfdir}/tox/bootstrapd/tox-bootstrapd.conf
%{_datadir}/bash-completion/completions/tox-bootstrapd
%{_bindir}/DHT_bootstrap
%{_bindir}/tox-bootstrapd
%{_unitdir}/tox-bootstrapd.service
%{_tmpfilesdir}/tox-bootstrapd.conf
%{_sbindir}/rctox-bootstrapd
%dir %{_localstatedir}/lib/tox-bootstrapd
%dir %attr(0770,tox,toxcmd) %{_sysconfdir}/tox/bootstrapd/keys

%files -n libtoxcore%{_soversion}
%{_libdir}/libtoxcore.so.%{_soversion}*

%changelog
