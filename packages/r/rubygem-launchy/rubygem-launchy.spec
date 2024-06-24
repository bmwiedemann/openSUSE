#
# spec file for package rubygem-launchy
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

Name:           rubygem-launchy
Version:        3.0.1
Release:        0
%define mod_name launchy
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/copiousfreetime/launchy
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Launchy is helper class for launching cross-platform applications in
License:        ISC
PreReq:         update-alternatives

%description
Launchy is helper class for launching cross-platform applications in a fire
and forget manner. There are application concepts (browser, email client, etc)
that are common across all platforms, and they may be launched differently on
each platform. Launchy is here to make a common approach to launching external
applications from within ruby programs.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="HISTORY.md LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
