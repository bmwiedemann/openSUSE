#
# spec file for package rubygem-fake_ftp-0_1
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-fake_ftp-0_1
Version:        0.1.1
Release:        0
%define mod_name fake_ftp
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -0_1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://rubygems.org/gems/fake_ftp
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A fake FTP server for use with RSpec
License:        MIT
Group:          Development/Languages/Ruby

%description
This is a gem that allows you to test FTP implementations in ruby. It is a minimal single-client FTP server that can be bound to any arbitrary port on localhost.
%prep

%build

%install
%gem_install \
  --doc-files="README.md" \
  -f

%gem_packages

%changelog
