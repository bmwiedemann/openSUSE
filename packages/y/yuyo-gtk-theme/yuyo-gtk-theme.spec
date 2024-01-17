#
# spec file for package yuyo-gtk-theme
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


%define _name yuyo
Name:           yuyo-gtk-theme
Version:        0.3
Release:        0
Summary:        Yuyo Gtk Theme
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://github.com/snwh/yuyo-gtk-theme
Source:         http://archive.ubuntu.com/ubuntu/pool/universe/y/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch

%description
Yuyo has light and dark variations and a flat style with crisp
clean lines.

%package -n metatheme-%{_name}-common
Summary:        Yuyo Gtk Theme -- Common Files
Group:          System/GUI/Other
Recommends:     ubuntu-mate-icon-theme
Suggests:       gtk2-metatheme-%{_name}
Suggests:       gtk3-metatheme-%{_name}

%description -n metatheme-%{_name}-common
Yuyo has light and dark variations and a flat style with crisp
clean lines.

%package -n gtk2-metatheme-%{_name}
Summary:        Yuyo Gtk Theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk2)

%description -n gtk2-metatheme-%{_name}
Yuyo has light and dark variations and a flat style with crisp
clean lines.

%package -n gtk3-metatheme-%{_name}
Summary:        Yuyo Gtk Theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk3)

%description -n gtk3-metatheme-%{_name}
Yuyo has light and dark variations and a flat style with crisp
clean lines.

%prep
%setup -q
chmod a-x README.md

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -a Yuyo* %{buildroot}%{_datadir}/themes/
%fdupes %{buildroot}%{_datadir}/themes/

%files -n metatheme-%{_name}-common
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_datadir}/themes/Yuyo*/
%exclude %{_datadir}/themes/Yuyo*/gtk-?.0/

%files -n gtk2-metatheme-%{_name}
%defattr(-,root,root)
%{_datadir}/themes/Yuyo*/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%defattr(-,root,root)
%{_datadir}/themes/Yuyo*/gtk-3.0/

%changelog
