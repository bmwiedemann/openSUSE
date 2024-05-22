#
# spec file for package rubygem-google-protobuf
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

Name:           rubygem-google-protobuf
Version:        3.25.2
Release:        0
%define mod_name google-protobuf
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubydevel >= 2.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://developers.google.com/protocol-buffers
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-google-protobuf-rpmlintrc
Source2:        gem2rpm.yml
# MANUAL
Patch0:         do-not-wrap.patch
Patch1:         0001-ruby-return-0-from-shared_convert.c-shared_message.c.patch
# /MANUAL
Summary:        Protocol Buffers
License:        BSD-3-Clause

%description
Protocol Buffers are Google's data interchange format.

%prep
%gem_unpack
%patch -P 0 -p1
%patch -P 1 -p2
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.sitearchdir.-.google.time' \) -delete
# upstream did a chmod 0777 on everything
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '*.c' -o -name '*.h' -o -name '*.rb' -o -name 'LICENSE' \) -print0 | xargs -r0 chmod -x
# add the executable bit back to all scripts
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name 'well_known_types.rb' -o -name 'descriptor_dsl.rb' -o -name 'extconf.rb' \) -print0 | xargs -r0 chmod +x
# /MANUAL

%gem_packages

%changelog
