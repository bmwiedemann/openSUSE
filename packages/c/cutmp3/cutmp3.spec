#
# spec file for package cutmp3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Packman Team <packman@links2linux.de>
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


Name:           cutmp3
Version:        3.0.1
Release:        0
Summary:        Command line based lossless MP3 editor
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            https://www.puchalla-online.de/cutmp3.html
Source:         https://www.puchalla-online.de/cutmp3-%{version}.tar.bz2
Source1:        https://www.puchalla-online.de/cutmp3-keys.pdf
Source2:        https://www.puchalla-online.de/cutmp3-keys.jpg
Source99:       %{name}-rpmlintrc
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
Requires:       mpg123
Obsoletes:      %{name}-kde3

%description
This is a program to split MP3 files without quality loss, using an
ncurses-based user interface. Beginning and end of a segment can be
marked with the 'a' and 'b' keys and the segment be saved with 's'.
VBR files are supported. Using a timetable with VBR files will not be
as precise as with CBR files, though.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
This is a program to edit MP3 files without quality loss, using an
ncurses-based user interface.

This package contains a user guide and a list of key bindings for %{name}

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -m 0755 -D cutmp3 "%{buildroot}%{_bindir}/cutmp3"
install -D -m 0644 cutmp3.1 "%{buildroot}%{_mandir}/man1/cutmp3.1"

install -d "%{buildroot}%{_docdir}/%{name}"
D="$PWD/main.doc.lst"
echo -n >"$D"
for f in BUGS COPYING USAGE README*; do
    b="${f##*/}"
    install -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$b"
    echo "%doc %{_docdir}/%{name}/$b" >>"$D"
done
D="$PWD/doc.doc.lst"
echo -n >"$D"
for f in "%{SOURCE1}" "%{SOURCE2}" TODO Changelog; do
    b="${f##*/}"
    install -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$b"
    echo "%doc %{_docdir}/%{name}/$b" >>"$D"
done

%files -f main.doc.lst
%dir %doc %{_docdir}/%{name}
%{_bindir}/cutmp3
%{_mandir}/man1/cutmp3.1%{ext_man}

%files doc -f doc.doc.lst
%dir %doc %{_docdir}/%{name}

%changelog
