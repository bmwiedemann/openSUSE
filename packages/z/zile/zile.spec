#
# spec file for package zile
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           zile
Version:        2.4.14
Release:        0
Summary:        Lightweight Emacs Clone
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
Url:            https://www.gnu.org/software/zile/
Source0:        https://ftp.gnu.org/gnu/zile/zile-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/zile/zile-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Source3:        zile.desktop
Source4:        zile.png
BuildRequires:  emacs-nox
BuildRequires:  help2man
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  termcap
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(bdw-gc)
Requires:       termcap
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Recommends:     %{name}-doc = %{version}
Provides:       %{name}-base = %{version}
Provides:       %{name}-desktop = %{version}
Obsoletes:      %{name}-base < %{version}
Obsoletes:      %{name}-desktop < %{version}
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(libacl)
%endif

%description
Zile is another Emacs-clone.  Zile is a customizable, self-documenting
real-time, open-source display editor.  Zile was written to be as similar
as possible to Emacs; every Emacs user should feel at home with Zile.

%package doc
Summary:        Lightweight Emacs Clone (Documentation)
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Zile is another Emacs-clone.  Zile is a customizable, self-documenting
real-time, open-source display editor.  Zile was written to be as similar
as possible to Emacs; every Emacs user should feel at home with Zile.

This package contains the documentation and the man page for %{name}.

%prep
%setup -q

%build
%configure \
  --disable-debug \
  --disable-silent-rules \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

install -m0644 -t "%{buildroot}%{_docdir}/%{name}/" ChangeLog COPYING README THANKS
install -Dp -m 0644 "%{SOURCE3}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
install -Dp -m 0644 "%{SOURCE4}" "%{buildroot}%{_datadir}/pixmaps/%{name}.png"
%suse_update_desktop_file "%{name}" Utility TextEditor

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/zile
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/zile.1%{ext_man}

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
