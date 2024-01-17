#
# spec file for package manpageeditor
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


%define oname ManPageEditor

Name:           manpageeditor
Version:        0.1.3
Release:        0
Summary:        A simple manual pages editor
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://keithdhedger.github.io/pages/manpageeditor/manpageeditor.html
Source0:        https://github.com/KeithDHedger/%{oname}/archive/refs/tags/%{version}.tar.gz#/%{oname}-%{version}.tar.gz
BuildRequires:  aspell-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  groff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gtksourceview-3.0)

%description
Create, edit, import, preview man-pages.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure \
  --enable-aspell \
  --enable-gtk3
%make_build

%install
%make_install
# Let's use %%doc macro.
rm -rfv %{buildroot}%{_datadir}/%{oname}/docs

%files
%license COPYING
%doc BUGS-ETC ChangeLog README 
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_mandir}/man1/manpageeditor.1*
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{oname}.png

%changelog
