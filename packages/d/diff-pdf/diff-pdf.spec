#
# spec file for package diff-pdf
#
# Copyright (c) 2023 SUSE LLC
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


Name:           diff-pdf
Version:        0.5
Release:        0
Summary:        Simple PDF comparison tool
License:        GPL-2.0-only AND LGPL-2.0-only
Group:          Productivity/Publishing/PDF
URL:            https://vslavik.github.io/diff-pdf/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-glib)

%description
diff-pdf is a simple tool for comparing two PDF files.

%prep
%autosetup

%build
./bootstrap
%configure
%make_build

%install
%make_install

#help2man -N -n "%%{summary}" --version-string="%%{version}" --no-discard-stderr \
#	  -o %%{buildroot}%%{_mandir}/man1/%%{name}.1 %%{buildroot}%%{_bindir}/%%{name}
install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ %{SOURCE1}

%files
%license COPYING COPYING.icons
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
