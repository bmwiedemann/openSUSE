#
# spec file for package perl-App-rsync-retry
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name App-rsync-retry
Name:           perl-App-rsync-retry
Version:        0.007
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Rsync wrapper to retry on transfer errrors
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        App-rsync-retry-0.007.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long) >= 2.50
Requires:       perl(File::Which)
Requires:       perl(Getopt::Long) >= 2.50
%{perl_requires}

%description
Rsync wrapper to retry on transfer errrors

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%license LICENSE

%changelog
