#
# spec file for package crypto-policies
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# disable testsuite and manbuild to reduce dependencies in ring0
%bcond_with testsuite
%bcond_with manbuild
%global _python_bytecompile_extra 0

Name:           crypto-policies
Version:        20250714.cd6043a
Release:        0
Summary:        System-wide crypto policies
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/redhat-crypto/fedora-%{name}
Source0:        fedora-%{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        man-crypto-policies.tar.xz
Source3:        man-fips-scripts.tar.xz
Source4:        fips-mode-setup
Source5:        fips-finish-install
Source6:        crypto-policies-rpmlintrc
%if %{without manbuild}
#PATCH-FIX-OPENSUSE Manpages build cycles and dependencies
# To reduce the build dependencies in Ring0, we have to compile the
# man pages locally (use --with testsuite) and add the built files
# crypto-policies.7.gz, update-crypto-policies.8.gz, fips-mode-setup.8.gz
# and fips-finish-install.8.gz as sources.
Patch1:         crypto-policies-no-build-manpages.patch
%endif
#PATCH-FIX-OPENSUSE Skip not needed LibreswanGenerator and SequoiaGenerator
Patch2:         crypto-policies-policygenerators.patch
#PATCH-FIX-OPENSUSE Skip NSS policy check if not installed mozilla-nss-tools [bsc#1211301]
Patch3:         crypto-policies-nss.patch
#PATCH-FIX-OPENSUSE enable SHA1 sigver in DEFAULT
Patch4:         crypto-policies-enable-SHA1-sigver-in-DEFAULT.patch
#PATCH-FIX-OPENSUSE Allow sshd in FIPS mode when using the DEFAULT policy [bsc#1227370]
Patch5:         crypto-policies-Allow-sshd-in-FIPS-mode-using-DEFAULT.patch
#PATCH-FIX-OPENSUSE Fix the output comments around setting the FIPS mode
Patch6:         crypto-policies-FIPS-output.patch
#PATCH-FIX-OPENSUSE Adapt the manpages to SUSE/openSUSE
Patch7:         crypto-policies-SUSE-manpages.patch
#PATCH-FIX-OPENSUSE Allow openssl to load when using any policy in FIPS mode [bsc#1243830, bsc#1242233]
Patch8:         crypto-policies-Allow-openssl-other-policies-in-FIPS-mode.patch
BuildRequires:  python3-base >= 3.11
%if %{with manbuild}
BuildRequires:  asciidoc
%endif
%if %{with testsuite}
# The following packages are needed for the testsuite
BuildRequires:  bind
BuildRequires:  crypto-policies-scripts
BuildRequires:  gnutls
BuildRequires:  java-devel
BuildRequires:  libxslt
BuildRequires:  mozilla-nss-tools
BuildRequires:  openssh-clients
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel >= 3.11
BuildRequires:  python3-pytest
BuildRequires:  systemd-rpm-macros
%else
# Avoid cycle with python-rpm-macros
#!BuildIgnore: python-rpm-packaging python-rpm-macros
%endif
%if 0%{?primary_python:1}
Recommends:     crypto-policies-scripts
%endif
Conflicts:      gnutls < 3.8.8
Conflicts:      nss < 3.101
Conflicts:      openssh < 9.9p1
Conflicts:      openssl < 3.0.2
#!BuildIgnore:  crypto-policies
BuildArch:      noarch

%description
This package provides pre-built configuration files with
cryptographic policies for various cryptographic back-ends,
such as SSL/TLS libraries.

%package scripts
Summary:        Tool to switch between crypto policies
Requires:       %{name} = %{version}-%{release}
Recommends:     perl-Bootloader
Provides:       fips-mode-setup = %{version}-%{release}

%description scripts
This package provides a tool update-crypto-policies, which applies
the policies provided by the crypto-policies package. These can be
either the pre-built policies from the base package or custom policies
defined in simple policy definition files.

The package also provides a tool fips-mode-setup, which can be used
to enable or disable the system FIPS mode.

%prep
%autosetup -p1 -n fedora-%{name}-%{version}

# Make README.SUSE available for %%doc
cp -p %{SOURCE1} .

%build
export OPENSSL_CONF=''

# The scripts fips-mode-setup and fips-finish-install
# have been removed upstream and we ship them as sources.
cp -p %{SOURCE4} %{SOURCE5} .

%if %{with manbuild}
cp -p %{SOURCE3} .
tar xf %{SOURCE3}
# The manpages fips-mode-setup.8.gz and fips-finish-install.8.gz
# have been removed upstream and we ship them as sources.
sed -i '/MAN8PAGES=update-crypto-policies.8/s/$/ fips-finish-install.8 fips-mode-setup.8/g' Makefile
sed -i '/SCRIPTS=update-crypto-policies/s/$/ fips-finish-install fips-mode-setup/g' Makefile
%endif

%make_build

%install
mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/
mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/back-ends/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/state/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/local.d/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/policies/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/policies/modules/
mkdir -p -m 755 %{buildroot}%{_bindir}

make DESTDIR=%{buildroot} DIR=%{_datarootdir}/crypto-policies MANDIR=%{_mandir} %{?_smp_mflags} install

install -p -m 644 default-config %{buildroot}%{_sysconfdir}/crypto-policies/config
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/current
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/CURRENT.pol

mkdir -p -m 755 %{buildroot}%{_mandir}/
mkdir -p -m 755 %{buildroot}%{_mandir}/man7/
mkdir -p -m 755 %{buildroot}%{_mandir}/man8/
%if %{without manbuild}
# Install the manpages from defined sources
tar xf %{SOURCE2}
cp *.7.gz %{buildroot}%{_mandir}/man7/
cp *.8.gz %{buildroot}%{_mandir}/man8/
%endif

# Install the executable scripts
install -p -m 755 update-crypto-policies %{buildroot}%{_bindir}/
install -p -m 755 fips-mode-setup %{buildroot}%{_bindir}/
install -p -m 755 fips-finish-install %{buildroot}%{_bindir}/

# Drop pre-generated GOST-ONLY and FEDORA policies, we do not need to ship them
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/GOST-ONLY
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/FEDORA*
find  %{buildroot} -type f -name 'FEDORA*.pol' -print -delete

# Drop libreswan and sequoia config files
find  %{buildroot} -type f -name 'libreswan.*' -print -delete
find  %{buildroot} -type f -name 'sequoia.*' -print -delete

# Drop not needed fips bind mount service
find %{buildroot} -type f -name 'default-fips-config' -print -delete
find %{buildroot} -type f -name 'fips-setup-helper' -print -delete
find %{buildroot} -type f -name 'fips-crypto-policy-overlay*' -print -delete

# Create back-end configs for mounting with read-only /etc/
for d in LEGACY DEFAULT FUTURE FIPS BSI ; do
    mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d
    for f in %{buildroot}%{_datarootdir}/crypto-policies/$d/* ; do
        ln $f %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d/$(basename $f .txt).config
    done
done

for f in %{buildroot}%{_datarootdir}/crypto-policies/DEFAULT/* ; do
    ln -sf %{_datarootdir}/crypto-policies/DEFAULT/$(basename $f) %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/$(basename $f .txt).config
done

# Fix shebang env in python scripts
for f in %{buildroot}%{_datadir}/crypto-policies/python/*.py
do
    sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' $f
done

%py3_compile %{buildroot}%{_datadir}/crypto-policies/python

# Install README.SUSE to %%doc
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/crypto-policies

%check
%if %{with testsuite}
export OPENSSL_CONF=''
%make_build test SKIP_LINTING=1
%endif

%post -p <lua>
if not posix.access("%{_sysconfdir}/crypto-policies/config") then
    local policy = "DEFAULT"
    local cf = io.open("/proc/sys/crypto/fips_enabled", "r")
    if cf then
        if cf:read() == "1" then
            policy = "FIPS"
        end
        cf:close()
    end
    cf = io.open("%{_sysconfdir}/crypto-policies/config", "w")
    if cf then
        cf:write(policy.."\n")
        cf:close()
    end
    cf = io.open("%{_sysconfdir}/crypto-policies/state/current", "w")
    if cf then
        cf:write(policy.."\n")
        cf:close()
    end
    local policypath = "%{_datarootdir}/crypto-policies/"..policy
    for fn in posix.files(policypath) do
        if fn ~= "." and fn ~= ".." then
            local backend = fn:gsub(".*/", ""):gsub("%%..*", "")
            local cfgfn = "%{_sysconfdir}/crypto-policies/back-ends/"..backend..".config"
            posix.unlink(cfgfn)
            posix.symlink(policypath.."/"..fn, cfgfn)
        end
    end
end

cfg_path_libreswan = "%{_sysconfdir}/crypto-policies/back-ends/libreswan.config"
st = posix.stat(cfg_path_libreswan)
if st and st.type == "link" then
   posix.unlink(cfg_path_libreswan)
end

cfg_path_javasystem = "%{_sysconfdir}/crypto-policies/back-ends/javasystem.config"
st = posix.stat(cfg_path_javasystem)
if st and st.type == "link" then
   posix.unlink(cfg_path_javasystem)
end

cfg_path_opensslconfig = "%{_sysconfdir}/crypto-policies/back-ends/openssl.config"
st = posix.stat(cfg_path_opensslconfig)
if st and st.type == "link" then
   posix.unlink(cfg_path_opensslconfig)
end

%posttrans scripts
%{_bindir}/update-crypto-policies --no-check >/dev/null 2>/dev/null || :

%files
%license COPYING.LESSER
%doc README.md CONTRIBUTING.md
%doc %{_sysconfdir}/crypto-policies/README.SUSE

%dir %{_sysconfdir}/crypto-policies/
%dir %{_sysconfdir}/crypto-policies/back-ends/
%dir %{_sysconfdir}/crypto-policies/state/
%dir %{_sysconfdir}/crypto-policies/local.d/
%dir %{_sysconfdir}/crypto-policies/policies/
%dir %{_sysconfdir}/crypto-policies/policies/modules/
%dir %{_datarootdir}/crypto-policies/

%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/config

%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/gnutls.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/opensslcnf.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/openssl_fips.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/openssh.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/opensshserver.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/nss.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/bind.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/java.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/krb5.config
%ghost %config(missingok,noreplace) %verify(not mode) %{_sysconfdir}/crypto-policies/back-ends/libssh.config
# %%verify(not mode) comes from the fact that these turn into symlinks and back to regular files at will.

%ghost %{_sysconfdir}/crypto-policies/state/current
%ghost %{_sysconfdir}/crypto-policies/state/CURRENT.pol

%{_mandir}/man7/crypto-policies.7%{?ext_man}
%{_datarootdir}/crypto-policies/LEGACY
%{_datarootdir}/crypto-policies/DEFAULT
%{_datarootdir}/crypto-policies/FUTURE
%{_datarootdir}/crypto-policies/FIPS
%{_datarootdir}/crypto-policies/BSI
%{_datarootdir}/crypto-policies/EMPTY
%{_datarootdir}/crypto-policies/back-ends
%{_datarootdir}/crypto-policies/default-config
%{_datarootdir}/crypto-policies/reload-cmds.sh
%{_datarootdir}/crypto-policies/policies

%files scripts
%{_bindir}/update-crypto-policies
%{_bindir}/fips-mode-setup
%{_bindir}/fips-finish-install
%{_mandir}/man8/update-crypto-policies.8%{?ext_man}
%{_mandir}/man8/fips-mode-setup.8%{?ext_man}
%{_mandir}/man8/fips-finish-install.8%{?ext_man}
%{_datarootdir}/crypto-policies/python

%changelog
