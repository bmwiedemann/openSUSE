#
# spec file for package confidential-computing.tee.dcap.pccs
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


%define pccs_user pccs
%global _buildshell /bin/bash
Name:           confidential-computing.tee.dcap.pccs
Version:        1.25
Release:        0
Summary:        Intel® SGX/TDX Provisioning Certificate Caching Service
License:        BSD-3-Clause
URL:            https://github.com/intel/confidential-computing.tee.dcap.pccs
ExclusiveArch:  x86_64
Source0:        %name-%version.tar
Source123:      %name.node_modules.cpio
Source321:      %name.node_modules.txt
BuildRequires:  bash
%description
This is the anchor package for intel-tee-pccs-admin-tool and sgx-dcap-pccs.

%package -n system-user-%pccs_user
Summary:        System user %pccs_user
BuildRequires:  sysuser-tools
%?sysusers_requires
%description -n system-user-%pccs_user
System user %pccs_user for Intel(R) SGX PCK Caching Service
%pre -n system-user-%pccs_user -f system-user-%pccs_user.pre
%post -n system-user-%pccs_user
%tmpfiles_create %_tmpfilesdir/system-user-%pccs_user.conf
%files -n system-user-%pccs_user
%_sysusersdir/system-user-%pccs_user.conf
%_tmpfilesdir/system-user-%pccs_user.conf

%package -n suse-sgx-dcap-pccs
Summary:        Intel(R) Software Guard Extensions PCK Caching Service
BuildRequires:  cpio
BuildRequires:  gawk
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
Conflicts:      intel-tee-pccs-admin-tool
Conflicts:      sgx-dcap-pccs
Requires:       python3-keyring
Requires:       python3-requests
Requires:       system-user-%pccs_user = %version-%release
Requires(posttrans): system-user-%pccs_user = %version-%release
%systemd_requires
%systemd_ordering
%description -n suse-sgx-dcap-pccs
Intel(R) Software Guard Extensions PCK Caching Service.
This package provides also the pccs-admin-tool for administering PCCS.

Together they support Intel® SGX DCAP remote attestation by locally caching
provisioning collateral consumed during quote generation (PCK certificates,
PCK certificate chains) and verification (TCB info, CRLs, QE/QvE identities,
root CAs, appraisal policies), reducing latency and external dependencies.

PCCS also caches Intel SGX DCAP provisioning certification collateral (i.e.,
Platform Manifests), helping centralize the infrastructure set-up as well.

%files -n suse-sgx-dcap-pccs
%license License.txt
%_bindir/pccsadmin.py
%_libexecdir/suse-sgx-dcap-pccs
%_unitdir/*.service
%python3_sitearch/*
%pre -n suse-sgx-dcap-pccs
%service_add_pre pccs.service
%post -n suse-sgx-dcap-pccs
%service_add_post pccs.service
%preun -n suse-sgx-dcap-pccs
%service_del_preun pccs.service
%postun -n suse-sgx-dcap-pccs
%service_del_postun_with_restart pccs.service

%prep
%autosetup -p1

%build
find \( -name "*.js" -o -name "*.py" \) -type f -exec chmod -c 644 '{}' +

# avoids binary bindings
sed --regexp-extended -i~ '
s|^[[:blank:]]+//[[:blank:]]*"|	"|
s|^[[:blank:]]+//[[:blank:]]*}|	}|
s|[[:blank:]]//.*$||' service/config/default.json
diff -u "$_"~ "$_" && exit 1
python3 - <<'_EOS_'
import json
with open("service/config/default.json", "r") as f:
	content = json.load(f)
with open("a.json", "w") as f:
	json.dump(content, f, indent=2, sort_keys=True)
	f.write('\n')
content["DB_CONFIG"]="mysql"
del content["sqlite"]
with open("b.json", "w") as f:
	json.dump(content, f, indent=2, sort_keys=True)
	f.write('\n')
_EOS_
cat b.json
mv b.json service/config/default.json
rm a.json

sed -i~ "
s|^const __dirname.*|import os from 'os';|
/filename: __dirname/s|^.*|    filename: os.homedir() + '/logs/pccs_server.log',|
" service/utils/Logger.js
diff -u "$_"~ "$_" && exit 1

sed -i~ '1{s|^.*|#!%_bindir/node|}' service/pccs_server.js
diff -u "$_"~ "$_" && exit 1

sed -i~ '
/^After/{
	s|^.*|After=network.target time-sync.target mariadb.service|
	a\
# Use %_libexecdir/suse-sgx-dcap-pccs/config/default.json as template\
ConditionPathExists=%_localstatedir/lib/%pccs_user/config/default.json
}
/^EnvironmentFile=/d
/^Environment=/d
/^ExecStart/s|^.*|ExecStart=%_libexecdir/suse-sgx-dcap-pccs/pccs_server.js|
/^User/s|^.*|User=%pccs_user|
/^WorkingDirectory/s|^.*|WorkingDirectory=%_localstatedir/lib/%pccs_user|
' service/pccs.service
diff -u "$_"~ "$_" && exit 1

chmod -c 755 PccsAdminTool/pccsadmin.py service/pccs_server.js
mkdir node_modules
pushd node_modules
cpio --extract < %{SOURCE123}
while read
do
	oIFS=$IFS
	IFS=/
	set -- ${REPLY}
	IFS=$oIFS
	if test "$6" = '-'
	then
		mkdir -p "$4"
		name="$4/$5"
		tgz=$8
	elif test "$5" = '-'
	then
		name="$4"
		tgz=$7
	else
		tgz=
	fi
	if mkdir "${name}"
	then
		tar \
		--auto-compress \
		--extract \
		"--directory=./${name}" \
		--strip-components=1 \
		--file="./${tgz}"
	fi
	rm -- "./${tgz}"
done < <(gawk '{print $2}' %{SOURCE321})
find \( \
	-name .nyc_output -o \
	-name .vscode -o \
	-name Xcode -o \
	-name benchmark -o \
	-name bin -o \
	-name coverage -o \
	-name demo -o \
	-name deps -o \
	-name docs -o \
	-name emacs -o \
	-name gyp -o \
	-name test -o \
	-name tests -o \
	-name tools -o \
	-name .github \) -type d -exec rm -rfv '{}' +
find \( \
	-name "*.c" -o \
	-name "*.cc" -o \
	-name "*.el" -o \
	-name "*.h" -o \
	-name "*.html" -o \
	-name "*.sh" -o \
	-name "*~" -o \
	-name "C*.md" -o \
	-name "R*.md" -o \
	-name .babelrc -o \
	-name .coveralls.yml -o \
	-name .editorconfig -o \
	-name .eslintignore -o \
	-name .eslintrc -o \
	-name .eslintrc.cjs -o \
	-name .eslintrc.json -o \
	-name .eslintrc.yml -o \
	-name .flake8 -o \
	-name .gitattributes -o \
	-name .gitignore -o \
	-name .jshintrc -o \
	-name .npmignore -o \
	-name .nvmrc -o \
	-name .nycrc -o \
	-name .prettierrc.js -o \
	-name .prettierrc.yaml -o \
	-name .runkit_example.js -o \
	-name .testem.json -o \
	-name .travis.yml -o \
	-name .uglifyjsrc.json -o \
	-name AUTHORS -o \
	-name AUTHORS.md -o \
	-name CHANGELOG.json -o \
	-name CHANGELOG.md -o \
	-name CONTRIBUTING.md -o \
	-name Changelog.md -o \
	-name FUNDING.yml -o \
	-name GOVERNANCE.md -o \
	-name HISTORY.md -o \
	-name History.md -o \
	-name Makefile -o \
	-name PULL_REQUEST_TEMPLATE.md -o \
	-name Porting-Buffer.md -o \
	-name README -o \
	-name README.markdown -o \
	-name Readme.markdown -o \
	-name Readme.md -o \
	-name SECURITY.md -o \
	-name UPGRADING.md -o \
	-name bin.js -o \
	-name build.js -o \
	-name caching_sha2_password.md -o \
	-name changelog.md -o \
	-name flake.lock -o \
	-name flake.nix -o \
	-name index.md -o \
	-name readme.markdown -o \
	-name readme.md -o \
	-name release.md -o \
	-name update-gyp.py -o \
	-name yarn.lock -o \
	-name README.md \) -type f -exec rm -fv '{}' +
find -type f | grep -Ev '(tsconfig.json|package.json|license|LICENSE|LICENSE.md|\.((js|ts)\.map|js|ts|json))$' || : $?
find -type f -name "*.js" -exec sed -i -e '1{/^#!/d}' '{}' +
find -type f -exec chmod -c 644 '{}' +
find -type d -exec chmod -c 755 '{}' +
hardlink --verbose --ignore-time .
popd
find -name "*~" -delete

%install
mkdir -p '%buildroot%_tmpfilesdir' '%buildroot%_sysusersdir'
suc='system-user-%pccs_user.conf'
tee "${suc}" <<'_EOC_'
u %pccs_user - "SGX PCK Caching Service" %_localstatedir/lib/%pccs_user %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-%pccs_user
mv -t '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/%pccs_user 0700 %pccs_user %pccs_user - -
_EOC_
mv -t '%buildroot%_tmpfilesdir' "${suc}"

mkdir -p '%buildroot%_bindir'
mkdir -p '%buildroot%python3_sitearch'
mv PccsAdminTool/pccsadmin.py '%buildroot%_bindir'
mv PccsAdminTool/lib '%buildroot%python3_sitearch'

pushd service
mkdir -p '%buildroot%_libexecdir/suse-sgx-dcap-pccs'
mkdir -p '%buildroot%_unitdir'
mv -t '%buildroot%_unitdir' \
	*.service
	%nil
mv -t '%buildroot%_libexecdir/suse-sgx-dcap-pccs' \
	config \
	constants \
	controllers \
	dao \
	middleware \
	migrations \
	package.json \
	pccs_server.js \
	pckCertSelection \
	pcs_client \
	routes \
	services \
	utils \
	x509 \
	%nil
popd
mv -t '%buildroot%_libexecdir/suse-sgx-dcap-pccs' node_modules

%python3_fix_shebang

%changelog

