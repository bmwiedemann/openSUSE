#
# spec file for package trustee
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
%define user_coco_as coco_as
%define user_coco_kbs coco_kbs
%define user_coco_rvps coco_rvps
%define user_coco_trustee coco_trustee

Name:           trustee
Version:        0.20.0~git60.435ed3c
Release:        0
Summary:        Attestation and Secret Delivery Components 
License:        Apache-2.0
URL:            https://github.com/confidential-containers/trustee.git
ExclusiveArch:  x86_64
Source0:        %name-%version.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  bash
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(tss2-sys)
BuildRequires:  rust
BuildRequires:  suse-libsgx-dcap-quoteverify-devel
BuildRequires:  systemd-rpm-macros
Requires:       system-user-%user_coco_as = %version-%release
Requires:       system-user-%user_coco_kbs = %version-%release
Requires:       system-user-%user_coco_rvps = %version-%release
Requires:       system-user-%user_coco_trustee = %version-%release
%systemd_requires
%systemd_ordering
%description
This package contains tools and components for attesting confidential guests and providing secrets to them. Collectively, these components are known as Trustee. Trustee typically operates on behalf of the guest owner and interact remotely with guest components.

%pre
%service_add_pre                 grpc-as.service kbs.service rvps.service trustee.service
%post
%service_add_post                grpc-as.service kbs.service rvps.service trustee.service
%preun
%service_del_preun               grpc-as.service kbs.service rvps.service trustee.service
%postun
%service_del_postun_with_restart grpc-as.service kbs.service rvps.service trustee.service
%files
%doc attestation-service/docs/*.md
%doc *.md
%license LICENSE
%_libexecdir/%name
%_unitdir/*.service

%package -n system-user-%user_coco_as
Summary:        System user %user_coco_as
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_as
System user %user_coco_as for Confidential Containers Attestation Service
%pre -n system-user-%user_coco_as -f system-user-%user_coco_as.pre
%post -n system-user-%user_coco_as
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_as.conf
%files -n system-user-%user_coco_as
%_sysusersdir/system-user-%user_coco_as.conf
%_tmpfilesdir/system-user-%user_coco_as.conf

%package -n system-user-%user_coco_kbs
Summary:        System user %user_coco_kbs
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_kbs
System user %user_coco_kbs for Key Broker Service
%pre -n system-user-%user_coco_kbs -f system-user-%user_coco_kbs.pre
%post -n system-user-%user_coco_kbs
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_kbs.conf
%files -n system-user-%user_coco_kbs
%_sysusersdir/system-user-%user_coco_kbs.conf
%_tmpfilesdir/system-user-%user_coco_kbs.conf

%package -n system-user-%user_coco_rvps
Summary:        System user %user_coco_rvps
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_rvps
System user %user_coco_rvps for Reference Value Provider Service
%pre -n system-user-%user_coco_rvps -f system-user-%user_coco_rvps.pre
%post -n system-user-%user_coco_rvps
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_rvps.conf
%files -n system-user-%user_coco_rvps
%_sysusersdir/system-user-%user_coco_rvps.conf
%_tmpfilesdir/system-user-%user_coco_rvps.conf

%package -n system-user-%user_coco_trustee
Summary:        System user %user_coco_trustee
BuildRequires:  sysuser-tools
Requires:       %name = %version-%release
%?sysusers_requires
%description -n system-user-%user_coco_trustee
System user %user_coco_trustee for Trustee
%pre -n system-user-%user_coco_trustee -f system-user-%user_coco_trustee.pre
%post -n system-user-%user_coco_trustee
%tmpfiles_create %_tmpfilesdir/system-user-%user_coco_trustee.conf
%files -n system-user-%user_coco_trustee
%_sysusersdir/system-user-%user_coco_trustee.conf
%_tmpfilesdir/system-user-%user_coco_trustee.conf

%prep
trap 'set -ex;df -hTP' EXIT
%autosetup -p1

%build
trap 'set -ex;df -hTP' EXIT
find * -type f -exec grep -l 'build::BUILD_TIME' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::BUILD_TIME|"Meaningless"|'
find * -type f -exec grep -l 'build::COMMIT_HASH' '{}' + | xargs --no-run-if-empty --verbose sed -i 's|build::COMMIT_HASH|"%name %version"|'
sed -i~ '/KBS_BUILD_DATE/s|build_date|"MeaningLess"|' kbs/build.rs
diff -u "$_"~ "$_" && exit 123
tar xfa %SOURCE1

%install
trap 'set -ex;df -hTP' EXIT
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
mv attestation-service/docs/config.md grpc-as-config.md
mv attestation-service{/,-}README.md
mv kbs/docs/config.md kbs-config.md
mv kbs{/,-}README.md
mv rvps{/,-}README.md
mv tools/kbs-client/README.md kbs-client-README.md
#
mkdir -p '%buildroot%_sysusersdir' '%buildroot%_tmpfilesdir' '%buildroot%_unitdir'
#
tee '%buildroot%_unitdir/grpc-as.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/grpc-as.json
Description=Confidential Containers Attestation Service (gRPC)
[Service]
Environment=GRPC_AS_OPTIONS="--config %_sysconfdir/grpc-as.json"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/grpc-as $GRPC_AS_OPTIONS
RemainAfterExit=true
User=%user_coco_as
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
suc='system-user-%user_coco_as.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_as - "Confidential Containers Attestation Service" %_localstatedir/lib/%user_coco_as %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_as
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_as 0700 %user_coco_as %user_coco_as - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"
#
tee '%buildroot%_unitdir/kbs.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/kbs.json
Description=Confidential Containers Key Broker Service
[Service]
Environment=KBS_OPTIONS="--config %_sysconfdir/kbs.json"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/kbs $KBS_OPTIONS
RemainAfterExit=true
User=%user_coco_kbs
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
suc='system-user-%user_coco_kbs.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_kbs - "Confidential Containers Key Broker Service" %_localstatedir/lib/%user_coco_kbs %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_kbs
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_kbs 0700 %user_coco_kbs %user_coco_kbs - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"
#
tee '%buildroot%_unitdir/rvps.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/rvps.json
Description=Confidential Containers Key Broker Service
[Service]
Environment=RVPS_OPTIONS="--config %_sysconfdir/rvps.json"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/rvps $RVPS_OPTIONS
RemainAfterExit=true
User=%user_coco_rvps
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
suc='system-user-%user_coco_rvps.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_rvps - "Confidential Containers Reference Value Provider Service" %_localstatedir/lib/%user_coco_rvps %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_rvps
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_rvps 0700 %user_coco_rvps %user_coco_rvps - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"
#
tee '%buildroot%_unitdir/trustee.service' <<_EOS_
[Unit]
After=local-fs.target
ConditionPathExists=%_sysconfdir/trustee.json
Description=Confidential Containers Key Broker Service
[Service]
Environment=RVPS_OPTIONS="--config %_sysconfdir/trustee.json"
Environment=OPENSSL_CONF=%_sysconfdir/ssl/openssl.cnf
ExecStart=%_libexecdir/trustee $RVPS_OPTIONS
RemainAfterExit=true
User=%user_coco_trustee
WorkingDirectory=~
[Install]
WantedBy=multi-user.target
_EOS_
suc='system-user-%user_coco_trustee.conf'
tee "${suc}" <<'_EOC_'
u %user_coco_trustee - "Trustee" %_localstatedir/lib/%user_coco_trustee %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%user_coco_trustee
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%user_coco_trustee 0700 %user_coco_trustee %user_coco_trustee - -
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

