#
# spec file for package ed
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


Name:           ed
Version:        1.19
Release:        0
Summary:        A line-oriented text editor
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Text/Editors
URL:            https://www.gnu.org/software/ed/
# This is just recompressed from  https://ftp.gnu.org/gnu/ed/ed-%%{version}.tar.lz
# in order to avoid pulling lzip to ring0
Source0:        ed-%{version}.tar.zst
BuildRequires:  zstd
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

%description
GNU ed is a line-oriented text editor. It is used to create, display,
modify and otherwise manipulate text files, both interactively and via
shell scripts. A restricted version of ed, red, can only edit files in
the current directory and cannot execute shell commands. Ed is the
"standard" text editor in the sense that it is the original editor for
Unix, and thus widely available. For most purposes, however, it is
superseded by full-screen editors such as GNU Emacs or GNU Moe.

%prep
%setup -q

%build
%configure
%make_build CFLAGS="%{optflags}"

%install
%make_install

%check
%make_build check

%post
%install_info --entry="* ed: (ed). Line-oriented text editor" --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_bindir}/r%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/r%{name}.1%{?ext_man}

%changelog
