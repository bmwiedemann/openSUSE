#
# spec file for package perl-HTML-Clean
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


Name:           perl-HTML-Clean
Version:        1.2
Release:        0
%define cpan_name HTML-Clean
Summary:        Cleans up HTML code for web browsers, not humans
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AZ/AZJADFTRE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The HTML::Clean module encapsulates a number of common techniques for
minimizing the size of HTML files. You can typically save between 10% and
50% of the size of a HTML file using these methods. It provides the
following features:

* Remove unneeded whitespace (beginning of line, etc)

* Remove unneeded META elements.

* Remove HTML comments (except for styles, javascript and SSI)

* Replace tags with equivalent shorter tags (<strong> --> <b>)

* etc.

The entire process is configurable, so you can pick and choose what you want
to clean.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README TODO

%changelog
