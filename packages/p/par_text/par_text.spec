#
# spec file for package par_text
#
# Copyright (c) 2020 SUSE LLC
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


%define upname par
Name:           par_text
Version:        1.53.0+git.1584347654.eb0590f
Release:        0
Summary:        Paragraph reformatter
License:        MIT
Group:          Productivity/Text/Convertors
URL:            http://www.nicemice.net/par/
Source0:        par-%{version}.tar.gz
# I hope that these two packages are so specialised, they
# shouldn't be on one system.
Conflicts:      par

%description
par is a filter which copies its input to its output, changing all
white characters (except newlines) to spaces, and reformatting
each paragraph.  Paragraphs are separated by protected, blank, and
bodiless lines, and optionally delimited by indentation.

Each output paragraph is generated from the corresponding input
paragraph as follows:

1) An optional prefix and/or suffix is removed from each input line.
2) The remainder is divided into words (separated by spaces).
3) The words are joined into lines to make an eye-pleasing paragraph.
4) The prefixes and suffixes are reattached.

If there are suffixes, spaces are inserted before them so that they all
end in the same column.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
make -f protoMakefile CC="cc -c" LINK1="cc" LINK2="-o" RM="rm" JUNK="" %{?_smp_mflags} CFLAGS="%{optflags}"$*

%install
install -D -t %{buildroot}/%{_bindir} par
install -p -m 0644 -D -t %{buildroot}/%{_mandir}/man1 par.1

%files
%{_bindir}/par
%doc par.doc releasenotes
%{_mandir}/man1/par.1%{?ext_man}

%changelog
