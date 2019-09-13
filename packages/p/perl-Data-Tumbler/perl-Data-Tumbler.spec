#
# spec file for package perl-Data-Tumbler
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


Name:           perl-Data-Tumbler
Version:        0.010
Release:        0
%define cpan_name Data-Tumbler
Summary:        Dynamic generation of nested combinations of variants
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Most) >= 0.33
%{perl_requires}

%description
NOTE: This is alpha code and liable to change while it and
Test::WriteVariants mature.

The tumble() method calls a sequence of 'provider' code references each of
which returns a hash. The first provider is called and then, for each hash
item it returns, the tumble() method recurses to call the next provider.

The recursion continues until there are no more providers to call, at which
point the consumer code reference is called. Effectively the providers
create a tree of combinations and the consumer is called at the leafs of
the tree.

If a provider returns no items then that part of the tree is pruned.
Further providers, if any, are not called and the consumer is not called.

During a call to tumble() three values are passed down through the tree and
into the consumer: path, context, and payload.

The path and context are derived from the names and values of the hashes
returned by the providers. Typically the path define the current "path"
through the tree of combinations.

The providers are passed the current path, context, and payload. The
payload is cloned at each level of recursion so that any changes made to it
by providers are only visible within the scope of the generated sub-tree.

Note that although the example above shows the path, context and payload as
array references, the tumbler code makes no assumptions about them. They
can be any kinds of values.

See Test::WriteVariants for a practical example use.

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
%doc Changes LICENSE README TODO
%license ARTISTIC-1.0 GPL-1 GPL-2.0 LICENSE

%changelog
