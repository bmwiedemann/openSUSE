#
# spec file for package perl-Wx
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


Name:           perl-Wx
Version:        0.9932
Release:        0
%define cpan_name Wx
Summary:        Interface to the Wxwidgets Cross-Platform Gui Toolkit
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Wx/
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDOOTSON/%{cpan_name}-%{version}.tar.gz
Source1:        perl-Wx-rpmlintrc
Source2:        cpanspec.yml
Patch0:         0001-Sort-output-of-dumped-dictionaries-for-reproducible-.patch
Patch1:         0002-Provide-overload-methods-to-XSpp-in-sorted-order.patch
Patch2:         0003-Define-overload-constants-in-sorted-order.patch
Patch3:         0004-Define-enum-values-in-sorted-order.patch
Patch4:         0001-fix-incomplete-Wx_Exp.pm-due-to-missing-dependecy-in.patch
Patch5:         fix_wxWidgets_3_0_3_API_break.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::wxWidgets) >= 0.25
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.15
BuildRequires:  perl(ExtUtils::XSpp) >= 0.1602
Requires:       perl(Alien::wxWidgets) >= 0.25
Requires:       perl(ExtUtils::MakeMaker) >= 6.46
Requires:       perl(ExtUtils::ParseXS) >= 3.15
Requires:       perl(ExtUtils::XSpp) >= 0.1602
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
BuildRequires:  wxWidgets-3_0-nostl-devel
%if 0%{?suse_version} <= 1500
# Since WxWidgets 3.0.4, the full version is encoded in the soname
Requires:       %(rpmqpack | grep libwx_baseu-suse-nostl)
%endif
BuildRequires:  xspp
# MANUAL END

%description
The Wx module is a wrapper for the wxWidgets (formerly known as wxWindows)
GUI toolkit.

This module comes with extensive documentation in HTML format; you can
download it from http://wxperl.sourceforge.net/

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
# MANUAL no testing (needs X)
#%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes docs README.txt samples typemap.tmpl typemap.xsp wxpl.ico wxpl.xpm Wx.rc

%changelog
