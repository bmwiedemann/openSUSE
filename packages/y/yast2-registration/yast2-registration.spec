#
# spec file for package yast2-registration
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


Name:           yast2-registration
Version:        5.0.2
Release:        0
Summary:        YaST2 - Registration Module
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-registration

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
# Y2Packager::NewRepositorySetup
BuildRequires:  yast2 >= 4.4.42
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-slp >= 3.1.9
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake) >= 0.2.5
# uses Fiddle instead of FFI
BuildRequires:  suseconnect-ruby-bindings > 0.0.4
# new product mapping API
BuildRequires:  yast2-packager >= 5.0.5
BuildRequires:  yast2-update >= 3.1.36
# log.group call
BuildRequires:  yast2-ruby-bindings >= 4.5.4

# Y2Packager::NewRepositorySetup
Requires:       yast2 >= 4.4.42
# "dupAllowVendorChange" option in Pkg.SetSolverFlags()
Requires:       yast2-pkg-bindings >= 3.1.34
# log.group call
Requires:       yast2-ruby-bindings >= 4.5.4
# uses Fiddle instead of FFI
Requires:       suseconnect-ruby-bindings > 0.0.4
Requires:       yast2-add-on >= 3.1.8
Requires:       yast2-slp >= 3.1.9
# new product mapping API
Requires:       yast2-packager >= 5.0.5
Requires:       yast2-update >= 3.1.36

# new calls in AutoinstGeneral
Conflicts:      autoyast2 < 4.3.23

Supplements:    autoyast(suse_register)

BuildArch:      noarch
# SUSEConnect does not build for i586 and s390 and is not supported on those architectures
# bsc#1088552
ExcludeArch:    %ix86 s390

%description
The registration module to register products and/or to fetch an update
source (mirror) automatically.

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_ybindir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_clientdir}
%{yast_ydatadir}
%{yast_schemadir}
%{yast_libdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
