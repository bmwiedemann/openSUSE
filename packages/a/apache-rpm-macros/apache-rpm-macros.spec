#
# spec file for package apache-rpm-macros
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} < 1130
%define _libexecdir   /usr/lib
%endif

%define ap_major                 2
%if 0%{?suse_version}
%define ap_branch                %(rpm -q --qf "%%{version}" apache%{ap_major} | tr '.' ' ' | { read maj min patch; printf "%d%02d" $maj $min; })
%define ap_version               %(rpm -q --qf "%%{version}" apache%{ap_major} | tr '.' ' ' | { read maj min patch; printf "%d%02d%02d" $maj $min $patch; })
%else
%define ap_branch                %(rpm -q --qf "%%{version}" httpd |             tr '.' ' ' | { read maj min patch; printf "%d%02d" $maj $min; })
%define ap_version               %(rpm -q --qf "%%{version}" httpd |             tr '.' ' ' | { read maj min patch; printf "%d%02d%02d" $maj $min $patch; })
%endif
%define ap_pname                 apache%{ap_major}
%define ap_apxs                  %(ls -1 /usr/{,s}bin/apxs{,2} 2>/dev/null | head -n 1)
%define ap_cflags                %(%{ap_apxs} -q CFLAGS)
%define ap_includedir            %(%{ap_apxs} -q INCLUDEDIR)
%define ap_libexecdir            %(%{ap_apxs} -q LIBEXECDIR)
%define ap_localstatedir         %(%{ap_apxs} -q LOCALSTATEDIR)
%if 0%{?suse_version}
%define ap_mmn                   %(MMN=$(%{ap_apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
%define ap_maint_mmn             %(MMN=$(rpm -q --provides apache2 | grep suse_maintenance_mmn); test -z "$MMN" && MMN=apache2; echo $MMN)
%endif
%define ap_serverroot            %(%{ap_apxs} -q PREFIX)
%define ap_sysconfdir            %(%{ap_apxs} -q SYSCONFDIR)
%define ap_datadir               %(%{ap_apxs} -q DATADIR)
%if 0%{?suse_version}
%define ap_user                  wwwrun
%define ap_group                 www
%else
%define ap_user                  apache
%define ap_group                 apache
%endif
%if 0%{?suse_version}
%define ap_access_syntax_version %(if [ $(grep -c '^[[:space:]]*Require all denied' /etc/apache2/httpd.conf) -gt 0 ]; then echo 24; else echo 22; fi)
%endif
#
%if 0%{?suse_version} > 1230
%define macros_dir            %{_libexecdir}/rpm/macros.d
%else
%define macros_dir            %{_sysconfdir}/rpm
%endif
%define macros_file           macros.apache
Name:           apache-rpm-macros
Version:        20160120
Release:        0
Summary:        Apache RPM Macros
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Url:            http://httpd.apache.org/
Source1:        macros.apache-module-test
%if 0%{?suse_version}
BuildRequires:  apache%{ap_major}-devel
%else
BuildRequires:  httpd-devel
%endif
Requires:       apache-rpm-macros-control
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RPM Macros intended for Apache modules spec files.

%prep

%build
cat << eom > %{macros_file}
%%apache_major                   %{ap_major}
%%apache_branch                  %{ap_branch}
%%apache_version                 %{ap_version}
%%apache_pname                   %{ap_pname}
%%apache_apxs                    %{ap_apxs}
%%apache_cflags                  %{ap_cflags}
%%apache_includedir              %{ap_includedir}
%%apache_libexecdir              %{ap_libexecdir}
%%apache_localstatedir           %{ap_localstatedir}
%%apache_mmn                     %{ap_mmn}
%%apache_suse_maintenance_mmn    %{ap_maint_mmn}
%%apache_serverroot              %{ap_serverroot}
%%apache_sysconfdir              %{ap_sysconfdir}
%%apache_datadir                 %{ap_datadir}
%%apache_user                    %{ap_user}
%%apache_group                   %{ap_group}
%%apache_access_syntax_version   %{ap_access_syntax_version}
eom
echo >> %{macros_file}

%install
mkdir -p %{buildroot}%{macros_dir}
install -m 644 %{macros_file} %{buildroot}%{macros_dir}
install -m 644 %{SOURCE1}     %{buildroot}%{macros_dir}

%files
%defattr(-,root,root)
%dir %{macros_dir}
%{macros_dir}/macros.apache*

%changelog
