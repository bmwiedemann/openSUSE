#
# spec file for package rubygem-ruby-shadow
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-ruby-shadow
Version:        2.5.0
Release:        0
%define mod_name ruby-shadow
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 1.8}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/apalmblad/ruby-shadow
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        *nix Shadow Password Module
License:        SUSE-Public-Domain
Group:          Development/Languages/Ruby

%description
This module provides access to shadow passwords on Linux, OSX, FreeBSD,
OpenBSD, and Solaris.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY LICENSE README" \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/ -name "*.[h|c]" -exec rm {} \;
# /MANUAL

%gem_packages

%changelog
