#
# spec file for package perl-CSS-Tiny
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CSS-Tiny
Version:        1.20
Release:        0
%define cpan_name CSS-Tiny
Summary:        Read/Write .css files with as little code as possible
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CSS-Tiny/
Source0:        http://www.cpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'CSS::Tiny' is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead. CSS.pm
requires about 2.6 meg or ram to load, which is a large amount of overhead
if you only want to do trivial things. Memory usage is normally scoffed at
in Perl, but in my opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to CSS.pm. With the increasing
complexity of CSS, this is becoming more common, but many situations can
still live with simple CSS files.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes test.css

%changelog
