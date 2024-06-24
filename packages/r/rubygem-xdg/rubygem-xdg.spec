#
# spec file for package rubygem-xdg
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-xdg
Version:        8.4.1
Release:        0
%define mod_name xdg
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%define rb_build_versions     ruby33
%define rb_build_ruby_abis    ruby:3.3.0
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby < 4}
BuildRequires:  %{ruby => 3.3}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://alchemists.io/projects/xdg
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A XDG Base Directory Specification implementation
License:        Hippocratic-2.1

%description
A XDG Base Directory Specification implementation.

%prep

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
