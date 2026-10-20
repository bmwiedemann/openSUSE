#
# spec file for package debianutils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           debianutils
Version:        5.24
Release:        0
Summary:        Miscellaneous utilities specific to Debian
License:        GPL-2.0-only
URL:            https://packages.debian.org/%{name}
Source:         https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  perl(Autom4te::C4che)
BuildRequires:  perl(Autom4te::ChannelDefs)
BuildRequires:  perl(Autom4te::Channels)
BuildRequires:  perl(Autom4te::Config)
BuildRequires:  perl(Autom4te::Configure_ac)
BuildRequires:  perl(Autom4te::FileUtils)
BuildRequires:  perl(Autom4te::General)
BuildRequires:  perl(Autom4te::Getopt)
BuildRequires:  perl(Autom4te::Request)
BuildRequires:  perl(Autom4te::XFile)
BuildRequires:  perl(Locale::Po4a::AsciiDoc)
BuildRequires:  perl(Locale::Po4a::BibTeX)
BuildRequires:  perl(Locale::Po4a::Chooser)
BuildRequires:  perl(Locale::Po4a::Common)
BuildRequires:  perl(Locale::Po4a::Debconf)
BuildRequires:  perl(Locale::Po4a::Dia)
BuildRequires:  perl(Locale::Po4a::Docbook)
BuildRequires:  perl(Locale::Po4a::Gemtext)
BuildRequires:  perl(Locale::Po4a::Guide)
BuildRequires:  perl(Locale::Po4a::Halibut)
BuildRequires:  perl(Locale::Po4a::Ini)
BuildRequires:  perl(Locale::Po4a::KernelHelp)
BuildRequires:  perl(Locale::Po4a::LaTeX)
BuildRequires:  perl(Locale::Po4a::Man)
BuildRequires:  perl(Locale::Po4a::NewsDebian)
BuildRequires:  perl(Locale::Po4a::Po)
BuildRequires:  perl(Locale::Po4a::Pod)
BuildRequires:  perl(Locale::Po4a::RubyDoc)
BuildRequires:  perl(Locale::Po4a::Sgml)
BuildRequires:  perl(Locale::Po4a::TeX)
BuildRequires:  perl(Locale::Po4a::Texinfo)
BuildRequires:  perl(Locale::Po4a::Text)
BuildRequires:  perl(Locale::Po4a::TransTractor)
BuildRequires:  perl(Locale::Po4a::Wml)
BuildRequires:  perl(Locale::Po4a::Xhtml)
BuildRequires:  perl(Locale::Po4a::Xml)
BuildRequires:  perl(Locale::Po4a::Yaml)

%description
* add-shell: add a shell to %{_sysconfdir}/shells
* ischroot: etects if it is currently running in a chroot
* run-parts: run scripts or programs in a directory
* remove-shell: remove a shell to %{_sysconfdir}/shells
* update-shells: update the list of valid login shells

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure
%make_build

%install
# savelog is under SMAIL license, don't install
install -Dt %{buildroot}%{_bindir} ischroot
install -Dt %{buildroot}%{_sbindir} add-shell
install -Dt %{buildroot}%{_sbindir} remove-shell
install -Dt %{buildroot}%{_bindir} run-parts
install -Dt %{buildroot}%{_sbindir} update-shells

install -m 0644 -Dt %{buildroot}%{_mandir}/man1 ischroot.1
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 add-shell.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 remove-shell.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 run-parts.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 update-shells.8

%files
%{_bindir}/ischroot
%{_sbindir}/add-shell
%{_sbindir}/remove-shell
%{_bindir}/run-parts
%{_sbindir}/update-shells
%{_mandir}/man1/ischroot.1%{?ext_man}
%{_mandir}/man8/add-shell.8%{?ext_man}
%{_mandir}/man8/remove-shell.8%{?ext_man}
%{_mandir}/man8/run-parts.8%{?ext_man}
%{_mandir}/man8/update-shells.8%{?ext_man}

%changelog
