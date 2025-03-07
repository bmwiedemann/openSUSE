#
# spec file for package rubygem-childprocess
#
# Copyright (c) 2024 SUSE LLC
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

Name:           rubygem-childprocess
Version:        5.1.0
Release:        0
%define mod_name childprocess
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.4.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/enkessler/childprocess
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A simple and reliable solution for controlling external programs
License:        MIT

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
# MANUAL
# delete custom files here or do other fancy stuff
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.document' -o -name '.travis.yml' -o -name '.gitignore' -o -name '.rspec' \) | xargs rm
# /MANUAL

%gem_packages

%changelog
