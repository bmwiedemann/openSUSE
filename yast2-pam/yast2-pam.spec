#
# spec file for package yast2-pam
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-pam
Version:        4.2.4
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Url:            http://github.com/yast/yast-pam
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       yast2

Requires:       pam-config >= 0.8

BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - PAM Agent
License:        GPL-2.0-only
Group:          System/YaST

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
%dir %{yast_agentdir}
%{yast_agentdir}/ag_passwd
%doc %{yast_docdir}
%license COPYING

%changelog
