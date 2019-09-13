#
# spec file for package rubygem-raindrops
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-raindrops
Version:        0.19.0
Release:        0
%define mod_name raindrops
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            https://bogomips.org/raindrops/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-raindrops-rpmlintrc
Source2:        gem2rpm.yml
Summary:        real-time stats for preforking Rack servers
License:        LGPL-2.1+
Group:          Development/Languages/Ruby

%description
raindrops is a real-time stats toolkit to show statistics for Rack HTTP
servers.  It is designed for preforking servers such as unicorn, but
should support any Rack HTTP server on platforms supporting POSIX shared
memory.  It may also be used as a generic scoreboard for sharing atomic
counters across multiple processes.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING LICENSE NEWS README" \
  -f
%gem_cleanup

%gem_packages

%changelog
