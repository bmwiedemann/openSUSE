#
# spec file for package rubygem-multipart-post
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-multipart-post
Version:        2.1.1
Release:        0
%define mod_name multipart-post
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/nicksieger/multipart-post
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A multipart form post accessory for Net::HTTP
License:        MIT
Group:          Development/Languages/Ruby

%description
Use with Net::HTTP to do multipart form postspec. IO values that have
#content_type, #original_filename, and #local_path will be posted as a binary
file.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt LICENSE README.md" \
  -f

%gem_packages

%changelog
