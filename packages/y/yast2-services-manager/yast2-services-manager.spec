#
# spec file for package yast2-services-manager
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
#            Use https://github.com/yast/yast-services-manager repo
#
######################################################################

Name:           yast2-services-manager
Version:        4.6.0
Release:        0
Summary:        YaST2 - Services Manager
Group:          System/YaST
License:        GPL-2.0-or-later
URL:            https://github.com/yast/yast-services-manager

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  ruby
BuildRequires:  update-desktop-files
# 'target' argument for Installation::AutoClient#export method
BuildRequires:  yast2 >= 4.3.10
BuildRequires:  yast2-ruby-bindings >= 1.2.0
# To show service logs
BuildRequires:  yast2-journal >= 4.1.1
# Support for 'data' directory in rake install task
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake) >= 0.1.7
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# The tests need systemctl
BuildRequires:  pkgconfig(systemd)

Requires:       ruby
 # 'target' argument for Installation::AutoClient#export method
Requires:       yast2 >= 4.3.10
Requires:       yast2-ruby-bindings >= 1.2.0

# To show service logs
Suggests:       yast2-journal >= 4.1.1

Obsoletes:      yast2-runlevel

# need new enough installation for its inst clients
Conflicts:      yast2-installation < 3.1.32
Conflicts:      yast2-runlevel

Supplements:    autoyast(services-manager)

BuildArch:      noarch

%description
Provides user interface and libraries to configure systemd
services and targets.

%prep
%setup -q

%build

%check
rake test:unit

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_moduledir}
%{yast_schemadir}
%{yast_libdir}
%{yast_ydatadir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
