#
# spec file for package perl-Browser-Open
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


%define cpan_name Browser-Open
Name:           perl-Browser-Open
Version:        0.40.0
Release:        0
# 0.04 -> normalize -> 0.40.0
%define cpan_version 0.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Open a browser in a given URL
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(parent)
Requires:       perl(Test::More) >= 0.92
Requires:       perl(parent)
Provides:       perl(Browser::Open) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The functions optionaly exported by this module allows you to open URLs in
the user browser.

A set of known commands per OS-name is tested for presence, and the first
one found is executed. With an optional parameter, all known commands are
checked.

The "open_browser" uses the 'system()' function to execute the command. If
you want more control, you can get the command with the "open_browser_cmd"
or "open_browser_cmd_all" functions and then use whatever method you want
to execute it.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
