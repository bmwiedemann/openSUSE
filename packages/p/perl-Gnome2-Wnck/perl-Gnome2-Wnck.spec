#
# spec file for package perl-Gnome2-Wnck
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Sascha Manns <saigkill@opensuse.org>
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


Name:           perl-Gnome2-Wnck
Version:        0.16
Release:        0
%define cpan_name Gnome2-Wnck
Summary:        Perl interface to the Window Navigator Construction Kit
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gnome2-Wnck/
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(Glib) >= 1.180
BuildRequires:  perl(Gtk2) >= 1.00
%if 0%{?suse_version} && 0%{?suse_version} < 1140 
BuildRequires:  perl-macros
%endif
BuildRequires:  pkgconfig(libwnck-1.0)
Requires:       perl(ExtUtils::Depends) >= 0.20
Requires:       perl(ExtUtils::PkgConfig) >= 1.03
Requires:       perl(Glib) >= 1.180
Requires:       perl(Gtk2) >= 1.00
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description
This module allows you to use the Window Navigator Construction Kit library
(libwnck for short) from Perl.

The index of the automatically generated API documentation can be accessed
with:

  perldoc Gnome2::Wnck::index

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE maps NEWS README

%changelog
