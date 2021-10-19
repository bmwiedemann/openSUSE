#
# spec file for package pam_ssh_agent_auth
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
# nodebuginfo

%{!?_pam_moduledir: %define _pam_moduledir /%{_lib}/security}

Name:           pam_ssh_agent_auth
Version:        0.10.4
Release:        0
Summary:        PAM module providing authentication via ssh-agent
License:        OpenSSL
Group:          Development/Tools/Other
URL:            https://github.com/jbeverly/pam_ssh_agent_auth
Source:         %{name}-%{version}.tar.gz
Source99:       git-script.sh
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl
BuildRequires:  sed

%description
pam_ssh_agent_auth is a PAM module which permits PAM
authentication via your keyring in a forwarded ssh-agent.

%prep
%setup -q -n %{name}-%{version}

%build
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

