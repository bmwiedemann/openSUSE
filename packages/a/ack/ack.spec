#
# spec file for package ack
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ack
Version:        3.8.0
Release:        0
Summary:        Grep-Like Text Finder
License:        Artistic-2.0
Group:          Productivity/Text/Utilities
URL:            https://beyondgrep.com/
Source:         https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/ack-v%{version}.tar.gz
Patch1:         ack-ignore-osc.patch
Patch3:         ack-add_spec.patch
BuildRequires:  make
BuildRequires:  perl >= 5.10.1
BuildRequires:  perl(File::Next) >= 1.18
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl >= 5.10.1
Requires:       perl-App-Ack = %{version}-%{release}
Requires:       perl-base = %{perl_version}
BuildArch:      noarch

%description
ack is a grep-like tool tailored to working with large trees of source code.

%package -n perl-App-Ack
Summary:        Grep-Like Text Finder Perl Module
Group:          Development/Libraries/Perl
Requires:       perl-base = %{perl_version}
Requires:       perl(File::Next) >= 1.18

%description -n perl-App-Ack
App::Ack is a grep-like tool tailored to working with large trees of source
code.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
perl Makefile.PL
%make_build

%install
%perl_make_install
%perl_process_packlist
# remove .packlist file
rm -rf "%{buildroot}%{perl_vendorarch}/auto/ack"
rm -f "%{buildroot}%{_localstatedir}/adm/perl-modules/ack"

%check
%make_build test

%files
%license LICENSE.md
%{_bindir}/ack
%{_mandir}/man1/ack.1%{?ext_man}

%files -n perl-App-Ack
%license LICENSE.md
%doc Changes README.md
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Ack.pm
%{perl_vendorlib}/App/Ack
%if 0%{?perl_process_packlist:1}
%endif

%changelog
