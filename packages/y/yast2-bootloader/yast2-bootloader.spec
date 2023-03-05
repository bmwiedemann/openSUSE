#
# spec file for package yast2-bootloader
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


Name:           yast2-bootloader
Version:        4.6.0
Release:        0
Summary:        YaST2 - Bootloader Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-bootloader
Source0:        %{name}-%{version}.tar.bz2

# ReducedRecorder
BuildRequires:  yast2 >= 4.5.16
BuildRequires:  yast2-devtools >= 4.2.2
# yast/rspec/helpers.rb
BuildRequires:  yast2-ruby-bindings >= 4.4.7
# BlkDevice#preferred_name and Filesystems::BlkFilesystem#preferred_name
BuildRequires:  yast2-storage-ng >= 4.3.36
# lenses needed also for tests
BuildRequires:  augeas-lenses
BuildRequires:  update-desktop-files
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa_grub2) >= 1.0.1
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

PreReq:         %fillup_prereq
PreReq:         /bin/sed
# Base classes for inst clients
Requires:       parted
# ReducedRecorder
Requires:       yast2 >= 4.5.16
Requires:       yast2-core >= 2.18.7
Requires:       yast2-packager >= 2.17.24
Requires:       yast2-pkg-bindings >= 2.17.25
# Y2Storage::Arch#efibootmgr?
Requires:       yast2-storage-ng >= 4.4.22
# Support for multiple values in GRUB_TERMINAL
Requires:       rubygem(%rb_default_ruby_abi:cfa_grub2) >= 1.0.1
# lenses are needed as cfa_grub2 depends only on augeas bindings, but also
# lenses are needed here
Requires:       augeas-lenses
Requires:       yast2-ruby-bindings >= 1.0.0

# only recommend syslinux, as it is not needed when generic mbr is not used (bsc#1004229)
%ifarch %ix86 x86_64
Recommends:     syslinux
%endif

Supplements:    autoyast(bootloader)

%description
This package contains the YaST2 component for bootloader configuration.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%post
%{fillup_only -n bootloader}

%files
%license COPYING
%doc %{yast_docdir}
%{yast_desktopdir}
%{yast_moduledir}
%{yast_clientdir}
%{yast_ybindir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_libdir}
%{_fillupdir}/sysconfig.bootloader.*
%{_datadir}/metainfo/org.opensuse.yast.Bootloader.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/yast-bootloader*

%changelog
