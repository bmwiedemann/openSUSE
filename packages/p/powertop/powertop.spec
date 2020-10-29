#
# spec file for package powertop
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


Name:           powertop
Version:        2.13
Release:        0
Summary:        A Linux Tool to Find out What is Using Power on a Laptop
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://01.org/powertop/
Source0:        https://github.com/fenrus75/powertop/archive/v2.13.tar.gz
Source1:        powertop.service
# they repeatedly forget to upload a release tarball and only have the one from
# GitHub which doesnt contain configure thus adding:
# autoconf, autoconf-archive, automake, libtool
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(zlib)
%{?systemd_requires}

%description
PowerTOP is a program that collects the various pieces of information
from your system and presents an overview of how well your laptop is
doing in terms of power savings.

%lang_package

%prep
%setup -q -n powertop-%{version}

# Delete objects files left in tarball
find . -name '*.o' -delete

%build
# workaround for 'error: too many loops' in sle15sp3
# also see rhbz#1826935
autoreconf -fi || autoreconf -fi
export CFLAGS="%{optflags} -D_GNU_SOURCE"
%configure
%make_build

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
%doc README.md
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
