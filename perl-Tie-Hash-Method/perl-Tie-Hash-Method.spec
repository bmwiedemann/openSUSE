#
# spec file for package perl-Tie-Hash-Method
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


Name:           perl-Tie-Hash-Method
Version:        0.02
Release:        0
%define cpan_name Tie-Hash-Method
Summary:        Tied hash with specific methods overriden by callbacks
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Tie-Hash-Method/
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Tie::Hash::Method provides a way to create a tied hash with specific
overriden behaviour without having to create a new class to do it. A tied
hash with no methods overriden is functionally equivalent to a normal hash.

Each method in a standard tie can be overriden by providing a callback to
the tie call. So for instance if you wanted a tied hash that changed 'foo'
into 'bar' on store you could say:

    tie my %hash, 'Tie::Hash::Method',
        STORE => sub {
            (my $v=pop)=~s/foo/bar/g if defined $_[2];
            return $_[0]->base_hash->{$_[1]}=$v;
        };

The callback is called with exactly the same arguments as the tie itself,
in particular the tied object is always passed as the first argument.

The tied object is itself an array, which contains a second hash in the
HASH slot (index 0) which is used to perform the default operations.

The callbacks available are in a hash keyed by name in the METHOD slot of
the array (index 1).

If your code needs to store extra data in the object it should be stored in
the PRIVATE slot of the object (index 2). No future release of this module
will ever use or alter anything in that slot.

The arguments passed to the tie constructor will be seperated by the case
of their keys. The ones with all capitals will be stored in the METHOD
hash, and the rest will be stored in the PRIVATE hash.

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
