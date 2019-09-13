#
# spec file for package update-checker
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


%if 0%{?is_opensuse}
%define service_list update-checker.service update-checker.timer
%else
%define service_list update-checker-migration.service update-checker.service update-checker-migration.timer update-checker.timer
%endif

%define rb_build_versions %{rb_default_ruby}
%define rb_build_abi      %{rb_default_ruby_abi}
%define rb_suffix         %{rb_default_ruby_suffix}

Name:           update-checker
Version:        1.0+git20181210.70430e2
Release:        0
Summary:        Scripts to check for new updates and migration targets
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
Url:            https://github.com/thkukuk/update-checker
Source:         update-checker-%{version}.tar.xz
Patch:          update-checker.conf-CaaSP.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  libxslt-tools
BuildRequires:  python3
BuildRequires:  python3-lxml
Requires:       perl-Config-IniFiles
Requires:       perl-XML-Twig
# for system service macros
PreReq:         coreutils
%if !0%{?is_opensuse}
Requires:       %{rubygem inifile >= 3.0.0}
Requires:       %{rubygem suse-connect >= 0.3.11}
%endif
BuildArch:      noarch

%description
Files, scripts and configuration files for two systemd services:
one, which checks for new, not applied updates and one which checks
for new migration targets.

%prep
%setup -q
%if 0%{?is_susecaasp}
%patch -p0
%endif

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
%if 0%{?is_opensuse}
rm %{buildroot}/usr/lib/systemd/system/update-checker-migration.*
rm %{buildroot}/usr/sbin/update-checker-migration
rm %{buildroot}/usr/share/man/man8/update-checker-migration.*
%endif

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
%if !0%{?is_opensuse}
%{_sbindir}/update-checker-migration
%endif
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
