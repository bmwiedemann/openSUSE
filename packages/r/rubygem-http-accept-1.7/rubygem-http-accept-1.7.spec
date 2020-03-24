#
# spec file for package rubygem-http-accept-1.7
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


%define mod_name http-accept
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1.7
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-http-accept-1.7
Version:        1.7.0
Release:        0
Summary:        Parse Accept and Accept-Language HTTP headers
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/ioquatix/http-accept
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

%description
Parse Accept and Accept-Language HTTP headers.

%prep

%build

%install
%gem_install \
  --doc-files="README.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems \( -name .rspec -o -name .travis.yml -o -name .simplecov -o -name .gitignore \) | xargs rm -rf
# /MANUAL


%gem_packages

%changelog
