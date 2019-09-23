#
# spec file for package apache2-mod_evasive
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if %{apache_branch} >= 204
%define ap_suffix 24
%else
%define ap_suffix 20
%endif
Name:           apache2-mod_evasive
Version:        1.10.1
Release:        0
Summary:        Denial of Service evasion module for Apache
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Servers
#
# Only mod_evasive20.c (GPL-2.0+) is provided in object form.
# mod_evasive.c (GPL-2.0) and mod_evasiveNSAPI.c (non-OSI compliant)
# are merely shipped unmodified, fulfilling their terms.
#
Url:            http://zdziarski.com/blog/?page_id=442

Source:         http://zdziarski.com/blog/wp-content/uploads/2010/02/mod_evasive_%version.tar.gz
Source2:        mod_evasive.conf
Patch1:         modev-return.diff
Patch2:         mail-invocation.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  apache2-prefork
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  pcre-devel
Recommends:     mailx
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2

%description
mod_evasive is an evasive maneuvers module for Apache to provide
evasive action in the event of an HTTP DoS or DDoS attack or brute
force attack. It is also designed to be a detection and network
management tool, and can be easily configured to talk to ipchains,
firewalls, routers, and etcetera. mod_evasive presently reports
abuses via email and syslog facilities.

%prep
%setup -qn mod_evasive
%patch -P 1 -P 2 -p1

%build
cp -a %{S:2} .
%if %{ap_suffix} == 24
# create apache httpd-2.4 version and compile it
sed 's/connection->remote_ip/connection->client_ip/' \
  < mod_evasive20.c > mod_evasive%{ap_suffix}.c
sed -i 's/evasive20_module/evasive24_module/' mod_evasive%{ap_suffix}.c
sed -i 's/evasive20/evasive24/g' mod_evasive.conf
%endif
%apache_apxs -Wc,"%{optflags}" -c mod_evasive%{ap_suffix}.c

%install
b="%buildroot"
mkdir -p "$b/%apache_libexecdir" "$b/%apache_sysconfdir/conf.d"

%apache_apxs -i -S LIBEXECDIR="%buildroot/%apache_libexecdir" \
	-n mod_evasive%{ap_suffix}.so mod_evasive%{ap_suffix}.la;
cp -a mod_evasive.conf "$b/%apache_sysconfdir/conf.d/";
perl -i -pe "s{/usr/lib/}{%_libdir/}g" \
	"$b/%apache_sysconfdir/conf.d/mod_evasive.conf";

%check
set +x
%apache_test_module_load -m evasive%{ap_suffix} -i mod_evasive.conf
set -x

%files
%defattr(-,root,root)
%apache_libexecdir/
%config(noreplace) %apache_sysconfdir/conf.d/mod_evasive.conf
%doc CHANGELOG LICENSE README test.pl

%changelog
