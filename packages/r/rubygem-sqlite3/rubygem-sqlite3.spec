#
# spec file for package rubygem-sqlite3
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

Name:           rubygem-sqlite3
Version:        2.1.0
Release:        0
%define mod_name sqlite3
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  %{rubygem mini_portile2 >= 2.8.0}
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 3.1}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
URL:            https://github.com/sparklemotion/sqlite3-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby library to interface with the SQLite3 database engine
License:        BSD-3-Clause

%description
Ruby library to interface with the SQLite3 database engine
(http://www.sqlite.org). Precompiled
binaries are available for common platforms for recent versions of Ruby.

%prep

%build

%install
# MANUAL
# patch out the runtime dep on mini_portile2
%gem_unpack
perl -p -i.back -e 's/.*mini_portile.*//g' %{mod_full_name}.gemspec
diff -urN %{mod_full_name}.gemspec{.back,} ||:
rm -f %{mod_full_name}.gemspec.back

find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build
cd ..
# /MANUAL
%gem_install \
  --extconf-opts="--enable-system-libraries" \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/ -name "*.[h|c|o]" -exec rm {} \;
# /MANUAL

%gem_packages

%changelog
