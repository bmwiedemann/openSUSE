#
# spec file for package rubygem-pry
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

Name:           rubygem-pry
Version:        0.14.2
Release:        0
%define mod_name pry
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://pry.github.io
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A runtime developer console and IRB alternative with powerful
License:        MIT
PreReq:         update-alternatives

%description
Pry is a runtime developer console and IRB alternative with powerful
introspection capabilities. Pry aims to be more than an IRB replacement. It is
an attempt to bring REPL driven programming to the Ruby language.

%prep

%build

%install
%gem_install \
  --no-rdoc --no-ri \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f

%gem_packages

%changelog
