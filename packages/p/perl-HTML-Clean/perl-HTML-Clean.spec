#
# spec file for package perl-HTML-Clean
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name HTML-Clean
Name:           perl-HTML-Clean
Version:        1.400.0
Release:        0
# 1.4 -> normalize -> 1.400.0
%define cpan_version 1.4
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTML::Clean - Cleans up HTML code for web browsers, not humans
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AZ/AZJADFTRE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(HTML::Clean) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The HTML::Clean module encapsulates a number of common techniques for
minimizing the size of HTML files. You can typically save between 10% and
50% of the size of a HTML file using these methods. It provides the
following features:

* Remove unneeded whitespace (begining of line, etc)

* Remove unneeded META elements.

* Remove HTML comments (except for styles, javascript and SSI)

* Replace tags with equivilant shorter tags (<strong> --> <b>)

* etc.

The entire proces is configurable, so you can pick and choose what you want
to clean.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
