#
# spec file for package yast2-packager
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


Name:           yast2-packager
Version:        4.5.9
Release:        0
Summary:        YaST2 - Package Library
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-packager

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:cfa) >= 0.5.0
BuildRequires:  rubygem(%{rb_default_ruby_abi}:nokogiri)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# Y2Storage::Device#exists_in_raw_probed
BuildRequires:  yast2-storage-ng >= 4.0.141
# break the yast2-packager -> yast2-storage-ng -> yast2-packager build cycle
#!BuildIgnore: yast2-packager
# Replace PackageSystem with Package
BuildRequires:  yast2 >= 4.4.38
# raw_name
BuildRequires:  yast2-pkg-bindings >= 4.2.8
# yast/rspec/helpers.rb
BuildRequires:  yast2-ruby-bindings >= 4.4.7
# Augeas lenses
BuildRequires:  augeas-lenses
BuildRequires:  ruby-solv

# Newly added RPM
Requires:       yast2-country-data >= 2.16.3
# raw_name
Requires:       yast2-pkg-bindings >= 4.2.8
# Replace PackageSystem with Package
Requires:       yast2 >= 4.4.38
# unzipping license file
Requires:       unzip
# HTTP, FTP, HTTPS modules (inst_productsources.ycp)
Requires:       yast2-transfer
# Bugzilla #305503 - storing/checking MD5 of licenses
Requires:       /usr/bin/md5sum
# .process agent
Requires:       yast2-core >= 2.16.35
# Y2Storage::Device#exists_in_raw_probed
Requires:       yast2-storage-ng >= 4.0.141
# Augeas lenses
Requires:       augeas-lenses
# zypp.conf model and minimal modifications (bsc#1023204)
Requires:       rubygem(%{rb_default_ruby_abi}:cfa) >= 0.5.0
# parsing xml with repositories
Requires:       rubygem(%{rb_default_ruby_abi}:nokogiri)
# One of libyui-qt-pkg, libyui-ncurses-pkg, libyui-gtk-pkg
Requires:       libyui_pkg
Requires:       ruby-solv
Requires:       yast2-ruby-bindings >= 1.0.0

# setenv() builtin
Conflicts:      yast2-core < 2.15.10
# NotEnoughMemory-related functions moved to misc.ycp import-file
Conflicts:      yast2-add-on < 2.15.15

# ensure that 'checkmedia' is on the medium
Recommends:     checkmedia
# for registering media add-ons on SLE
# (openSUSE does not contain the registration module)
%if 0%{?sles_version}
Recommends:     yast2-registration
%endif

# force *-webpin subpackage removal at upgrade
Obsoletes:      yast2-packager-devel-doc
Obsoletes:      yast2-packager-webpin < %version

%description
This package contains the libraries and modules for software management.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%suse_update_desktop_file org.opensuse.yast.Packager
%yast_metainfo

%files
%dir %{yast_yncludedir}/checkmedia
%dir %{yast_yncludedir}/packager
%dir %{yast_libdir}/packager
%dir %{yast_libdir}/packager/cfa
%dir %{yast_libdir}/y2packager
%dir %{yast_ybindir}
%{yast_ybindir}/*
%{yast_yncludedir}/checkmedia/*
%{yast_yncludedir}/packager/*
%{yast_libdir}/language_tag.rb
%{yast_libdir}/packager/*
%{yast_libdir}/y2packager/*
%{yast_libdir}/installation/*
%{yast_clientdir}/*.rb
%{yast_moduledir}/*
%{yast_desktopdir}/*.desktop
%{_datadir}/applications/*.desktop
%{yast_metainfodir}
%{yast_scrconfdir}/*
%{yast_execcompdir}/servers_non_y2/ag_*
%{yast_icondir}
%dir %{yast_docdir}
%license COPYING
%doc %{yast_docdir}/README.md

%changelog
