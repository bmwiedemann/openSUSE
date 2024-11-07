#
# spec file for package rubygem-path_expander
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

Name:           rubygem-path_expander
Version:        1.1.3
Release:        0
%define mod_name path_expander
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/seattlerb/path_expander
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        PathExpander helps pre-process command-line arguments expanding
License:        MIT

%description
PathExpander helps pre-process command-line arguments expanding
directories into their constituent files. It further helps by
providing additional mechanisms to make specifying subsets easier
with path subtraction and allowing for command-line arguments to be
saved in a file.
NOTE: this is NOT an options processor. It is a path processor
(basically everything else besides options). It does provide a
mechanism for pre-filtering cmdline options, but not with the intent
of actually processing them in PathExpander. Use OptionParser to
deal with options either before or after passing ARGV through
PathExpander.

%prep

%build

%install
%gem_install \
  --doc-files="History.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
