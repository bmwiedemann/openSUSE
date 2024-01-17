#
# spec file for package mined
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


Name:           mined
Version:        2022.27
Release:        0
Summary:        Powerful Text Editor with Extensive Unicode and CJK Support
License:        GPL-3.0-or-later
Group:          Productivity/Editors/Other
URL:            https://mined.github.io/
Source:         https://github.com/mined/mined/archive/refs/tags/%{version}.tar.gz
Source2:        http://unicode.org/Public/UNIDATA/Unihan.zip
BuildRequires:  fdupes
BuildRequires:  unzip
BuildRequires:  update-desktop-files

%description
Mined is a powerful text editor with a comprehensive yet concise and
easy-to-use user interface supporting modern interaction paradigms,
and fast, small-footprint behaviour.

Mined provides both extensive Unicode and CJK support offering many
specific features and covering special cases that other editors
are not aware of (like auto-detection features and automatic handling
of terminal variations, or Han character information).
It was the first editor that supported Unicode in a plain-text terminal
(like xterm or rxvt).

%package -n xmined
Summary:        Graphical interface using Xterm of Mined text editor
Group:          Productivity/Editors/Other
Requires:       mined = %{version}
%if 0%{?suse_version} > 1320
Requires:       xterm-bin
%else
Requires:       xterm
%endif

%description -n xmined
Mined is a powerful text editor with a comprehensive yet concise and
easy-to-use user interface supporting modern interaction paradigms,
and fast, small-footprint behaviour.

Mined provides both extensive Unicode and CJK support offering many
specific features and covering special cases that other editors
are not aware of (like auto-detection features and automatic handling
of terminal variations, or Han character information).
It was the first editor that supported Unicode in a plain-text terminal
(like xterm or rxvt).

%prep
%setup -q
# desktop file fix
sed -i "s/mined.xpm/mined/" ./usrshare/setup_install/mined.desktop
sed -i s/Utility/Utility\;/ ./usrshare/setup_install/mined.desktop

%build
cp -p %{SOURCE2} src
%configure
make OPT="%{optflags}" USRLIBDIR=%{_libdir} ROOTLIBDIR=/%{_lib} %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# fix links
rm -rf %{buildroot}%{_bindir}/{minmacs,mpico,mstar}
for i in minmacs mpico mstar ; do
	ln -sf %{_bindir}/mined %{buildroot}%{_bindir}/${i}
done

# Documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/doc_user/* %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}/package_doc/* %{buildroot}%{_docdir}/%{name}/
# CHANGES -> doc_user/changes.html
rm -rf %{buildroot}%{_docdir}/%{name}/CHANGES

# Remove files for Windows but needed for build
# and useless directories (package_doc, doc_user)
rm -rf %{buildroot}%{_datadir}/%{name}/bin/
mv %{buildroot}%{_datadir}/%{name}/setup_install/bin %{buildroot}%{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/%{name}/{setup_install,doc_user,package_doc}

%suse_update_desktop_file %{name} TextEditor Utility

%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/mined
%{_bindir}/minmacs
%{_bindir}/mpico
%{_bindir}/mstar
%{_mandir}/man1/mined.1.gz
%{_mandir}/man1/minmacs.1.gz
%{_mandir}/man1/mpico.1.gz
%{_mandir}/man1/mstar.1.gz
%{_datadir}/%{name}
%doc %{_docdir}/%{name}

%files -n xmined
%defattr(-,root,root)
%{_bindir}/umined
%{_bindir}/uterm
%{_bindir}/xmined
%{_mandir}/man1/umined.1.gz
%{_mandir}/man1/uterm.1.gz
%{_mandir}/man1/xmined.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
