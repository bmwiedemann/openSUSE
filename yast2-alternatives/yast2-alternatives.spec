#
# spec file for package yast2-alternatives
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


Name:           yast2-alternatives
Version:        4.2.1
Release:        0
Summary:        YaST2 - Manage Update-alternatives switching
License:        GPL-2.0-only
Group:          System/Yast
Url:            https://github.com/yast/yast-alternatives

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings
# For install
BuildRequires:  rubygem(yast-rake)
# For test
BuildRequires:  update-desktop-files
BuildRequires:  rubygem(rspec)

%description
A YaST2 module to manage update alternatives switching

%prep
%setup -q

%build

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
%doc COPYING
%doc README.md

%changelog
