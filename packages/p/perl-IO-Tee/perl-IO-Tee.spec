#
# spec file for package perl-IO-Tee
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


Name:           perl-IO-Tee
Version:        0.65
Release:        0
%define cpan_name IO-Tee
Summary:        Multiplex output to multiple output handles
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Tee/
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
'IO::Tee' objects can be used to multiplex input and output in two
different ways. The first way is to multiplex output to zero or more output
handles. The 'IO::Tee' constructor, given a list of output handles, returns
a tied handle that can be written to. When written to (using print or
printf), the 'IO::Tee' object multiplexes the output to the list of handles
originally passed to the constructor. As a shortcut, you can also directly
pass a string or an array reference to the constructor, in which case
'IO::File::new' is called for you with the specified argument or arguments.

The second way is to multiplex input from one input handle to zero or more
output handles as it is being read. The 'IO::Tee' constructor, given an
input handle followed by a list of output handles, returns a tied handle
that can be read from as well as written to. When written to, the 'IO::Tee'
object multiplexes the output to all handles passed to the constructor, as
described in the previous paragraph. When read from, the 'IO::Tee' object
reads from the input handle given as the first argument to the 'IO::Tee'
constructor, then writes any data read to the output handles given as the
remaining arguments to the constructor.

The 'IO::Tee' class supports certain 'IO::Handle' and 'IO::File' methods
related to input and output. In particular, the following methods will
iterate themselves over all handles associated with the 'IO::Tee' object,
and return TRUE indicating success if and only if all associated handles
returned TRUE indicating success:

* close

* truncate

* write

* syswrite

* format_write

* formline

* fcntl

* ioctl

* flush

* clearerr

* seek

The following methods perform input multiplexing as described above:

* read

* sysread

* readline

* getc

* gets

* eof

* getline

* getlines

The following methods can be used to set (but not retrieve) the current
values of output-related state variables on all associated handles:

* autoflush

* output_field_separator

* output_record_separator

* format_page_number

* format_lines_per_page

* format_lines_left

* format_name

* format_top_name

* format_line_break_characters

* format_formfeed

The following methods are directly passed on to the input handle given as
the first argument to the 'IO::Tee' constructor:

* input_record_separator

* input_line_number

Note that the return value of input multiplexing methods (such as 'print')
is always the return value of the input action, not the return value of
subsequent output actions. In particular, no error is indicated by the
return value if the input action itself succeeds but subsequent output
multiplexing fails.

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
%doc Changes README
%license LICENSE

%changelog
