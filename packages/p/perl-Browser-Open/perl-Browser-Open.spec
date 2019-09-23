#
# spec file for package perl-Browser-Open
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Browser-Open
Version:        0.04
Release:        0
%define cpan_name Browser-Open
Summary:        Open a browser in a given URL
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Browser-Open/
Source:         http://www.cpan.org/authors/id/C/CF/CFRANKS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(parent)
#BuildRequires: perl(Browser::Open)
Requires:       perl(Test::More) >= 0.92
Requires:       perl(parent)
%{perl_requires}

%description
The functions optionaly exported by this module allows you to open URLs in
the user browser.

A set of known commands per OS-name is tested for presence, and the first
one found is executed. With an optional parameter, all known commands are
checked.

The the "open_browser" manpage uses the 'system()' function to execute the
command. If you want more control, you can get the command with the the
"open_browser_cmd" manpage or the "open_browser_cmd_all" manpage functions
and then use whatever method you want to execute it.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
