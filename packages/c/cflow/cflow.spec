#
# spec file for package cflow
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.6
Release:        0
Summary:        Tool to generate flowcharts for C sources
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://www.gnu.org/software/cflow
Source0:        https://ftp.gnu.org/gnu/cflow/cflow-1.6.tar.xz
Source1:        https://ftp.gnu.org/gnu/cflow/cflow-1.6.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  flex
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU cflow analyzes a collection of C source files and prints a graph, charting
control flow within the program. GNU cflow is able to produce both direct and
inverted flowgraphs for C sources. Optionally a cross-reference listing can be
generated. Two output formats are implemented: POSIX and GNU (extended). Input
files can optionally be preprocessed before analyzing.

%prep
%setup -q

%build
%configure \
  --disable-silent-rules
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files -f %{name}.lang
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
