#
# spec file for package guest-components
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

%global _buildshell /bin/bash
%define user_coco_api_server coco_api_server
%define user_coco_cdh coco_cdh

Name:           guest-components
Version:        0.20.0~git0.f156103
Release:        0
Summary:        Confidential Containers Guest Tools and Components
License:        Apache-2.0
URL:            https://github.com/confidential-containers/guest-components.git
ExclusiveArch:  x86_64
Source0:        %name-%version.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(tss2-sys)
BuildRequires:  rust
BuildRequires:  systemd-rpm-macros
Requires:       system-user-%user_coco_api_server = %version-%release
Requires:       system-user-%user_coco_cdh = %version-%release
%systemd_requires
%systemd_ordering
%description
This package includes tools and components for confidential container images.

%files
%license LICENSE
%_libexecdir/%name
%_unitdir/*.service

%package -n system-user-%user_coco_api_server
Summary:        System user %user_coco_api_server
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_api_server
System user %user_coco_api_server for CoCo RESTful API Server
%pre -n system-user-%user_coco_api_server -f system-user-%user_coco_api_server.pre
%post -n system-user-%user_coco_api_server
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_api_server.conf
%files -n system-user-%user_coco_api_server
%_sysusersdir/system-user-%user_coco_api_server.conf
%_tmpfilesdir/system-user-%user_coco_api_server.conf

%package -n system-user-%user_coco_cdh
Summary:        System user %user_coco_cdh
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_cdh
System user %user_coco_cdh for Confidential Data Hub
%pre -n system-user-%user_coco_cdh -f system-user-%user_coco_cdh.pre
%post -n system-user-%user_coco_cdh
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_cdh.conf
%files -n system-user-%user_coco_cdh
%_sysusersdir/system-user-%user_coco_cdh.conf
%_tmpfilesdir/system-user-%user_coco_cdh.conf

%prep
%autosetup -p1

%build
find * -type f -exec grep -l 'build::BUILD_TIME' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::BUILD_TIME|"Meaningless"|'
find * -type f -exec grep -l 'build::COMMIT_HASH' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::COMMIT_HASH|"%name %version"|'
find * -type f -exec grep -l 'build::LAST_TAG' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::LAST_TAG|"%name"|'
find * -type f -exec grep -l 'build::SHORT_COMMIT' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::SHORT_COMMIT|"%version"|'
export TZ=UTC
export GIT_AUTHOR_DATE=@1234567890
export GIT_COMMITTER_DATE=@1234567890
git --no-pager config --global user.email "you@example.com"
git --no-pager config --global user.name "Your Name"
git --no-pager init --initial-branch=fool .
git --no-pager add LICENSE
git --no-pager commit --message=LICENSE LICENSE
tar xfa %SOURCE1

%install
%if 0%{?__debug_package}
rustflags='-Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2'
release=
dir='debug'
%else
rustflags='-Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=0'
release='--release'
dir='release'
%endif
Meaningless=1234567890
SOURCE_DATE_EPOCH=${Meaningless} \
RUSTFLAGS="${rustflags}" cargo build %?_smp_mflags --offline ${release}
#
mkdir -p '%buildroot%_sysusersdir' '%buildroot%_tmpfilesdir' '%buildroot%_unitdir'
#
tee '%buildroot%_unitdir/api-server-rest.service' <<_EOS_
[Unit]
After=local-fs.target
Description=CoCo RESTful API Server
[Service]
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/%name/api-server-rest $API_SERVER_REST_OPTIONS
RemainAfterExit=true
User=%user_coco_api_server
WorkingDirectory=~
_EOS_
suc='system-user-%user_coco_api_server.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_api_server - "CoCo RESTful API Server" %_localstatedir/lib/%user_coco_api_server %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_api_server
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_api_server 0700 %user_coco_api_server %user_coco_api_server - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"
#
tee '%buildroot%_unitdir/grpc-cdh.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/confidential-data-hub.conf
Description=Confidential Data Hub (gRPC)
[Service]
Environment=GRPC_CDH_OPTIONS="-c %_sysconfdir/confidential-data-hub.conf"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/%name/grpc-cdh $GRPC_CDH_OPTIONS
RemainAfterExit=true
User=%user_coco_cdh
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
tee '%buildroot%_unitdir/ttrpc-cdh.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/confidential-data-hub.conf
Description=Confidential Data Hub (ttRPC)
[Service]
Environment=GRPC_CDH_OPTIONS="-c %_sysconfdir/confidential-data-hub.conf"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/%name/ttrpc-cdh $TTRPC_CDH_OPTIONS
RemainAfterExit=true
User=%user_coco_cdh
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
suc='system-user-%user_coco_cdh.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_cdh - "Confidential Data Hub" %_localstatedir/lib/%user_coco_cdh %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_cdh
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_cdh 0700 %user_coco_cdh %user_coco_cdh - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"
#
t='%buildroot%_libexecdir/%name'
mkdir -vp "${t}"
for dentry in target/${dir}/*
do
	test -f "${dentry}" || continue
	case "${dentry}" in
	*.d) continue ;;
	*.rlib) continue ;;
	*) mv -vt "${t}" "${dentry}" ;;
	esac
done

%changelog

