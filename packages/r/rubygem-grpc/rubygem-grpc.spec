#
# spec file for package rubygem-grpc
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

Name:           rubygem-grpc
Version:        1.70.1
Release:        0
%define mod_name grpc
%define mod_full_name %{mod_name}-%{version}
# MANUAL
#define rb_build_versions     %{my_apps_rb_build_versions}
#define rb_build_ruby_abis    %{my_apps_rb_build_abi}
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel >= 1.70.0
BuildRequires:  pkgconfig
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 3.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://github.com/google/grpc/tree/master/src/ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-grpc.rpmlintrc
Source2:        series
Source3:        gem2rpm.yml
# MANUAL
Patch0:         0001-Return-Qnil-from-grpc_rb_fork_unsafe_begin-end_api.patch
Patch1:         use_system_libs.patch
Patch2:         gcc14.patch
Patch3:         use_system_certs.patch
# /MANUAL
Summary:        GRPC system in Ruby
License:        Apache-2.0

%description
Send RPCs from Ruby using GRPC.

%prep
%gem_unpack
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  -f
%gem_cleanup
# MANUAL
# drop files from the git repository
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.sitearchdir.-.grpc.time' -o -name '.yardopts' \) | xargs rm
# fix permissions
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name 'ca.pem' -o -name 'server1.key' -o -name 'server1.pem' \) | xargs chmod -x
rm -rf %{buildroot}%{_libdir}/ruby/gems/*/gems/grpc-%{version}/src/ruby/ext/grpc/{libs,objs}/
rm -rf %{buildroot}%{_libdir}/ruby/gems/*/gems/grpc-%{version}/src/ruby/spec/
rm -rf %{buildroot}%{_libdir}/ruby/gems/*/gems/grpc-%{version}/etc
# /MANUAL

%gem_packages

%changelog
