#
# spec file for package intltool
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


Name:           intltool
Version:        0.51.0
Release:        0
Summary:        Internationalization Tool Collection
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://edge.launchpad.net/intltool/
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM intltool-perl-5.22.patch lp#1490906 dimstar@opensuse.org -- Fix execution with perl 5.22
Patch0:         intltool-perl-5.22.patch
# PATCH-FIX-UPSTREAM fixrace.patch lp#1687644 boo#1021335
Patch1:         fixrace.patch
# PATCH-FIX-UPSTREAM intltool-no-guess-builddir.patch lp#1117944 -- Fix out of tree builds with automake 1.15
Patch2:         intltool-no-guess-builddir.patch
BuildRequires:  perl-XML-Parser
Requires:       gettext-tools
Requires:       perl-XML-Parser
Provides:       xml-i18n-tools
Obsoletes:      xml-i18n-tools
BuildArch:      noarch

%description
Some scripts to support translators working on GNOME and similar
programs. Data available in XML files (.oaf, .desktop, .sheet, and
more) can be extracted into PO files. After translation, the new
information is written back into the XML files.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/intltool-*
%{_bindir}/intltoolize
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/intltool.m4
%{_datadir}/%{name}/
%{_mandir}/man8/intltool-*.8%{?ext_man}
%{_mandir}/man8/intltoolize.8%{?ext_man}

%changelog
