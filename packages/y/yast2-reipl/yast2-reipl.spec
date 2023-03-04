#
# spec file for package yast2-reipl
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


Name:           yast2-reipl
Version:        4.6.0
Release:        0
Summary:        YaST2 - IPL loader
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-reipl

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

PreReq:         %fillup_prereq
Requires:       yast2-ruby-bindings >= 1.0.0
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.22
# needed for chreipl and lsreipl commands
Requires:       s390-tools

Supplements:    yast2-s390

ExclusiveArch:  s390 s390x

%description
Module for loading IPL from running system on S/390

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%post
%{fillup_only -ns security checksig}

%files
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_yncludedir}
%doc %{yast_docdir}
%license COPYING

%changelog
