#
# spec file for package perl-Ref-Util-XS
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


Name:           perl-Ref-Util-XS
Version:        0.117
Release:        0
%define cpan_name Ref-Util-XS
Summary:        XS implementation for Ref::Util
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Ref-Util-XS/
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
Ref::Util::XS is the XS implementation of Ref::Util, which provides several
functions to help identify references in a more convenient way than the
usual approach of examining the return value of 'ref'.

You should use Ref::Util::XS by installing Ref::Util itself: if the system
you install it on has a C compiler available, 'Ref::Util::XS' will be
installed and used automatically, providing a significant speed boost to
everything that uses 'Ref::Util'.

See Ref::Util for full documentation of the available functions.

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
%doc Changes README
%license LICENSE

%changelog
