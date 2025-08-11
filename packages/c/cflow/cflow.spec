#
# spec file for package cflow
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           cflow
Version:        1.8
Release:        0
Summary:        Tool to generate flowcharts for C sources
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://www.gnu.org/software/cflow
Source0:        https://ftp.gnu.org/gnu/cflow/cflow-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/cflow/cflow-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  flex

%description
GNU cflow analyzes a collection of C source files and prints a graph, charting
control flow within the program. GNU cflow is able to produce both direct and
inverted flowgraphs for C sources. Optionally a cross-reference listing can be
generated. Two output formats are implemented: POSIX and GNU (extended). Input
files can optionally be preprocessed before analyzing.

%prep
%autosetup -p1

%build
%configure \
  --disable-silent-rules
%make_build

%check
%make_build check

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}

%changelog
