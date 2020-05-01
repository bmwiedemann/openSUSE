#
# spec file for package update-checker
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


%define service_list update-checker-migration.service update-checker.service update-checker-migration.timer update-checker.timer

%define rb_build_versions %{rb_default_ruby}
%define rb_build_abi      %{rb_default_ruby_abi}
%define rb_suffix         %{rb_default_ruby_suffix}

Name:           update-checker
Version:        1.1+git20200430.2de8b55
Release:        0
Summary:        Scripts to check for new updates and migration targets
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/thkukuk/update-checker
Source:         update-checker-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  libxslt-tools
BuildRequires:  python3
BuildRequires:  python3-lxml
Requires:       %{rubygem inifile >= 3.0.0}
Requires:       %{rubygem suse-connect >= 0.3.11}
Requires:       perl-Config-IniFiles
Requires:       perl-XML-Twig
BuildArch:      noarch

%description
Files, scripts and configuration files for two systemd services:
one, which checks for new, not applied updates and one which checks
for new migration targets.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%pre
%service_add_pre %{service_list}

%post
%service_add_post %{service_list}

%preun
%service_del_preun %{service_list}

%postun
%service_del_postun %{service_list}

%files
%license COPYING
%config /etc/update-checker.conf
%{_unitdir}
%{_sbindir}/update-checker
%{_sbindir}/update-checker-migration
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
