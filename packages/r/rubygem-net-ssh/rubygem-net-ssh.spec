#
# spec file for package rubygem-net-ssh
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

Name:           rubygem-net-ssh
Version:        6.1.0
Release:        0
%define mod_name net-ssh
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/net-ssh/net-ssh
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License:        MIT
Group:          Development/Languages/Ruby

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows
you to write programs that invoke and interact with processes on remote
servers, via SSH2.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES.txt LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
