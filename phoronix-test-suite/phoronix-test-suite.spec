#
# spec file for package phoronix-test-suite
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


Name:           phoronix-test-suite
Version:        7.8.0
Release:        0
Summary:        Comprehensive test and benchmarking platform
License:        GPL-3.0
Group:          System/Benchmark
Url:            http://www.phoronix-test-suite.com/
Source0:        http://www.phoronix.net/downloads/phoronix-test-suite/releases/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
Requires:       php
Requires:       php-curl
Requires:       php-dom
Requires:       php-gd
Requires:       php-json
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-posix
Requires:       php-sockets
Requires:       php-zip
Requires:       xdg-utils
BuildArch:      noarch
%systemd_requires

%description
The Phoronix Test Suite can be used for simply comparing your
computer's performance or internal quality assurance purposes under
Linux. Results from the Phoronix Test Suite are displayed in a results
viewer with optional support for uploading them to PTS Global. This
software is based upon the internal tools and extensive Linux
benchmarking work done by Phoronix since 2004, with input from tier-one
computer hardware vendors. The Phoronix Test Suite ships with over 50
tests and 20 suites.

%prep
%setup -q -n %{name}

%build

%install
export DESTDIR=%{buildroot}
./install-sh ${_prefix}
%suse_update_desktop_file -i -n %{name}
%suse_update_desktop_file -i -n %{name}-launcher
%fdupes -s %{buildroot}
mkdir %{buildroot}%{_sbindir}
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcphoromatic-client
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcphoromatic-server

rm  %{buildroot}%{_datadir}/%{name}/pts-core/static/sample-pts-client-update-script.sh
rm  %{buildroot}%{_datadir}/%{name}/pts-core/external-test-dependencies/scripts/install-macports-packages.sh

%pre
%service_add_pre phoromatic-client.service phoromatic-server.service

%post
%if 0%{?suse_version} < 1330
%desktop_database_post
%icon_theme_cache_post
%mime_database_post
%endif
%service_add_post phoromatic-client.service phoromatic-server.service

%preun
%service_del_preun phoromatic-client.service phoromatic-server.service

%postun
%if 0%{?suse_version} < 1330
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif
%service_del_postun phoromatic-client.service phoromatic-server.service

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.md
%doc %{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/
%config(noreplace) %{_sysconfdir}/bash_completion.d/*
%{_datadir}/mime/packages/*
%dir %{_datadir}/appdata
%{_sbindir}/rcphoromatic-client
%{_sbindir}/rcphoromatic-server
%{_unitdir}/phoromatic-client.service
%{_unitdir}/phoromatic-server.service
%{_datadir}/appdata/phoronix-test-suite.appdata.xml

%changelog
