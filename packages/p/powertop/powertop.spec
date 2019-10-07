#
# spec file for package powertop
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           powertop
Version:        2.11
Release:        0
#Git-Clone:	git://github.com/fenrus75/powertop
Summary:        A Linux Tool to Find out What is Using Power on a Laptop
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://01.org/powertop/
#Source0:        https://01.org/sites/default/files/downloads/#{name}-v#{version}.tar.gz
Source0:        https://01.org/sites/default/files/downloads/powertop-v2.11-1-g7ef7f79.tar_0.gz
Source1:        powertop.service
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
%{?systemd_requires}

%description
PowerTOP is a program that collects the various pieces of information
from your system and presents an overview of how well your laptop is
doing in terms of power savings.

%lang_package

%prep
%setup -q -n powertop-v2.11-1-g7ef7f79

# Delete objects files left in tarball
find . -name '*.o' -delete

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE"
%configure
make %{?_smp_mflags} V=1

%install
%make_install
install -Dd %{buildroot}%{_localstatedir}/cache/powertop
touch %{buildroot}%{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/powertop.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%find_lang %{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
# Hack for powertop not to show warnings on first start
touch %{_localstatedir}/cache/powertop/saved_parameters.powertop
touch %{_localstatedir}/cache/powertop/saved_results.powertop

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README
%dir %{_localstatedir}/cache/powertop
%ghost %{_localstatedir}/cache/powertop/saved_parameters.powertop
%ghost %{_localstatedir}/cache/powertop/saved_results.powertop
%{_sbindir}/%{name}
%{_mandir}/man8/powertop.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_datadir}/bash-completion/completions/powertop

%files lang -f %{name}.lang

%changelog
