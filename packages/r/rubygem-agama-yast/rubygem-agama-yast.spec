#
# spec file for package rubygem-agama-yast
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-agama-yast
Version:        14.devel10.952ad275a
Release:        0
%define mod_name agama-yast
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%global rb_build_versions %{rb_default_ruby}
BuildRequires:  dbus-1-common
Requires:       dbus-1-common
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
URL:            https://github.com/openSUSE/agama
Source:         %{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        YaST integration service for Agama
License:        GPL-2.0-only

%description
D-Bus service exposing some YaST features that are useful for Agama.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  -f

%gem_packages

%changelog
