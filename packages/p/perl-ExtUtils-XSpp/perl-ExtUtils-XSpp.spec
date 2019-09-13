#
# spec file for package perl-ExtUtils-XSpp
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-ExtUtils-XSpp
Version:        0.18
Release:        0
%define cpan_name ExtUtils-XSpp
Summary:        XS for C++
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/ExtUtils-XSpp/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.07
BuildRequires:  perl(ExtUtils::Typemaps) >= 1
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Differences)
Requires:       perl(ExtUtils::ParseXS) >= 3.07
Requires:       perl(ExtUtils::Typemaps) >= 1
%{perl_requires}
# MANUAL
Provides:       xspp = %{version}
Obsoletes:      xspp < %{version}
Provides:       perl(ExtUtils::XSpp) = %{version}00
Requires:       gcc-c++

%description
Anything that does not look like a XS++ directive or a class declaration is
passed verbatim to XS. If you want XS++ to ignore code that looks like a
XS++ directive or class declaration, simply surround it with a raw block
delimiter like this:

  %{
  XS++ won't interpret this
  %}

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README scripts XSP.yp

%changelog
