#
# spec file for package rubygem-ruby-dbus
#
# Copyright (c) 2021 SUSE LLC
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

Name:           rubygem-ruby-dbus
Version:        0.16.0
Release:        0
%define mod_name ruby-dbus
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  %{rubygem nokogiri >= 1.10.4}
BuildRequires:  %{rubygem packaging_rake_tasks}
BuildRequires:  %{rubygem rake}
BuildRequires:  %{rubygem rspec}
BuildRequires:  dbus-1
BuildRequires:  netcfg
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/mvidner/ruby-dbus
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby module for interaction with D-Bus
License:        LGPL-2.1-only
Group:          Development/Languages/Ruby

%description
Pure Ruby module for interaction with D-Bus IPC system.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING NEWS.md README.md" \
  -f

# MANUAL
%check
(pushd %{buildroot}%{gem_base}/gems/%{mod_full_name} && rake test)
#/ MANUAL

%gem_packages

%changelog
