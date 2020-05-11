#
# spec file for package rubygem-commander
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

Name:           rubygem-commander
Version:        4.5.2
Release:        0
%define mod_name commander
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/commander-rb/commander
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        The complete solution for Ruby command-line executables
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
The complete solution for Ruby command-line executables. Commander bridges the
gap between other terminal related libraries you know and love (OptionParser,
HighLine), while providing many new features, and an elegant API.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc LICENSE README.md" \
  -f

%gem_packages

%changelog
