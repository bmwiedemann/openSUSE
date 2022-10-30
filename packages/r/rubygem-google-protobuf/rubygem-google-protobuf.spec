#
# spec file for package rubygem-google-protobuf
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

Name:           rubygem-google-protobuf
Version:        3.21.9
Release:        0
%define mod_name google-protobuf
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%global _lto_cflags %{nil}
%if 0%{?suse_version} > 1500
%define rb_build_versions ruby31
%define rb_build_ruby_abi ruby:3.1.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://developers.google.com/protocol-buffers
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-google-protobuf-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Languages/Ruby

%description
Protocol Buffers are Google's data interchange format.

%prep

%build

%install
%gem_install \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.sitearchdir.-.google.time' \) | xargs rm
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name 'ruby-upb.c' -o -name 'ruby-upb.h' \) | xargs chmod -x
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name 'descriptor_dsl.rb' \) | xargs chmod +x
# /MANUAL

%gem_packages

%changelog
