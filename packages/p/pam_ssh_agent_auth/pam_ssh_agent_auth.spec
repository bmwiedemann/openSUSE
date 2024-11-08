#
# spec file for package pam_ssh_agent_auth
#
# Copyright (c) 2024 SUSE LLC
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
# nodebuginfo


%{!?_pam_moduledir: %define _pam_moduledir /%{_lib}/security}

Name:           pam_ssh_agent_auth
Version:        0.10.4
Release:        0
Summary:        Permits PAM authentication via your keyring in a forwarded ssh-agent
License:        OpenSSL
Group:          Development/Tools/Other
URL:            https://github.com/FlorianFranzen/pam_ssh_agent_auth
Source:         %{name}-%{version}.tar.gz
### 20241107: having issues compiling with gcc14, but this patch helps
Patch0:         gcc14-configure.patch
Patch1:         dot-c.patch
Patch2:         bsd-misc.patch
#BuildRequires:  gcc13
#####
BuildRequires:  git-core
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl
BuildRequires:  sed

%description
pam_ssh_agent_auth is a PAM module which permits PAM
authentication via your keyring in a forwarded ssh-agent.

20220111: using https://github.com/FlorianFranzen/pam_ssh_agent_auth,
"just-one-big-cookie" branch so that ed25519 + Yubikey works.

%prep
%setup -q -n %{name}-%{version}
### 20241107: for gcc14
%patch -p1 -P 0
%patch -P 1
%patch -P 2
#####

%build
### 20241107: won't be required for gcc14
#export CC=gcc-13
#####
# 'git submodule init; git submodule update'
#   required before being tar'd up.
%configure \
  --without-openssl-header-check \
  --with-mantype=man \
  --libexecdir=%{_pam_moduledir}
%make_build

%install
%make_install

%files
%doc README
%license LICENSE.OpenSSL
%{_mandir}/man8/%{name}.8.gz
%{_pam_moduledir}/pam_ssh_agent_auth.so

%changelog
