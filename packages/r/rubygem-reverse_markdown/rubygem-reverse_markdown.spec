#
# spec file for package rubygem-reverse_markdown
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

Name:           rubygem-reverse_markdown
Version:        3.0.0
Release:        0
%define mod_name reverse_markdown
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://github.com/xijo/reverse_markdown
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Convert html code into markdown
License:        WTFPL

%description
Map simple html back into markdown, e.g. if you want to import existing html
data in your application.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems \( -name .gitignore -o -name .travis.yml -o -name .rspec \) | xargs rm
# /MANUAL

%gem_packages

%changelog
