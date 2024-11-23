#
# spec file for package text-engine
#
# Copyright (c) 2024 SUSE LLC
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


%define         soversion 0_1-0
Name:           text-engine
Version:        0.1.1
Release:        0
Summary:        A lightweight rich text framework for GTK
License:        LGPL-2.1-or-later OR MPL-2.0
URL:            https://github.com/mjakeman/text-engine
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-Wreturn-type.patch
Patch1:         add-soversion.patch
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)

%description
Text Engine is a rich-text editing framework for GTK 4. The primary user of this
library is bluetype but it can be used wherever rich text display and editing is
needed.

%package -n lib%{name}-%{soversion}
Summary:        %{summary}

%description -n lib%{name}-%{soversion}
%{summary}.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}-%{soversion} >= %{version}

%description -n lib%{name}-devel
%{summary}.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
%meson
%meson_build

%install
%meson_install
rm %{buildroot}%{_bindir}/text-engine-demo

%ldconfig_scriptlets -n lib%{name}-%{soversion}

%files -n lib%{name}-%{soversion}
%license COPYING
%doc README.md
%{_libdir}/lib%{name}*.so.*

%files -n lib%{name}-devel
%{_includedir}/text-engine
%{_libdir}/pkgconfig/text-engine-0.1.pc
%{_libdir}/lib%{name}*.so

%changelog
