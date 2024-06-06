#
# spec file for package rubygem-diff-lcs
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

Name:           rubygem-diff-lcs
Version:        1.5.0
Release:        0
%define mod_name diff-lcs
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 1.8}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/halostatue/diff-lcs
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         fix-interpreter.patch
# /MANUAL
Summary:        Diff::LCS computes the difference between two Enumerable sequences
License:        Artistic-2.0 AND MIT AND GPL-2.0-only
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.
This is release 1.4.3, providing a simple extension that allows for
Diff::LCS::Change objects to be treated implicitly as arrays and fixes a
number of formatting issues.
Ruby versions below 2.5 are soft-deprecated, which means that older versions
are no longer part of the CI test suite. If any changes have been introduced
that break those versions, bug reports and patches will be accepted, but it
will be up to the reporter to verify any fixes prior to release. The next
major release will completely break compatibility.

%prep
%gem_unpack
%patch -P 0 -p1
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
