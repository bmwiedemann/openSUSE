#
# spec file for package rubygem-prism
#
# Copyright (c) 2025 SUSE LLC
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

Name:           rubygem-prism
Version:        1.4.0
Release:        0
%define mod_name prism
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 2.7.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://github.com/ruby/prism
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Prism Ruby parser
License:        MIT

%description
Prism Ruby parser.

%prep

%build

%install
%gem_install \
  --no-rdoc --no-ri \
  --doc-files="CHANGELOG.md LICENSE.md README.md" \
  -f
%gem_cleanup
# MANUAL
rm -rvf %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_full_name}/{build,ext,include,src}
# /MANUAL


%gem_packages

%changelog
