#
# spec file for package yast2-update
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-update
Version:        4.5.2
Release:        0
Summary:        YaST2 - Update
Group:          System/YaST
License:        GPL-2.0-only
URL:            https://github.com/yast/yast-update

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings >= 1.0.0
# Product#register_target
BuildRequires:  yast2 >= 4.4.25
# ProductSpec#register_target
BuildRequires:  yast2-packager >= 4.4.15
# xmllint
BuildRequires:  libxml2-tools
# control.rng
BuildRequires:  yast2-installation-control
# Needed for tests
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# nokogiri is used also for parsing in tests. It is not problem as yast2 also depends on it
BuildRequires:  rubygem(%{rb_default_ruby_abi}:nokogiri)
# Y2Storage::Crypttab.save_encryption_names
BuildRequires:  yast2-storage-ng >= 4.2.42

# Y2Storage::Crypttab.save_encryption_names
Requires:       yast2-storage-ng >= 4.2.42
# Product#register_target
Requires:       yast2 >= 4.4.25
Requires:       yast2-installation
# ProductSpec#register_target
Requires:       yast2-packager >= 4.4.15
# filtering orphaned packages
Requires:       yast2-pkg-bindings >= 4.5.1
Requires:       yast2-ruby-bindings >= 1.0.0
# nokogiri is used for parsing pam conf.
Requires:       rubygem(%{rb_default_ruby_abi}:nokogiri)
# use parallel gzip when crating backup (much faster)
Requires:       pigz

# moved into yast2-update from yast2-installation
# to remove dependency on yast2-storage
Provides:       yast2-installation:/usr/share/YaST2/clients/vendor.ycp

# Pkg::PkgUpdateAll (map conf)
Conflicts:      yast2-pkg-bindings < 2.15.11
# Storage::DeviceMatchFstab (#244117)
Conflicts:      yast2-storage < 2.15.4

%description
Use this component if you wish to update your system.

%package FACTORY
Summary:        YaST2 - Update
Group:          System/YaST

PreReq:         %fillup_prereq

Requires:       yast2
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-update

# moved into yast2-update from yast2-installation
# to remove dependency on yast2-storage
Provides:       yast2-update:/usr/share/YaST2/clients/update.ycp

%description FACTORY
Use this component if you wish to update your system.

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_moduledir}
%{yast_clientdir}/inst_rootpart.rb
%{yast_clientdir}/inst_backup.rb
%{yast_clientdir}/rootpart_proposal.rb
%{yast_clientdir}/update_proposal.rb
%{yast_clientdir}/packages_proposal.rb
%{yast_clientdir}/backup_proposal.rb
%{yast_clientdir}/inst_update_partition.rb
%{yast_clientdir}/inst_update_partition_auto.rb
%{yast_yncludedir}
%{yast_libdir}
%doc %{yast_docdir}

%files FACTORY
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%{yast_controldir}
%{yast_clientdir}/update.rb
%{yast_clientdir}/run_update.rb
%license COPYING

%changelog
