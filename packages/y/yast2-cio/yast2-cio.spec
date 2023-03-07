#
# spec file for package yast2-cio
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


######################################################################
#
# IMPORTANT: Please do not change spec file in build service directly
#            Use https://github.com/yast/yast-cio repo
#
######################################################################

Name:           yast2-cio
Version:        4.6.1
Release:        0
Summary:        YaST2 - IO Channel management
Group:          System/YaST
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/yast/yast-cio

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 3.0.5
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings >= 1.2.0
#for install task
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# for tests
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)

Requires:       s390-tools
Requires:       yast2 >= 3.0.5
Requires:       yast2-ruby-bindings >= 1.2.0

Supplements:    yast2-s390

ExclusiveArch:  s390 s390x

%description
Provides interface for blacklisting and unblocking IO channels

%prep
%setup -q

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%doc README.md
%license COPYING

%changelog
