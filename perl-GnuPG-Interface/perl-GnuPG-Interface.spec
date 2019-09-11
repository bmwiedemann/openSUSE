#
# spec file for package perl-GnuPG-Interface
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


Name:           perl-GnuPG-Interface
Version:        0.52
Release:        0
%define cpan_name GnuPG-Interface
Summary:        Perl interface to GnuPG
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         1.patch
Patch1:         gpg2.2.6_7c85ac40660861e7507c43d043323c3f1b83921b.patch
Patch2:         gpg2.2.8_b356e7fda15e39e037da1888a24000a96fc85c90.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.78
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Moo) >= 0.091011
BuildRequires:  perl(MooX::HandlesVia) >= 0.001004
BuildRequires:  perl(MooX::late) >= 0.014
Requires:       perl(Math::BigInt) >= 1.78
Requires:       perl(Moo) >= 0.091011
Requires:       perl(MooX::HandlesVia) >= 0.001004
Requires:       perl(MooX::late) >= 0.014
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gpg2
Requires:       gpg2
# MANUAL END

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to perform
functions such as but not limited to encrypting, signing, decryption,
verification, and key-listing parsing.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

# old (open)SUSE distributions use too old gpg
%if 0%{suse_version} >= 1330
%check
# RT#88963
%{__make} test || :
%{__make} test
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
