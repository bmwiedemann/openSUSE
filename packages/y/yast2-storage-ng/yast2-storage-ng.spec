#
# spec file for package yast2-storage-ng
#
# Copyright (c) 2025 SUSE LLC
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


Name:           yast2-storage-ng
Version:        5.0.32
Release:        0
Summary:        YaST2 - Storage Configuration
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-storage-ng

Source:         %{name}-%{version}.tar.bz2

# RB_FILESYSTEM_MOUNT_READ_ONLY
BuildRequires:  libstorage-ng-ruby >= 4.5.246
BuildRequires:  update-desktop-files
# Arch.has_tpm2
BuildRequires:  yast2 >= 5.0.13
BuildRequires:  yast2-devtools >= 4.2.2
# yast/rspec/helpers.rb
BuildRequires:  yast2-ruby-bindings >= 4.4.7
# yast2-xml dependency is added by yast2 but ignored in the
# openSUSE:Factory project config
BuildRequires:  yast2-xml
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# communicate with udisks
BuildRequires:  rubygem(%{rb_default_ruby_abi}:ruby-dbus)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# speed up the tests in SLE15-SP1+ or TW
%if 0%{?sle_version} >= 150100 || 0%{?suse_version} > 1500
BuildRequires:  rubygem(%{rb_default_ruby_abi}:parallel_tests)
%endif

# findutils for xargs
Requires:       findutils
# RB_FILESYSTEM_MOUNT_READ_ONLY
Requires:       libstorage-ng-ruby >= 4.5.246
# Require libstorage bindings for the current Ruby version (bsc#1235598)
Requires:       libstorage-ng-ruby-%{rb_ver}
# Arch.has_tpm2
Requires:       yast2 >= 5.0.13
# Y2Packager::Repository
Requires:       yast2-packager >= 3.3.7
# for AbortException and handle direct abort
Requires:       yast2-ruby-bindings >= 4.0.6
# OpenItems for (nested) tables
Requires:       yast2-ycp-ui-bindings >= 4.3.4
# communicate with udisks
Requires:       rubygem(%{rb_default_ruby_abi}:ruby-dbus)
Requires(post): %fillup_prereq

Recommends:     (libyui-qt-graph if libyui-qt)

Obsoletes:      yast2-storage

%description
This package contains the files for YaST2 that handle access to disk
devices during installation and on an installed system.
This YaST2 module uses libstorage-ng.

%prep
%setup -q

%check
rake test:unit

%build

%install
%yast_install
%yast_metainfo

%post
%{fillup_only -ans storage %{name}.common}
%ifarch s390 s390x
%{fillup_only -ans storage %{name}.s390}
%else
%{fillup_only -ans storage %{name}.default}
%endif

%files
%license COPYING
%doc README.md
%{yast_clientdir}
%{yast_desktopdir}
%{yast_libdir}
%{yast_ybindir}
%{_fillupdir}/*%{name}*
# agents-scr
%{yast_scrconfdir}
%{_datadir}/icons/hicolor/*/apps/yast-disk.*
%{_datadir}/metainfo/org.opensuse.yast.Disk.metainfo.xml

%changelog
