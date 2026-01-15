#
# spec file for package rubygem-hoe
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           rubygem-hoe
Version:        4.5.1
Release:        0
%define mod_name hoe
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 3.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://www.zenspider.com/projects/hoe.html
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Hoe is a rake/rubygems helper for project Rakefiles
License:        MIT

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
  --no-rdoc --no-ri \
  --symlink-binaries \
  --doc-files="History.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
