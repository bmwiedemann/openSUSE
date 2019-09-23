#
# spec file for package perl-Test-Pod-Coverage
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Pod-Coverage
Version:        1.10
Release:        0
%define cpan_name Test-Pod-Coverage
Summary:        Check for pod coverage in your distribution.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Pod-Coverage/
Source:         http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Pod::Coverage)
Requires:       perl(Pod::Coverage)
%{perl_requires}

%description
Test::Pod::Coverage is used to create a test for your distribution, to
ensure that all relevant files in your distribution are appropriately
documented in pod.

Can also be called with the Pod::Coverage manpage parms.

    use Test::Pod::Coverage tests=>1;
    pod_coverage_ok(
        "Foo::Bar",
        { also_private => [ qr/^[A-Z_]+$/ ], },
        "Foo::Bar, with all-caps functions as privates",
    );

The the Pod::Coverage manpage parms are also useful for subclasses that
don't re-document the parent class's methods. Here's an example from the
Mail::SRS manpage.

    pod_coverage_ok( "Mail::SRS" ); # No exceptions

    # Define the three overridden methods.
    my $trustme = { trustme => [qr/^(new|parse|compile)$/] };
    pod_coverage_ok( "Mail::SRS::DB", $trustme );
    pod_coverage_ok( "Mail::SRS::Guarded", $trustme );
    pod_coverage_ok( "Mail::SRS::Reversable", $trustme );
    pod_coverage_ok( "Mail::SRS::Shortcut", $trustme );

Alternately, you could use the Pod::Coverage::CountParents manpage, which
always allows a subclass to reimplement its parents' methods without
redocumenting them. For example:

    my $trustparents = { coverage_class => 'Pod::Coverage::CountParents' };
    pod_coverage_ok( "IO::Handle::Frayed", $trustparents );

(The 'coverage_class' parameter is not passed to the coverage class with
other parameters.)

If you want POD coverage for your module, but don't want to make
Test::Pod::Coverage a prerequisite for installing, create the following as
your _t/pod-coverage.t_ file:

    use Test::More;
    eval "use Test::Pod::Coverage";
    plan skip_all => "Test::Pod::Coverage required for testing pod coverage" if $@;

    plan tests => 1;
    pod_coverage_ok( "Pod::Master::Html");

Finally, Module authors can include the following in a _t/pod-coverage.t_
file and have 'Test::Pod::Coverage' automatically find and check all
modules in the module distribution:

    use Test::More;
    eval "use Test::Pod::Coverage 1.00";
    plan skip_all => "Test::Pod::Coverage 1.00 required for testing POD coverage" if $@;
    all_pod_coverage_ok();

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

%changelog
