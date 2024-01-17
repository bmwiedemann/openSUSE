#
# spec file for package perl-String-Formatter
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name String-Formatter
Name:           perl-String-Formatter
Version:        1.235
Release:        0
License:        GPL-1.0-or-later
Summary:        Build sprintf-like functions of your own
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Params::Util)
Requires:       perl(Sub::Exporter)
%{perl_requires}

%description
String::Formatter is a tool for building sprintf-like formatting routines.
It supports named or positional formatting, custom conversions, fixed
string interpolation, and simple width-matching out of the box. It is easy
to alter its behavior to write new kinds of format string expanders. For
most cases, it should be easy to build all sorts of formatters out of the
options built into String::Formatter.

Normally, String::Formatter will be used to import a sprintf-like routine
referred to as "'stringf'", but which can be given any name you like. This
routine acts like sprintf in that it takes a string and some inputs and
returns a new string:

  my $output = stringf "Some %a format %s for you to %u.\n", { ... };

This routine is actually a wrapper around a String::Formatter object
created by importing stringf. In the following code, the entire hashref
after "stringf" is passed to String::Formatter's constructor (the 'new'
method), save for the '-as' key and any other keys that start with a dash.

  use String::Formatter
    stringf => {
      -as => 'fmt_time',
      codes           => { ... },
      format_hunker   => ...,
      input_processor => ...,
    },
    stringf => {
      -as => 'fmt_date',
      codes           => { ... },
      string_replacer => ...,
      hunk_formatter  => ...,
    },
  ;

As you can see, this will generate two stringf routines, with different
behaviors, which are installed with different names. Since the behavior of
these routines is based on the 'format' method of a String::Formatter
object, the rest of the documentation will describe the way the object
behaves.

There's also a 'named_stringf' export, which behaves just like the
'stringf' export, but defaults to the 'named_replace' and
'require_named_input' arguments. There's a 'method_stringf' export, which
defaults 'method_replace' and 'require_single_input'. Finally, a
'indexed_stringf', which defaults to 'indexed_replaced' and
'require_arrayref_input'. For more on these, keep reading, and check out
the cookbook.

String::Formatter::Cookbook provides a number of recipes for ways to put
String::Formatter to use.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
