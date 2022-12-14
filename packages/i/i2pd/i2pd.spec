#
# spec file for package i2pd
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 PurpleI2P team
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


%define sysuser i2pd
%define sysgroup i2pd
Name:           i2pd
Version:        2.44.0
Release:        0
Summary:        C++ implementation of an I2P client
License:        BSD-3-Clause
Group:          Productivity/Networking/System
URL:            https://i2pd.website
Source0:        https://github.com/PurpleI2P/i2pd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libminiupnpc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow
Suggests:       logrotate
%{?systemd_requires}
%if 0%{?suse_version} < 1500
BuildRequires:  boost-devel
%else
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%endif

%description
The Invisible Internet Protocol (I2P) is a universal anonymous network layer. All
communications over I2P are anonymous and end-to-end encrypted, participants
don't reveal their real IP addresses.

This package contains a C++ implementation of an I2P router.

%prep
%setup -q

cp contrib/debian/i2pd.service i2pd.service.in
cp contrib/debian/i2pd.tmpfile i2pd.tmpfile.in

grep ^User=%{sysuser} i2pd.service.in || { echo '%{sysuser} not found'; exit 1; }
grep ^Group=%{sysgroup} i2pd.service.in || { echo '%{sysgroup} not found'; exit 1; }

#sed -i 's/\ \-\-daemon//' i2pd.service.in

%build
pushd build
%cmake \
    -DWITH_LIBRARY=OFF \
    -DWITH_UPNP=ON \
    -DBUILD_SHARED_LIBS=OFF
%make_build -j1
popd

%install
pushd build
%cmake_install
popd

cat debian/%{name}.install | while read _install; do
  ! echo $_install | grep '^%{name}' || continue
  mkdir -p $(echo $_install | sed 's|.*\ \+\(.*\)|%{buildroot}/\1|')
  cp -r $(echo $_install | sed 's|\(\ \+\)|\1%{buildroot}/|')
done

cat debian/%{name}.links | while read _links; do
  mkdir -p $(echo $_links | sed 's|.*\ \+\(.*\)/.*|%{buildroot}/\1|')
  ln -s $(echo $_links | sed 's|\(.*\ \+\)|/\1%{buildroot}/|')
done

mkdir -p %{buildroot}%{_sysconfdir}/i2pd/tunnels.conf.d
cp -rf contrib/tunnels.d/README %{buildroot}%{_sysconfdir}/i2pd/tunnels.conf.d

install -Dm0644 %{name}.service.in %{buildroot}%{_unitdir}/%{name}.service
install -Dm0644 %{name}.tmpfile.in %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -Dm0644 debian/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dm0644 {debian,%{buildroot}%{_mandir}/man1}/%{name}.1

install -d %{buildroot}%{_sbindir}
mv %{buildroot}{%{_bindir},%{_sbindir}}/%{name}

find %{buildroot} -regex ".*\(\.a\|\/src\|LICENSE\)" -exec rm -Rf '{}' +

%pre
%service_add_pre %{name}.service
getent group %{sysgroup} >/dev/null || groupadd -r %{sysgroup}
if ! getent passwd %{sysuser} >/dev/null; then
    useradd -r -g %{sysgroup} -d %{_localstatedir}/lib/i2pd -s /sbin/nologin -c "user for i2pd" %{sysuser}
fi
exit 0

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc ChangeLog README.md
%{_sbindir}/i2pd
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.i2pd
%config %{_sysconfdir}/logrotate.d/i2pd
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_mandir}/man?/i2pd.?%{ext_man}
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_datadir}/i2pd
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_datadir}/i2pd/certificates
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_datadir}/i2pd/certificates/family
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_datadir}/i2pd/certificates/reseed
%{_datadir}/i2pd/certificates/family/
%{_datadir}/i2pd/certificates/reseed/
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_localstatedir}/lib/i2pd
%{_localstatedir}/lib/i2pd/
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_sysconfdir}/i2pd
%attr(0750,%{sysuser},%{sysgroup}) %dir %{_sysconfdir}/i2pd/tunnels.conf.d
%config(noreplace) %{_sysconfdir}/i2pd/i2pd.conf
%config(noreplace) %{_sysconfdir}/i2pd/subscriptions.txt
%config(noreplace) %{_sysconfdir}/i2pd/tunnels.conf
%{_sysconfdir}/i2pd/tunnels.conf.d/README

%changelog
