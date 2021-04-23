#
# spec file for package yast2-tftp-server
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-tftp-server
Summary:        YaST2 - TFTP Server Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
Version:        4.3.1
Release:        0
Url:            https://github.com/yast/yast-tftp-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  augeas-lenses
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
# Yast2::Systemd::Service
BuildRequires:  yast2 >= 4.1.3
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa)
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# Yast2::Systemd::Service
Requires:       yast2 >= 4.1.3
# Namespace Y2Journal
Requires:       augeas-lenses
Requires:       lsof
Requires:       yast2-journal >= 4.1.1
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%rb_default_ruby_abi:cfa)

Supplements:    autoyast(tftp-server)

BuildArch:      noarch

%description
The YaST2 component for configuring a TFTP server. TFTP stands for
Trivial File Transfer Protocol. It is used for booting over the
network.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
