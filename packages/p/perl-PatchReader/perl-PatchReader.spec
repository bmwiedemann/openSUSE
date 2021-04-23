# vim: set sw=4 ts=4 et nu:
#
# spec file for package perl-PatchReader
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           perl-PatchReader
Version:        0.9.6
Release:        0
Summary:        Utilities to read and manipulate patches and CVS
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/T/TM/TMANNERM/PatchReader-%{version}.tar.gz
Url:            http://search.cpan.org/dist/PatchReader
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp) >= 0.05
Requires:       perl(Cwd) >= 2
Requires:       perl(File::Temp) >= 0.05
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description
This perl library allows you to manipulate patches programmatically by chaining
together a variety of objects that read, manipulate, and output patch
information.

%prep
%setup -q -n "PatchReader-%{version}"
%__sed -i '/^auto_install/d' Makefile.PL
%__sed -i 's/\r$//' \
    lib/PatchReader.pm \
    lib/PatchReader/Raw.pm \
    lib/PatchReader/FixPatchRoot.pm \
    README \
    Changes

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?_smp_flags}

%install
%perl_make_install
%perl_process_packlist

find "%{buildroot}%{perl_vendorlib}/" -type f -name '*.pm' -exec %__chmod 0644 {} \;

%check
%__make test

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/PatchReader.pm
%{perl_vendorlib}/PatchReader
%doc %{perl_man3dir}/PatchReader.%{perl_man3ext}%{ext_man}

%changelog
