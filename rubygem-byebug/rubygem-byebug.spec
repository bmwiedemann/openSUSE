#
# spec file for package rubygem-byebug
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

Name:           rubygem-byebug
Version:        11.0.1
Release:        0
%define mod_name byebug
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby22 ruby23 ruby24
%define rb_default_ruby_abi ruby:2.2.0 ruby:2.3.0 ruby:2.4.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            https://github.com/deivid-rodriguez/byebug
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-byebug-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby fast debugger - base + CLI
License:        BSD-2-Clause
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Byebug is a Ruby debugger. It's implemented using the
TracePoint C API for execution control and the Debug Inspector C API for
call stack navigation.  The core component provides support that front-ends
can build on. It provides breakpoint handling and bindings for stack frames
among other things and it comes with an easy to use command line interface.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
