#
# spec file for package rubygem-cool.io
#
# Copyright (c) 2021 SUSE LLC
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

Name:           rubygem-cool.io
Version:        1.7.0
Release:        0
%define mod_name cool.io
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            http://coolio.github.com
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Source2:        rubygem-cool.io-rpmlintrc
Source3:        gem2rpm.yml
Summary:        A cool framework for doing high performance I/O in Ruby
License:        MIT
Group:          Development/Languages/Ruby

%description
Cool.io provides a high performance event framework for Ruby which uses the
libev C library.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
