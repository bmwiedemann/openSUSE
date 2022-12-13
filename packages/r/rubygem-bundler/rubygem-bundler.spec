#
# spec file for package rubygem-bundler
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-bundler
Version:        2.3.26
Release:        0
%define mod_name bundler
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} < 1500
%define rb_build_versions     ruby27
%define rb_build_ruby_abis    ruby:2.7.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://bundler.io
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        series
Source2:        gem2rpm.yml
Summary:        The best way to manage your application's dependencies
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE.md README.md" \
  -f

%gem_packages

%changelog
