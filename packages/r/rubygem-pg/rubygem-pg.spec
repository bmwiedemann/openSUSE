#
# spec file for package rubygem-pg
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-pg
Version:        1.2.3
Release:        0
%define mod_name pg
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/ged/ruby-pg
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-pg-rpmlintrc
Source2:        gem2rpm.yml
# MANUAL
Patch0:         use-pkg-config.patch
# /MANUAL
Summary:        Pg is the Ruby interface to the PostgreSQL RDBMS
License:        BSD-2-Clause
Group:          Development/Languages/Ruby

%description
Pg is the Ruby interface to the {PostgreSQL
RDBMS}[http://www.postgresql.org/].
It works with {PostgreSQL 9.2 and
later}[http://www.postgresql.org/support/versioning/].
A small example usage:
#!/usr/bin/env ruby
require 'pg'
# Output a table of current connections to the DB
conn = PG.connect( dbname: 'sales' )
conn.exec( "SELECT * FROM pg_stat_activity" ) do |result|
puts "     PID | User             | Query"
result.each do |row|
puts " %7d | %-16s | %s " %
row.values_at('procpid', 'usename', 'current_query')
end
end.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="ChangeLog History.rdoc LICENSE README.rdoc" \
  -f
%gem_cleanup

%gem_packages

%changelog
