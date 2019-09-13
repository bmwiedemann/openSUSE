#
# spec file for package perl-Term-ProgressBar
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


Name:           perl-Term-ProgressBar
Version:        2.22
Release:        0
%define cpan_name Term-ProgressBar
Summary:        Provide a Progress Meter On a Standard Terminal
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Term-ProgressBar/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.13
BuildRequires:  perl(Class::MethodMaker) >= 1.02
BuildRequires:  perl(Term::ReadKey) >= 2.14
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.80
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Class::MethodMaker) >= 1.02
Requires:       perl(Term::ReadKey) >= 2.14
%{perl_requires}

%description
Term::ProgressBar provides a simple progress bar on the terminal, to let
the user know that something is happening, roughly how much stuff has been
done, and maybe an estimate at how long remains.

A typical use sets up the progress bar with a number of items to do, and
then calls update to update the bar whenever an item is processed.

Often, this would involve updating the progress bar many times with no
user-visible change. To avoid unnecessary work, the update method returns a
value, being the update value at which the user will next see a change. By
only calling update when the current value exceeds the next update value,
the call overhead is reduced.

Remember to call the '$progress->update($max_value)' when the job is done
to get a nice 100% done bar.

A progress bar by default is simple; it just goes from left-to-right,
filling the bar with '=' characters. These are called *major* characters.
For long-running jobs, this may be too slow, so two additional features are
available: a linear completion time estimator, and/or a *minor* character:
this is a character that _moves_ from left-to-right on the progress bar (it
does not fill it as the major character does), traversing once for each
major-character added. This exponentially increases the granularity of the
bar for the same width.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes examples README

%changelog
