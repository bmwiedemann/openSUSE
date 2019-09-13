#
# spec file for package paper-gtk-theme
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Sam Hewitt
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


Name:           paper-gtk-theme
Version:        2.1.0
Release:        0
Summary:        The 'Paper' Gtk theme
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://snwh.org/paper
Source:         https://github.com/snwh/paper-gtk-theme/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildArch:      noarch

%description
Paper is a modern desktop theme suite. Its design is mostly flat
with a minimal use of shadows for depth.

%package -n metatheme-paper-common
Summary:        Common files for the 'Paper' Gtk theme
Group:          System/GUI/Other
Recommends:     paper-icon-theme
Suggests:       gtk2-metatheme-paper
Suggests:       gtk3-metatheme-paper
# paper-gtk-theme was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n metatheme-paper-common
Paper is a modern desktop theme suite. Its design is mostly flat
with a minimal use of shadows for depth.

%package -n gtk2-metatheme-paper
Summary:        The 'Paper' theme for Gtk2
Group:          System/GUI/Other
Requires:       metatheme-paper-common = %{version}
Recommends:     gtk2-theming-engine-adwaita
Supplements:    packageand(metatheme-paper-common:gtk2)

%description -n gtk2-metatheme-paper
Paper is a modern desktop theme suite. Its design is mostly flat
with a minimal use of shadows for depth.

%package -n gtk3-metatheme-paper
Summary:        The 'Paper' theme for Gtk3
Group:          System/GUI/Other
Requires:       metatheme-paper-common = %{version}
Supplements:    packageand(metatheme-paper-common:gtk3)

%description -n gtk3-metatheme-paper
Paper is a modern desktop theme suite. Its design is mostly flat
with a minimal use of shadows for depth.

%prep
%setup -q
chmod a-x README.md Paper/gtk-2.0/gtkrc

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-paper-common
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_datadir}/themes/Paper/
%exclude %{_datadir}/themes/Paper/gtk-?.*/

%files -n gtk2-metatheme-paper
%defattr(-,root,root)
%{_datadir}/themes/Paper/gtk-2.*/

%files -n gtk3-metatheme-paper
%defattr(-,root,root)
%{_datadir}/themes/Paper/gtk-3.*/

%changelog
