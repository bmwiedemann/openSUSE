#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define pgname @BUILD_FLAVOR@
%if "%{pgname}" == ""
%define         pgname postgresql
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} < 1500 && "%{pgname}" == "postgresql10"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && "%{pgname}" == "postgresql93"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && "%{pgname}" == "postgresql94"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} >= 1500 && "%{pgname}" == "postgresql95"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} >= 1500 && "%{pgname}" == "postgresql96"
ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?suse_version} == 1500 && "%{pgname}" == "postgresql11"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150100 && "%{pgname}" == "postgresql12"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150200 && "%{pgname}" == "postgresql13"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150400 && "%{pgname}" == "postgresql14"
ExclusiveArch:  do_not_build
%endif
%define         sname pgagent
%define         pg_bindir %(pg_config --bindir)
%define         pg_libdir %(pg_config --pkglibdir)
%define         pg_share %(pg_config --sharedir)
# double \ as they are escaped in %%() call
%define         pg_version %(pg_config --version | sed -e 's/.*[[:space:]]//' -e 's/\\.[0-9]*$//' -e 's/\\.//')

Name:           %{pgname}-%{sname}
Version:        4.2.2
Release:        0
Summary:        Job scheduler for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            http://www.pgadmin.org/
Source0:        https://github.com/pgadmin-org/%{sname}/archive/refs/tags/%{sname}-%{version}.tar.gz
Source2:        %{sname}.service.in
Source3:        %{sname}.logrotate.in
Source4:        %{sname}.conf.in
Source5:        README.SUSE
BuildRequires:  %{pgname}-server
BuildRequires:  %{pgname}-server-devel
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8.8
BuildRequires:  gcc-c++
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow
Requires:       %{pgname}-server
Recommends:     logrotate
%{?systemd_requires}

%description
pgAgent is a job scheduler for PostgreSQL which may be managed
using pgAdmin.

%prep
%autosetup -n %{sname}-%{sname}-%{version}

cp %{SOURCE2} %{name}.service
cp %{SOURCE3} %{name}.logrotate
cp %{SOURCE4} %{name}.conf
sed -ie "s/%%{name}/%{name}/" %{name}.service
sed -ie "s/%%{pg_version}/%{pg_version}/" %{name}.service
sed -ie "s/%%{name}/%{name}/" %{name}.logrotate
sed -ie "s/%%{name}/%{name}/" %{name}.conf
cp %{S:5} .

%build
CFLAGS="%{optflags} -fPIC -pie"
CXXFLAGS="%{optflags} -fPIC -pie -pthread"
export CFLAGS
export CXXFLAGS
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DPG_CONFIG_PATH:FILEPATH=%{_bindir}/pg_config \
	-DSTATIC_BUILD:BOOL=OFF
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

# Rename pgagent binary, so that we can have parallel installations:
mv -f %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{name}
# Remove some cruft, and also install doc related files to appropriate directory:
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}
rm -f %{buildroot}%{_prefix}/LICENSE
rm -f %{buildroot}%{_prefix}/README
mv -f %{buildroot}%{_datadir}/pgagent*.sql %{buildroot}%{_datadir}/%{name}-%{version}/

# Install unit file
install -d %{buildroot}%{_unitdir}
install -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
# Install conf file
install -p -d %{buildroot}%{_sysconfdir}/%{sname}/
install -p -m 644 %{name}.conf %{buildroot}%{_sysconfdir}/%{sname}/%{name}.conf
# ... and make a tmpfiles script to recreate it at reboot.
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_rundir}/%{name} 0755 root root -
d %{_localstatedir}/lib/%{sname} 0700 pgagent pgagent -
f %{_localstatedir}/log/%{name}.log 0700 pgagent pgagent -
EOF

# Install logrotate file:
install -p -d %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
getent group pgagent >/dev/null || groupadd -r pgagent
getent passwd pgagent >/dev/null || useradd -r -g pgagent -d %{_localstatedir}/lib/%{sname} -s /sbin/false -c "user for pgAgent Job Scheduler" pgagent
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README README.SUSE
%license LICENSE
%{_bindir}/%{name}
%ghost %dir %{_rundir}/%{name}
%ghost %dir %{_localstatedir}/lib/%{sname}
%ghost %{_localstatedir}/log/%{name}.log
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/%{sname}*.sql
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_sysconfdir}/%{sname}/
%config(noreplace) %{_sysconfdir}/%{sname}/%{name}.conf
%{pg_share}/extension/%{sname}--*.sql
%{pg_share}/extension/%{sname}--unpackaged--*.sql
%{pg_share}/extension/%{sname}.control

%changelog
