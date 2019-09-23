#
# spec file for package rollback-helper
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


Name:           rollback-helper
Version:        1.0+git20181218.5394d6e
Release:        0
Summary:        Helper Scripts for system rollback
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/openSUSE/rollback-helper
Source:         rollback-helper-%{version}.tar.xz
Source1:        README.packaging.txt
Requires:       SUSEConnect
Supplements:    packageand(snapper:SUSEConnect)
BuildArch:      noarch
%{?systemd_requires}
# SUSEConnect does not build for i586 and s390 and is not supported on those architectures
# bsc#1088552
ExcludeArch:    %ix86 s390

%description
The rollback-helper package is a collection of scripts, which,
after a successfull filesystem rollback with snapper, resets
registered products on SCC or SMT.

%prep
%setup -q

%build

%install
install -d "%{buildroot}%{_prefix}/lib/snapper/plugins"
install -d "%{buildroot}/%{_var}/lib/rollback"
install -d "%{buildroot}%{_unitdir}"
install -d "%{buildroot}%{_sbindir}"
cp plugins/rollback %{buildroot}%{_prefix}/lib/snapper/plugins/
cp systemd/rollback.service %{buildroot}%{_unitdir}/
cp sbin/rollback-reset-registration %{buildroot}%{_sbindir}/

%pre
%service_add_pre rollback.service

%post
%service_add_post rollback.service

%preun
%service_del_preun rollback.service

%postun
%service_del_postun rollback.service

%files
%license COPYING
%dir %{_prefix}/lib/snapper
%dir %{_prefix}/lib/snapper/plugins
%{_prefix}/lib/snapper/plugins/rollback
%{_unitdir}/rollback.service
%{_sbindir}/rollback-reset-registration
%dir %{_var}/lib/rollback

%changelog
