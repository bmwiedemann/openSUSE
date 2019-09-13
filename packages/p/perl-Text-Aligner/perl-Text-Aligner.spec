#
# spec file for package perl-Text-Aligner
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


Name:           perl-Text-Aligner
Version:        0.13
Release:        0
%define cpan_name Text-Aligner
Summary:        Module to Align Text
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Aligner/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Term::ANSIColor) >= 2.02
Requires:       perl(Term::ANSIColor) >= 2.02
%{perl_requires}

%description
Text::Aligner exports a single function, align(), which is used to justify
strings to various alignment styles. The alignment specification is the
first argument, followed by any number of scalars which are subject to
alignment.

The operation depends on context. In list context, a list of the justified
scalars is returned. In scalar context, the justified arguments are joined
into a single string with newlines appended. The original arguments remain
unchanged. In void context, in-place justification is attempted. In this
case, all arguments must be lvalues.

Align() also does one level of scalar dereferencing. That is, whenever one
of the arguments is a scalar reference, the scalar pointed to is aligned
instead. Other references are simply stringified. An undefined argument is
interpreted as an empty string without complaint.

Alignment respects colorizing escape sequences a la Term::ANSIColor which
means it knows that these sequences don't take up space on the screen.

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
