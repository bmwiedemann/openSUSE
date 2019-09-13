#
# spec file for package perl-Gtk2-ImageView
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


Name:           perl-Gtk2-ImageView
Version:        0.05
Release:        0
%define cpan_name Gtk2-ImageView
Summary:        Perl bindings to the GtkImageView image viewer widget
License:        LGPL-3.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gtk2-ImageView/
Source:         http://www.cpan.org/authors/id/R/RA/RATCLIFFE/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(Glib) >= 1.140
BuildRequires:  perl(Gtk2) >= 1.140
Requires:       perl(ExtUtils::Depends) >= 0.2
Requires:       perl(ExtUtils::PkgConfig) >= 1.03
Requires:       perl(Glib) >= 1.140
Requires:       perl(Gtk2) >= 1.140
%{perl_requires}
# MANUAL
BuildRequires:  libgtkimageview-devel

%description
The Gtk2::ImageView module allows a Perl developer to use the GtkImageView
image viewer widget. Find out more about GtkImageView at
http://trac.bjourne.webfactional.com/.

To discuss Gtk2::ImageView or gtk2-perl, ask questions and flame/praise the
authors, join gtk-perl-list@gnome.org at lists.gnome.org.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
# MANUAL - requires Display
# %{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS COPYING.LESSER examples maps README style.css

%changelog
