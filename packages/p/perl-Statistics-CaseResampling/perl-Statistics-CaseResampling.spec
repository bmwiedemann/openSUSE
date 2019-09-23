#
# spec file for package perl-Statistics-CaseResampling
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


Name:           perl-Statistics-CaseResampling
Version:        0.15
Release:        0
%define cpan_name Statistics-CaseResampling
Summary:        Efficient resampling and calculation of medians with confidence intervals
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Statistics-CaseResampling/
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The purpose of this (XS) module is to calculate the median (or in principle
also other statistics) with confidence intervals on a sample. To do that,
it uses a technique called bootstrapping. In a nutshell, it resamples the
sample a lot of times and for each resample, it calculates the median. From
the distribution of medians, it then calculates the confidence limits.

In order to implement the confidence limit calculation, various other
functions had to be implemented efficiently (both algorithmically efficient
and done in C). These functions may be useful in their own right and are
thus exposed to Perl. Most notably, this exposes a median (and general
selection) algorithm that works in linear time as opposed to the trivial
implementation that requires 'O(n*log(n))'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes RdGen.xs.inc README

%changelog
