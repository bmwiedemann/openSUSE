#
# spec file for package perl-Net-LibIDN2
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


%define cpan_name Net-LibIDN2
Name:           perl-Net-LibIDN2
Version:        1.02
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Summary:        Perl bindings for GNU Libidn2
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        Net-LibIDN2-1.02.tar.gz
BuildRequires:  libidn2-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Module::Build) >= 0.420000
%{perl_requires}

%description
Provides bindings for GNU Libidn2, a C library for handling
internationalized domain names based on IDNA 2008, Punycode and TR46.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
