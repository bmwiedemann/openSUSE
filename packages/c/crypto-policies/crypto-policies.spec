#
# spec file for package crypto-policies
#
# Copyright (c) 2021 SUSE LLC
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


%global _python_bytecompile_extra 0
Name:           crypto-policies
Version:        20210917.c9d86d1
Release:        0
Summary:        System-wide crypto policies
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/redhat-crypto/fedora-%{name}
Source0:        fedora-%{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        crypto-policies.7.gz
Source3:        update-crypto-policies.8.gz
Patch0:         crypto-policies-test_supported_modules_only.patch
Patch1:         crypto-policies-no-build-manpages.patch
Patch2:         crypto-policies-FIPS.patch
BuildRequires:  python3-base
# For testing, the following buildrequires need to be uncommented.
# BuildRequires:  asciidoc
# BuildRequires:  bind
# BuildRequires:  gnutls >= 3.6.0
# BuildRequires:  java-devel
# BuildRequires:  libxslt
# BuildRequires:  openssl
# BuildRequires:  perl
# BuildRequires:  python3-coverage
# BuildRequires:  python3-devel >= 3.6
# BuildRequires:  python3-flake8
# BuildRequires:  python3-pylint
# BuildRequires:  python3-pytest
# BuildRequires:  perl(File::Copy)
# BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(File::Which)
# BuildRequires:  perl(File::pushd)
Recommends:     crypto-policies-scripts
Conflicts:      gnutls < 3.7.0
#Conflicts:      libreswan < 3.28
Conflicts:      nss < 3.44.0
#Conflicts:      openssh < 8.2p1
#!BuildIgnore:  crypto-policies
BuildArch:      noarch

%description
This package provides pre-built configuration files with
cryptographic policies for various cryptographic back-ends,
such as SSL/TLS libraries.

%package scripts
Summary:        Tool to switch between crypto policies
Requires:       %{name} = %{version}-%{release}

%description scripts
This package provides a tool update-crypto-policies, which applies
the policies provided by the crypto-policies package. These can be
either the pre-built policies from the base package or custom policies
defined in simple policy definition files.

%prep
%autosetup -p1 -n fedora-%{name}-%{version}

%build
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

# Install the manpages
mkdir -p -m 755 %{buildroot}%{_mandir}/
mkdir -p -m 755 %{buildroot}%{_mandir}/man7/
mkdir -p -m 755 %{buildroot}%{_mandir}/man8/
cp %{SOURCE2} %{buildroot}%{_mandir}/man7/
cp %{SOURCE3} %{buildroot}%{_mandir}/man8/

# Install the executable files
install -p -m 755 update-crypto-policies %{buildroot}%{_bindir}/

install -p -m 644 default-config %{buildroot}%{_sysconfdir}/crypto-policies/config
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/current
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/CURRENT.pol

# Drop pre-generated GOST-ONLY policy, we do not need to ship the files
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/GOST-ONLY

# Remove fips-finish-install and test-fips-setup scripts and man
find -type f -name fips-finish-install -delete
find -type f -name fips-finish-install.8.txt -delete
find -type f -name test-fips-setup.sh -delete

# Create back-end configs for mounting with read-only /etc/
for d in LEGACY DEFAULT FUTURE FIPS ; do
    mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d
    for f in %{buildroot}%{_datarootdir}/crypto-policies/$d/* ; do
        ln $f %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d/$(basename $f .txt).config
    done
done

for f in %{buildroot}%{_datarootdir}/crypto-policies/DEFAULT/* ; do
    ln -sf %{_datarootdir}/crypto-policies/DEFAULT/$(basename $f) %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/$(basename $f .txt).config
done

%py3_compile %{buildroot}%{_datadir}/crypto-policies/python

cp %{SOURCE1} %{buildroot}%{_sysconfdir}/crypto-policies

%check
%make_build test || :

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

%posttrans scripts
%{_bindir}/update-crypto-policies --no-check >/dev/null 2>/dev/null || :

%files
%dir %{_sysconfdir}/crypto-policies/
%dir %{_sysconfdir}/crypto-policies/back-ends/
%dir %{_sysconfdir}/crypto-policies/state/
%dir %{_sysconfdir}/crypto-policies/local.d/
%dir %{_sysconfdir}/crypto-policies/policies/
%dir %{_sysconfdir}/crypto-policies/policies/modules/
%dir %{_datarootdir}/crypto-policies/

%{_sysconfdir}/crypto-policies/README.SUSE
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/config

%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/gnutls.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/openssl.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/opensslcnf.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/openssh.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/opensshserver.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/nss.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/bind.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/java.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/javasystem.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/krb5.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/libreswan.config
%ghost %config(missingok,noreplace) %{_sysconfdir}/crypto-policies/back-ends/libssh.config

%ghost %{_sysconfdir}/crypto-policies/state/current
%ghost %{_sysconfdir}/crypto-policies/state/CURRENT.pol

%{_mandir}/man7/crypto-policies.7%{?ext_man}
%{_datarootdir}/crypto-policies/LEGACY
%{_datarootdir}/crypto-policies/DEFAULT
%{_datarootdir}/crypto-policies/FUTURE
%{_datarootdir}/crypto-policies/FIPS
%{_datarootdir}/crypto-policies/EMPTY
%{_datarootdir}/crypto-policies/back-ends
%{_datarootdir}/crypto-policies/default-config
%{_datarootdir}/crypto-policies/reload-cmds.sh
%{_datarootdir}/crypto-policies/policies

%license COPYING.LESSER

%files scripts
%{_bindir}/update-crypto-policies
%{_mandir}/man8/update-crypto-policies.8%{?ext_man}
%{_datarootdir}/crypto-policies/python

%changelog
