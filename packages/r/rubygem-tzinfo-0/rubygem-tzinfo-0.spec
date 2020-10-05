#
# spec file for package rubygem-tzinfo-0
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

Name:           rubygem-tzinfo-0
Version:        0.3.57
Release:        0
%define mod_name tzinfo
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            http://tzinfo.github.io
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Daylight-savings aware timezone library
License:        MIT
Group:          Development/Languages/Ruby

%description
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES LICENSE README" \
  -f

%gem_packages

%changelog
