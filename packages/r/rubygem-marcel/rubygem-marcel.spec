#
# spec file for package rubygem-marcel
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-marcel
Version:        1.0.1
Release:        0
%define mod_name marcel
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby23 ruby24 ruby25
%define rb_build_ruby_abi ruby:2.3.0 ruby:2.4.0 ruby:2.5.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.2}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/rails/marcel
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Simple mime type detection using magic numbers, filenames, and
License:        MIT and Apache-2.0
Group:          Development/Languages/Ruby

%description
Simple mime type detection using magic numbers, filenames, and extensions.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE" \
  -f

%gem_packages

%changelog
