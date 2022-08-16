#
# spec file for package perl-Digest-SHA3
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Digest-SHA3
Name:           perl-Digest-SHA3
Version:        1.05
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for SHA-3
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Digest::SHA3 is written in C for speed. If your platform lacks a C
compiler, perhaps you can find the module in a binary form compatible with
your particular processor and operating system.

The programming interface is easy to use: it's the same one found in CPAN's
Digest module. So, if your applications currently use Digest::SHA and you'd
prefer the newer flavor of the NIST standard, it's a simple matter to
convert them.

The interface provides two ways to calculate digests: all-at-once, or in
stages. To illustrate, the following short program computes the SHA3-256
digest of "hello world" using each approach:

	use Digest::SHA3 qw(sha3_256_hex);

	$data = "hello world";
	@frags = split(//, $data);

	# all-at-once (Functional style)
	$digest1 = sha3_256_hex($data);

	# in-stages (OOP style)
	$state = Digest::SHA3->new(256);
	for (@frags) { $state->add($_) }
	$digest2 = $state->hexdigest;

	print $digest1 eq $digest2 ?
		"that's the ticket!\n" : "oops!\n";

To calculate the digest of an n-bit message where _n_ is not a multiple of
8, use the _add_bits()_ method. For example, consider the 446-bit message
consisting of the bit-string "110" repeated 148 times, followed by "11".
Here's how to display its SHA3-512 digest:

	use Digest::SHA3;
	$bits = "110" x 148 . "11";
	$sha3 = Digest::SHA3->new(512)->add_bits($bits);
	print $sha3->hexdigest, "\n";

Note that for larger bit-strings, it's more efficient to use the
two-argument version _add_bits($data, $nbits)_, where _$data_ is in the
customary packed binary format used for Perl strings.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README sha3sum

%changelog
