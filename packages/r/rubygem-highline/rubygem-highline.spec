#
# spec file for package rubygem-highline
#
# Copyright (c) 2023 SUSE LLC
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

Name:           rubygem-highline
Version:        2.1.0
Release:        0
%define mod_name highline
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/JEG2/highline
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        HighLine is a high-level command-line IO library
License:        Ruby

%description
A high-level IO library that provides validation, type conversion, and more
for
command-line interfaces. HighLine also includes a complete menu system that
can
crank out anything from simple list selection to complete shells with just
minutes of work.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING Changelog.md LICENSE README.md" \
  -f
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name .gitignore -delete
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name .cvsignore -delete

rm -rf %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/examples
# /MANUAL

%gem_packages

%changelog
