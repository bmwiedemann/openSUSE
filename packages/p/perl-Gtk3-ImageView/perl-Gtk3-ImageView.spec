#
# spec file for package perl-Gtk3-ImageView
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


%define cpan_name Gtk3-ImageView
Name:           perl-Gtk3-ImageView
Version:        8
Release:        0
Summary:        Image viewer widget for Gtk3
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASOKOLOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(Glib) >= 1.21
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Glib) >= 1.21
Requires:       perl(Gtk3)
Requires:       perl(Readonly)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgtkimageview-devel
# MANUAL END

%description
The Gtk3::ImageView widget allows the user to zoom, pan and select the
specified image and provides hooks to allow additional tools, e.g. painter,
to be created and used.

Gtk3::ImageView is a Gtk3 port of Gtk2::ImageView.

To discuss Gtk3::ImageView or gtk3-perl, ask questions and flame/praise the
authors, join gtk-perl-list@gnome.org at lists.gnome.org.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# MANUAL no testing (requires Display)
#make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc README.md

%changelog
