#
# spec file for package rubygem-inifile
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-inifile
Version:        3.0.0
Release:        0
%define mod_name inifile
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://rubygems.org/gems/inifile
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        INI file reader and writer
License:        MIT
Group:          Development/Languages/Ruby

%description
Although made popular by Windows, INI files can be used on any system thanks
to their flexibility. They allow a program to store configuration data, which
can then be easily parsed and changed. Two notable systems that use the INI
format are Samba and Trac.
More information about INI files can be found on the [Wikipedia
Page](http://en.wikipedia.org/wiki/INI_file).
### Properties
The basic element contained in an INI file is the property. Every property has
a name and a value, delimited by an equals sign *=*. The name appears to the
left of the equals sign and the value to the right.
name=value
### Sections
Section declarations start with *[* and end with *]* as in `[section1]` and
`[section2]` shown in the example below. The section declaration marks the
beginning of a section. All properties after the section declaration will be
associated with that section.
### Comments
All lines beginning with a semicolon *;* or a number sign *#* are considered
to be comments. Comment lines are ignored when parsing INI files.
### Example File Format
A typical INI file might look like this:
[section1]
; some comment on section1
var1 = foo
var2 = doodle
var3 = multiline values \
are also possible
[section2]
# another comment
var1 = baz
var2 = shoodle.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt README.md" \
  -f

%gem_packages

%changelog
