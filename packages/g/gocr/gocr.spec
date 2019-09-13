#
# spec file for package gocr
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gocr
Version:        0.50
Release:        0
Summary:        Optical Character Recognition Program
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            http://jocr.sourceforge.net/
Source0:        http://www-e.uni-magdeburg.de/jschulen/ocr/%{name}-%{version}.tar.gz
Source1:        gocr.desktop
Source99:       %{name}.changes
BuildRequires:  libnetpbm-devel
BuildRequires:  transfig
BuildRequires:  update-desktop-files
Requires:       jpeg
Requires:       netpbm
Requires:       transfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GOCR is an optical character recognition program. It reads images in
many formats and outputs a text file. It is also able to recognize
and translate barcodes.

%package gui
Summary:        Optical Character Recognition Program - Basic Graphical Interface
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       tk
Requires(postun): update-desktop-files
Requires(pre):  update-desktop-files
Supplements:    packageand(gocr:tk)

%description gui
GOCR is an optical character recognition program. It reads images in
many formats and outputs a text file. It is also able to recognize
and translate barcodes.

This package contains a basic graphical interface for GOCR.

%prep
%setup -q

# Fix rpmlint warning "hidden-file-or-dir"
rm -f examples/.#Makefile.1.22

# Fix rpmlint warning "doc-file-dependency"
chmod 644 examples/score

# Remove build time references so build-compare can do its work (fix rpmlint warning "file-contains-current-date")
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/gocr.c

%build
# configure does not check if netpbm headers are installed in /usr/include/netpbm
export CPPFLAGS=-I%{_includedir}/netpbm
%configure
make %{?_smp_mflags}
make %{?_smp_mflags} examples

%install
%make_install

# Fix rpmlint warning "spurious-executable-perm"
chmod 644 %{buildroot}%{_mandir}/man1/gocr.1

# Fix doc files path in manpage
perl -pi -e "s|%{_datadir}/doc/gocr-\\\fBX.XX\\\fR/|%{_docdir}/gocr/|" %{buildroot}%{_mandir}/man1/gocr.1

# Install desktop file
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" OCR program

%post gui
%desktop_database_post

%postun gui
%desktop_database_postun

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS CREDITS HISTORY README READMEde.txt TODO gpl.html
%doc doc/{examples.txt,gocr.html,unicode.txt}
%doc examples/
%{_mandir}/man1/gocr.1%{ext_man}
%{_bindir}/gocr

%files gui
%defattr(-,root,root,-)
%{_bindir}/gocr.tcl
%{_datadir}/applications/gocr.desktop

%changelog
