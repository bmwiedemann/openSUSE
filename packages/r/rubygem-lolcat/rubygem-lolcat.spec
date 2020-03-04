#
# spec file for package rubygem-lolcat
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


%define mod_name lolcat
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-lolcat
Version:        100.0.1
Release:        0
Summary:        Add the colors of the rainbow to your terminal a.k.a. Rainbows and Unicorns!
License:        BSD-3-Clause
Group:          Development/Languages/Ruby
URL:            https://github.com/busyloop/lolcat
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         update-alternatives

%description
This is a console program that transforms text from files or stdin by adding
crazy rainbow colors or even animations.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
