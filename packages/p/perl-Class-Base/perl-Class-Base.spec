#
# spec file for package perl-Class-Base
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Class-Base
Version:        0.09
Release:        0
%define cpan_name Class-Base
Summary:        Useful Base Class for Deriving Other Modules
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Base/
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
Requires:       perl(Clone)
%{perl_requires}

%description
Please consider using Badger::Base instead which is the successor of this
module.

This module implements a simple base class from which other modules can be
derived, thereby inheriting a number of useful methods such as 'new()',
'init()', 'params()', 'clone()', 'error()' and 'debug()'.

For a number of years, I found myself re-writing this module for
practically every Perl project of any significant size. Or rather, I would
copy the module from the last project and perform a global search and
replace to change the names. Each time it got a little more polished and
eventually, I decided to Do The Right Thing and release it as a module in
it's own right.

It doesn't pretend to be an all-encompassing solution for every kind of
object creation problem you might encounter. In fact, it only supports
blessed hash references that are created using the popular, but by no means
universal convention of calling 'new()' with a list or reference to a hash
array of named parameters. Constructor failure is indicated by returning
undef and setting the '$ERROR' package variable in the module's class to
contain a relevant message (which you can also fetch by calling 'error()'
as a class method).

e.g.

    my $object = My::Module->new( 
	file => 'myfile.html',
	msg  => 'Hello World'
    ) || die $My::Module::ERROR;

or:

    my $object = My::Module->new({
	file => 'myfile.html',
	msg  => 'Hello World',
    }) || die My::Module->error();

The 'new()' method handles the conversion of a list of arguments into a
hash array and calls the 'init()' method to perform any initialisation. In
many cases, it is therefore sufficient to define a module like so:

    package My::Module;
    use Class::Base;
    use base qw( Class::Base );

    sub init {
	my ($self, $config) = @_;
	# copy some config items into $self
	$self->params($config, qw( FOO BAR )) || return undef;
	return $self;
    }

    # ...plus other application-specific methods

    1;

Then you can go right ahead and use it like this:

    use My::Module;

    my $object = My::Module->new( FOO => 'the foo value',
				  BAR => 'the bar value' )
        || die $My::Module::ERROR;

Despite its limitations, Class::Base can be a surprisingly useful module to
have lying around for those times where you just want to create a regular
object based on a blessed hash reference and don't want to worry too much
about duplicating the same old code to bless a hash, define configuration
values, provide an error reporting mechanism, and so on. Simply derive your
module from 'Class::Base' and leave it to worry about most of the detail.
And don't forget, you can always redefine your own 'new()', 'error()', or
other method, if you don't like the way the Class::Base version works.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTORS doap.xml README README.mkdn TODO
%license LICENSE

%changelog
