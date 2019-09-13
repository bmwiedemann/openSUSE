#
# spec file for package rubygem-diff-lcs
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

Name:           rubygem-diff-lcs
Version:        1.3
Release:        0
%define mod_name diff-lcs
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 1.8}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            https://github.com/halostatue/diff-lcs
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         fix-interpreter.patch
# /MANUAL
Summary:        Diff::LCS computes the difference between two Enumerable sequences
License:        MIT and Artistic-2.0 and GPL-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.
This is release 1.3, providing a tentative fix to a long-standing issue
related
to incorrect detection of a patch direction. Also modernizes the gem
infrastructure, testing infrastructure, and provides a warning-free experience
to Ruby 2.4 users.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.md License.md README.rdoc" \
  -f

%gem_packages

%changelog
