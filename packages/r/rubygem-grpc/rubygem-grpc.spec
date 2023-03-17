#
# spec file for package rubygem-grpc
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-grpc
Version:        1.52.0
Release:        0
%define mod_name grpc
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  gcc-c++
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/google/grpc/tree/master/src/ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-grpc.rpmlintrc
Source2:        gem2rpm.yml
Summary:        GRPC system in Ruby
License:        Apache-2.0
Group:          Development/Languages/Ruby

%description
Send RPCs from Ruby using GRPC.

%prep

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
# remove buildroot from .dep files
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '*.dep' \) | xargs sed -i 's|%{buildroot}||'
# /MANUAL

%gem_packages

%changelog
