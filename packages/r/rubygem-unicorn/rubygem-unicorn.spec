#
# spec file for package rubygem-unicorn
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-unicorn
Version:        5.5.0
Release:        0
%define mod_name unicorn
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel < 3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            https://bogomips.org/unicorn/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-unicorn-rpmlintrc
Source2:        series
Source3:        gem2rpm.yml
# MANUAL
Patch0:         unicorn-4.6.3_fix_shebangline.patch
Patch1:         6836d06.patch
# /MANUAL
Summary:        Rack HTTP server for fast clients and Unix
License:        GPL-2.0-only OR GPL-3.0-only OR Ruby
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between unicorn and slow clients.

%prep
%gem_unpack
%patch0 -p0
%patch1 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="COPYING LICENSE NEWS README" \
  -f
%gem_cleanup

%gem_packages

%changelog
