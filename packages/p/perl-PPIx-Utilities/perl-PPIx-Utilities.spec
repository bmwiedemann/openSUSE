#
# spec file for package perl-PPIx-Utilities
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-PPIx-Utilities
Version:        1.001000
Release:        0
%define cpan_name PPIx-Utilities
Summary:        Extensions to L<PPI|PPI>
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PPIx-Utilities/
Source:         http://www.cpan.org/authors/id/E/EL/ELLIOTJS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PPI) >= 1.208
BuildRequires:  perl(PPI::Document) >= 1.208
BuildRequires:  perl(PPI::Document::Fragment) >= 1.208
BuildRequires:  perl(PPI::Dumper) >= 1.208
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
Requires:       perl(Exception::Class)
Requires:       perl(PPI) >= 1.208
Requires:       perl(PPI::Document::Fragment) >= 1.208
Requires:       perl(Readonly)
Requires:       perl(Task::Weaken)
Recommends:     perl(Readonly::XS)
%{perl_requires}

%description
This is a collection of functions for dealing with PPI objects, many of
which originated in Perl::Critic. They are organized into modules by the
kind of PPI class they relate to, by replacing the "PPI" at the front of
the module name with "PPIx::Utilities", e.g. functionality related to
PPI::Nodes is in PPIx::Utilities::Node.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README xt

%changelog
