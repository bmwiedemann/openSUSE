#
# spec file for package perl-Spiffy
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


Name:           perl-Spiffy
Version:        0.46
Release:        0
%define cpan_name Spiffy
Summary:        Spiffy Perl Interface Framework For You
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Spiffy/
Source:         http://www.cpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts
to fix all the nits and warts of traditional Perl OO, in a clean,
straightforward and (perhaps someday) standard way.

Spiffy borrows ideas from other OO languages like Python, Ruby, Java and
Perl 6. It also adds a few tricks of its own.

If you take a look on CPAN, there are a ton of OO related modules. When
starting a new project, you need to pick the set of modules that makes most
sense, and then you need to use those modules in each of your classes.
Spiffy, on the other hand, has everything you'll probably need in one
module, and you only need to use it once in one of your classes. If you
make Spiffy.pm the base class of the basest class in your project, Spiffy
will automatically pass all of its magic to all of your subclasses. You may
eventually forget that you're even using it!

The most striking difference between Spiffy and other Perl object oriented
base classes, is that it has the ability to export things. If you create a
subclass of Spiffy, all the things that Spiffy exports will automatically
be exported by your subclass, in addition to any more things that you want
to export. And if someone creates a subclass of your subclass, all of those
things will be exported automatically, and so on. Think of it as "Inherited
Exportation", and it uses the familiar Exporter.pm specification syntax.

To use Spiffy or any subclass of Spiffy as a base class of your class, you
specify the '-base' argument to the 'use' command.

    use MySpiffyBaseModule -base;

You can also use the traditional 'use base 'MySpiffyBaseModule';' syntax
and everything will work exactly the same. The only caveat is that
Spiffy.pm must already be loaded. That's because Spiffy rewires base.pm on
the fly to do all the Spiffy magics.

Spiffy has support for Ruby-like mixins with Perl6-like roles. Just like
'base' you can use either of the following invocations:

    use mixin 'MySpiffyBaseModule';
    use MySpiffyBaseModule -mixin;

The second version will only work if the class being mixed in is a subclass
of Spiffy. The first version will work in all cases, as long as Spiffy has
already been loaded.

To limit the methods that get mixed in, use roles. (Hint: they work just
like an Exporter list):

    use MySpiffyBaseModule -mixin => qw(:basics x y !foo);

In object oriented Perl almost every subroutine is a method. Each method
gets the object passed to it as its first argument. That means practically
every subroutine starts with the line:

    my $self = shift;

Spiffy provides a simple, optional filter mechanism to insert that line for
you, resulting in cleaner code. If you figure an average method has 10
lines of code, that's 10% of your code! To turn this option on, you just
use the '- Base' option instead of the '-base' option, or add the
'-selfless' option. If source filtering makes you queazy, don't use the
feature. I personally find it addictive in my quest for writing squeaky
clean, maintainable code.

A useful feature of Spiffy is that it exports two functions: 'field' and
'const' that can be used to declare the attributes of your class, and
automatically generate accessor methods for them. The only difference
between the two functions is that 'const' attributes can not be modified;
thus the accessor is much faster.

One interesting aspect of OO programming is when a method calls the same
method from a parent class. This is generally known as calling a super
method. Perl's facility for doing this is butt ugly:

    sub cleanup {
        my $self = shift;
        $self->scrub;
        $self->SUPER::cleanup(@_);
    }

Spiffy makes it, er, super easy to call super methods. You just use the
'super' function. You don't need to pass it any arguments because it
automatically passes them on for you. Here's the same function with Spiffy:

    sub cleanup {
        $self->scrub;
        super;
    }

Spiffy has a special method for parsing arguments called 'parse_arguments',
that it also uses for parsing its own arguments. You declare which
arguments are boolean (singletons) and which ones are paired, with two
special methods called 'boolean_arguments' and 'paired_arguments'. Parse
arguments pulls out the booleans and pairs and returns them in an anonymous
hash, followed by a list of the unmatched arguments.

Finally, Spiffy can export a few debugging functions 'WWW', 'XXX', 'YYY'
and 'ZZZ'. Each of them produces a YAML dump of its arguments. WWW warns
the output, XXX dies with the output, YYY prints the output, and ZZZ
confesses the output. If YAML doesn't suit your needs, you can switch all
the dumps to Data::Dumper format with the '-dumper' option.

That's Spiffy!

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
%doc Changes CONTRIBUTING LICENSE README

%changelog
