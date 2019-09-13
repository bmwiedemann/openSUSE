#
# spec file for package rubygem-rake-11_3
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

Name:           rubygem-rake-11_3
Version:        11.3.0
Release:        0
%define mod_name rake
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -11_3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  update-alternatives
Url:            https://github.com/ruby/rake
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Rake is a Make-like program implemented in Ruby
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.
Rake has the following features:
* Rakefiles (rake's version of Makefiles) are completely defined in
standard Ruby syntax.  No XML files to edit.  No quirky Makefile
syntax to worry about (is that a tab or a space?)
* Users can specify tasks with prerequisites.
* Rake supports rule patterns to synthesize implicit tasks.
* Flexible FileLists that act like arrays but know about manipulating
file names and paths.
* A library of prepackaged tasks to make building rakefiles easier. For
example,
tasks for building tarballs and publishing to FTP or SSH sites.  (Formerly
tasks for building RDoc and Gems were included in rake but they're now
available in RDoc and RubyGems respectively.)
* Supports parallel execution of tasks.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc MIT-LICENSE README.rdoc" \
  -f

%gem_packages

%changelog
