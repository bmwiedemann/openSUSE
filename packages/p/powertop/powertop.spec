#
# spec file for package powertop
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.16
Release:        0
Summary:        A Linux Tool to Find out What is Using Power on a Laptop
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://01.org/powertop/
Source0:        https://github.com/fenrus75/powertop/archive/v%{version}.tar.gz
Source1:        powertop.service
Source2:        powertop.conf
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libtracefs-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(bash-completion)
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
%meson -Denable-tests=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/powertop %{buildroot}%{_sbindir}/powertop
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/powertop.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
%find_lang %{name}
# remove shebang from bash completion file
sed -i '1s/^#!.*//' %{buildroot}%{_datadir}/bash-completion/completions/powertop

%check
%meson_test

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README.md
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%{_sbindir}/%{name}
%{_mandir}/man8/powertop.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_datadir}/bash-completion/completions/powertop
%ghost %attr(0755,-,-) %dir %{_localstatedir}/cache/%{name}
%ghost %attr(0644,-,-) %{_localstatedir}/cache/%{name}/saved_parameters.powertop
%ghost %attr(0644,-,-) %{_localstatedir}/cache/%{name}/saved_results.powertop

%files lang -f %{name}.lang

%changelog
