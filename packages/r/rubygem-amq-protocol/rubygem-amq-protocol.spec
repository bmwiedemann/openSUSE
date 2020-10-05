#
# spec file for package rubygem-amq-protocol
#
# Copyright (c) 2020 SUSE LLC
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

Name:           rubygem-amq-protocol
Version:        2.3.2
Release:        0
%define mod_name amq-protocol
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby22
%define rb_default_ruby_abi ruby:2.2.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            http://github.com/ruby-amqp/amq-protocol
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        AMQP 0.9.1 encoding & decoding library
License:        MIT
Group:          Development/Languages/Ruby

%description
amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not a
client: the library only handles serialization and deserialization.

%prep

%build

%install
%gem_install \
  --doc-files="ChangeLog.md LICENSE README.md" \
  -f

%gem_packages

%changelog
