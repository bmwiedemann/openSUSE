#
# spec file for package rubygem-vagrant-spec
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-vagrant-spec
Version:        0.0.1.abfc344.git
Release:        0
%define mod_name vagrant-spec
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
Url:            https://github.com/mitchellh/vagrant-spec
# MANUALLY modified:
Source:         %{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Tool and library for testing Vagrant plugins
License:        MPL-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
vagrant-spec is a both a specification of how Vagrant and its various
components should behave as well as a library of testing helpers that let you
write your own unit and acceptance tests for Vagrant.

The library provides a set of helper methods in addition to RSpec matchers and
expectations to help you both unit test and acceptance test Vagrant
components. The RSpec components are built on top of the helper methods so
that the test library can be used with your test framework of choice, but the
entire tool is geared very heavily towards RSpec.
%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt README.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems \( -name .gitignore -o -name .travis.yml \) | xargs rm
# /MANUAL


%gem_packages

%changelog
