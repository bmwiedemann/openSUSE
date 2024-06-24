#
# spec file for package rubygem-yard
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

Name:           rubygem-yard
Version:        0.9.36
Release:        0
%define mod_name yard
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://yardoc.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         yard-do-not-record-timestamps.diff
# /MANUAL
Summary:        Documentation tool for consistent and usable documentation in Ruby
License:        MIT
PreReq:         update-alternatives

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%prep
%gem_unpack
%patch -P 0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LEGAL LICENSE README.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems \( -name .dockerignore -o -name .gitignore -o -name .travis.yml -o -name .rspec -o -name .rubocop.yml -o -name .yardopts -o -name .yardopts_guide -o -name .yardopts_i18n -o -name .github -o -name .gitattributes \) | xargs rm -rf
# /MANUAL

%gem_packages

%changelog
