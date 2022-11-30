#
# spec file for package ucblogo
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ucblogo
Version:        6.2.2
Release:        0
Summary:        Berkeley Logo interpreter
License:        GPL-3.0-or-later
URL:            https://people.eecs.berkeley.edu/~bh/logo.html
Source:         https://github.com/jrincayc/ucblogo-code/releases/download/version_%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ucblogo-wxString-to-c_str.patch badshah400@gmail.com -- Explicitly convert a wxString to c_string to match calling function's definition
Patch0:         ucblogo-wxString-to-c_str.patch
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  makeinfo
BuildRequires:  wxGTK3-devel
Recommends:     %{name}-doc = %{version}

%description
Berkeley Logo interpreter is a free (both senses) interpreter for the Logo
programming language.

%package doc
Summary:       Documentation for ucblogo - a free logo interpreter
BuildArch:     noarch

%description doc
This package provides additional documentation for ucblogo.

%prep
%autosetup -p1

%build
%configure --enable-docs \
           --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

%fdupes %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/ucblogo
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.xpm
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files doc
%doc %{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/README.md

%changelog
