#
# spec file for package ruby
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


Name:           ruby
Version:        3.2
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         README
Url:            http://www.ruby-lang.org/
Summary:        An Interpreted Object-Oriented Scripting Language
License:        MIT
Group:          Development/Languages/Ruby
BuildRequires:  ruby%{version}-devel
#!BuildIgnore:  ruby
#!BuildIgnore:  rubygem-gem2rpm
%requires_ge ruby%{version}
Provides:       rubygems = 1.8.15
Obsoletes:      rubygems < 1.8.15

%description
Ruby is an interpreted scripting language for quick and easy
object-oriented programming.  It has many features for processing text
files and performing system management tasks (as in Perl).  It is
simple, straight-forward, and extensible.

* Ruby features:

- Simple Syntax

- *Normal* Object-Oriented features (class, method calls, for
   example)

- *Advanced* Object-Oriented features(Mix-in, Singleton-method, for
   example)

- Operator Overloading

- Exception Handling

- Iterators and Closures

- Garbage Collection

- Dynamic Loading of Object Files (on some architectures)

- Highly Portable (works on many UNIX machines; DOS, Windows, Mac,
BeOS, and more)

%package devel
Summary:        Development files to link against Ruby
Group:          Development/Languages/Ruby
Requires:       %{name}
%requires_ge    ruby%{version}-devel

%description devel
Development files to link against Ruby.

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/ruby/README
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/ruby-devel/README

%files
%defattr(-,root,root)
%doc /usr/share/doc/packages/ruby/

%files devel
%defattr(-,root,root)
%doc /usr/share/doc/packages/ruby-devel/

%changelog
