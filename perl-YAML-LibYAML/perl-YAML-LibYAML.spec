#
# spec file for package perl-YAML-LibYAML
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


%define cpan_name YAML-LibYAML
Name:           perl-YAML-LibYAML
Version:        0.79
Release:        0
Summary:        Perl YAML Serialization using XS and libyaml
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Patch0:         %{name}-no-plan.patch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Perl YAML Serialization using XS and libyaml

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

# This patch is only necessary for systems without Test::More >= 0.87_01
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%patch0 -p1
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license LICENSE
%doc Changes README

%changelog
