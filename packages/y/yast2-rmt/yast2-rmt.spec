#
# spec file for package yast2-rmt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-rmt
Version:        1.3.4
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Source99:       %{name}-rpmlintrc

Requires:       rmt-server >= 2.5.0
Requires:       yast2
Requires:       yast2-ruby-bindings

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-ruby-bindings
#for install task
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# for tests
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)

Summary:        YaST2 - Module to configure RMT
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-rmt
# ExcludeArch synced with our main dependency: rmt-server
ExcludeArch:    %{ix86} s390

%description
Provides the YaST module to configure the Repository Mirroring Tool (RMT) Server.

%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%{yast_dir}/clients/*.rb
%{yast_dir}/lib/rmt
%{yast_desktopdir}/rmt.desktop
%{yast_dir}/data/rmt

%doc COPYING
%doc README.md

%build

%changelog
