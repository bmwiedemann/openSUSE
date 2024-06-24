#
# spec file for package rubygem-hoe
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

Name:           rubygem-hoe
Version:        4.2.1
Release:        0
%define mod_name hoe
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby < 4}
BuildRequires:  %{ruby >= 2.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://www.zenspider.com/projects/hoe.html
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Hoe is a rake/rubygems helper for project Rakefiles
License:        MIT
PreReq:         update-alternatives

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you
manage, maintain, and release your project and includes a dynamic
plug-in system allowing for easy extensibility. Hoe ships with
plug-ins for all your usual project tasks including rdoc generation,
testing, packaging, deployment, and announcement.
See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed
below.
For extra goodness, see: http://docs.seattlerb.org/hoe/Hoe.pdf.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
