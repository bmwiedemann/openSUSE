#
# spec file for package rubygem-ipaddress
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-ipaddress
Version:        0.8.3
Release:        0
%define mod_name ipaddress
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/bluemonk/ipaddress
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        IPv4/IPv6 address manipulation library
License:        MIT
Group:          Development/Languages/Ruby

%description
IPAddress is a Ruby library designed to make manipulation 
of IPv4 and IPv6 addresses both powerful and simple. It mantains
a layer of compatibility with Ruby's own IPAddr, while 
addressing many of its issues.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.rdoc LICENSE.txt README.rdoc" \
  -f

%gem_packages

%changelog
