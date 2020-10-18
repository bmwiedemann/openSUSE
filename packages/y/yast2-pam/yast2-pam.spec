#
# spec file for package yast2-pam
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-pam
Version:        4.3.3
Release:        0
Summary:        YaST2 - PAM Agent
License:        GPL-2.0-only
Group:          System/YaST

URL:            http://github.com/yast/yast-pam
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# cfa for parsing nsswitch
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
# lenses are needed to use cfa
BuildRequires:  augeas-lenses
# testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)

Requires:       yast2
# cfa for parsing nsswitch
Requires:       rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
# lenses are needed to use cfa
Requires:       augeas-lenses
Requires:       pam-config >= 0.8
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
This agent is used by YaST2 to modify the PAM configuration files

%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%build

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%dir %{yast_moduledir}
%{yast_moduledir}/*
%dir %{yast_scrconfdir}
%{yast_scrconfdir}/*.scr
%{yast_libdir}
%dir %{yast_agentdir}
%{yast_agentdir}/ag_passwd
%doc %{yast_docdir}
%license COPYING

%changelog
